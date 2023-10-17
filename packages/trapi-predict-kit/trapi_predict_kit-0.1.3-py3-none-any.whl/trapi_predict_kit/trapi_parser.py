import re

import requests

from trapi_predict_kit.config import settings
from trapi_predict_kit.utils import get_entities_labels, log

# TODO: add evidence path to TRAPI


def is_accepted_id(id_to_check):
    return id_to_check.lower().startswith("omim") or id_to_check.lower().startswith("drugbank")


def get_biolink_parents(concept):
    concept_snakecase = concept.replace("biolink:", "")
    concept_snakecase = re.sub(r"(?<!^)(?=[A-Z])", "_", concept_snakecase).lower()
    query_url = f"https://bl-lookup-sri.renci.org/bl/{concept_snakecase}/ancestors"
    try:
        resolve_curies = requests.get(query_url, timeout=settings.TIMEOUT)
        # TODO: can't specify a BioLink version because asking for v3.1.0 does not exist, so we use latest
        # resolve_curies = requests.get(query_url,
        #                     params={'version': f'v{settings.BIOLINK_VERSION}'})
        resp = resolve_curies.json()
        resp.append(concept)
        return resp
    except Exception as e:
        log.warn(f"Error querying {query_url}, using the original IDs: {e}")
        return [concept]


def resolve_ids_with_nodenormalization_api(resolve_ids_list, resolved_ids_object):
    resolved_ids_list = []
    ids_to_normalize = []
    for id_to_resolve in resolve_ids_list:
        if is_accepted_id(id_to_resolve):
            resolved_ids_list.append(id_to_resolve)
            resolved_ids_object[id_to_resolve] = id_to_resolve
        else:
            ids_to_normalize.append(id_to_resolve)

    # Query Translator NodeNormalization API to convert IDs to OMIM/DrugBank IDs
    if len(ids_to_normalize) > 0:
        try:
            resolve_curies = requests.get(
                "https://nodenormalization-sri.renci.org/get_normalized_nodes",
                params={"curie": ids_to_normalize},
                timeout=settings.TIMEOUT,
            )
            # Get corresponding OMIM IDs for MONDO IDs if match
            resp = resolve_curies.json()
            for resolved_id, alt_ids in resp.items():
                for alt_id in alt_ids["equivalent_identifiers"]:
                    if is_accepted_id(str(alt_id["identifier"])):
                        main_id = str(alt_id["identifier"])
                        # NOTE: fix issue when NodeNorm returns OMIM.PS: instead of OMIM:
                        if main_id.lower().startswith("omim"):
                            main_id = "OMIM:" + main_id.split(":", 1)[1]
                        resolved_ids_list.append(main_id)
                        resolved_ids_object[main_id] = resolved_id
        except Exception:
            log.warn("Error querying the NodeNormalization API, using the original IDs")
    # log.info(f"Resolved: {resolve_ids_list} to {resolved_ids_object}")
    return resolved_ids_list, resolved_ids_object


def resolve_id(id_to_resolve, resolved_ids_object):
    if id_to_resolve in resolved_ids_object:
        return resolved_ids_object[id_to_resolve]
    return id_to_resolve


def resolve_trapi_query(reasoner_query, endpoints_list):
    """Main function for TRAPI
    Convert an array of predictions objects to ReasonerAPI format
    Run the get_predict to get the QueryGraph edges and nodes
    {disease: OMIM:1567, drug: DRUGBANK:DB0001, score: 0.9}

    :param: reasoner_query Query from Reasoner API
    :return: Results as ReasonerAPI object
    """
    # Example TRAPI message: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/examples/Message/simple.json
    query_graph = reasoner_query["message"]["query_graph"]
    # Default query_options
    model_id = None
    n_results = None
    min_score = None
    max_score = None
    query_options = {}
    if "query_options" in reasoner_query:
        query_options = reasoner_query["query_options"]
        if "n_results" in query_options:
            n_results = int(query_options["n_results"])
        if "min_score" in query_options:
            min_score = float(query_options["min_score"])
        if "max_score" in query_options:
            max_score = float(query_options["max_score"])
        if "model_id" in query_options:
            model_id = str(query_options["model_id"])

    query_plan = {}
    resolved_ids_object = {}

    # if not similarity_embeddings or similarity_embeddings == {}:
    # similarity_embeddings = None
    # treatment_embeddings = None

    # Parse the query_graph to build the query plan
    for edge_id, qg_edge in query_graph["edges"].items():
        # Build dict with all infos of associations to predict
        query_plan[edge_id] = {
            # 'predicates': qg_edge['predicates'],
            # 'qedge_subjects': qg_edge['subject'],
            "qg_source_id": qg_edge["subject"],
            "qg_target_id": qg_edge["object"],
        }
        query_plan[edge_id]["predicates"] = qg_edge["predicates"]

        # If single value provided for predicate: make it an array
        # if not isinstance(query_plan[edge_id]['predicate'], list):
        #     query_plan[edge_id]['predicate'] = [ query_plan[edge_id]['predicate'] ]

        # Get the nodes infos in the query plan object
        for node_id, node in query_graph["nodes"].items():
            if node_id == qg_edge["subject"]:
                query_plan[edge_id]["subject_qg_id"] = node_id
                query_plan[edge_id]["subject_types"] = node.get("categories", ["biolink:NamedThing"])
                if "ids" in node:
                    query_plan[edge_id]["subject_kg_id"], resolved_ids_object = resolve_ids_with_nodenormalization_api(
                        node["ids"], resolved_ids_object
                    )
                    query_plan[edge_id]["ids_to_predict"] = query_plan[edge_id]["subject_kg_id"]
                    query_plan[edge_id]["types_to_predict"] = query_plan[edge_id]["subject_types"]
                    query_plan[edge_id]["relation_to_predict"] = "subject"
                    query_plan[edge_id]["relation_predicted"] = "object"

            if node_id == qg_edge["object"]:
                query_plan[edge_id]["object_qg_id"] = node_id
                query_plan[edge_id]["object_types"] = node.get("categories", ["biolink:NamedThing"])
                if "ids" in node:
                    query_plan[edge_id]["object_kg_id"], resolved_ids_object = resolve_ids_with_nodenormalization_api(
                        node["ids"], resolved_ids_object
                    )
                    if "ids_to_predict" not in query_plan[edge_id]:
                        query_plan[edge_id]["ids_to_predict"] = query_plan[edge_id]["object_kg_id"]
                        query_plan[edge_id]["types_to_predict"] = query_plan[edge_id]["object_types"]
                        query_plan[edge_id]["relation_to_predict"] = "object"
                        query_plan[edge_id]["relation_predicted"] = "subject"

    knowledge_graph = {"nodes": {}, "edges": {}}
    node_dict = {}
    query_results = []
    kg_edge_count = 0

    # Now iterates the query plan to execute each query
    for edge_qg_id in query_plan:
        # TODO: exit if no ID provided? Or check already done before?

        for predict_func in endpoints_list:
            # TODO: run the functions in parallel with future.concurrent

            for prediction_relation in predict_func._trapi_predict["edges"]:
                predicate_parents = get_biolink_parents(prediction_relation["predicate"])
                subject_parents = get_biolink_parents(prediction_relation["subject"])
                object_parents = get_biolink_parents(prediction_relation["object"])

                # TODO: add support for "qualifier_constraints" on query edges. cf. https://github.com/NCATSTranslator/testing/blob/main/ars-requests/not-none/1.2/mvp2cMetformin.json

                # Check if requested subject/predicate/object are served by the function
                if (
                    any(i in predicate_parents for i in query_plan[edge_qg_id]["predicates"])
                    and any(i in subject_parents for i in query_plan[edge_qg_id]["subject_types"])
                    and any(i in object_parents for i in query_plan[edge_qg_id]["object_types"])
                ):
                    # TODO: pass all ids_to_predict instead of iterating
                    # And also pass the list of target IDs if provided: query_plan[edge_qg_id]["object_kg_id"]
                    # if "subject_kg_id" in query_plan[edge_id]
                    #     and "object_kg_id" in query_plan[edge_id]
                    # New params are: input_ids, target_ids (target can be None, input is length 1 minimum)
                    for id_to_predict in query_plan[edge_id]["ids_to_predict"]:
                        labels_dict = get_entities_labels([id_to_predict])
                        label_to_predict = None
                        if id_to_predict in labels_dict:
                            label_to_predict = labels_dict[id_to_predict]["id"]["label"]
                        try:
                            log.info(f"🔮⏳️ Getting predictions for: {id_to_predict}")
                            # Run function to get predictions
                            prediction_results = predict_func(
                                id_to_predict,
                                {
                                    "model_id": model_id,
                                    "min_score": min_score,
                                    "max_score": max_score,
                                    "n_results": n_results,
                                    "types": query_plan[edge_id]["types_to_predict"],
                                    # "types": query_plan[edge_qg_id]['from_type'],
                                },
                            )
                            prediction_json = prediction_results["hits"]
                        except Exception as e:
                            log.error(f"Error getting the predictions: {e}")
                            prediction_json = []

                        for association in prediction_json:
                            # id/type of nodes are registered in a dict to avoid duplicate in knowledge_graph.nodes
                            # Build dict of node ID : label
                            source_node_id = resolve_id(id_to_predict, resolved_ids_object)
                            target_node_id = resolve_id(association["id"], resolved_ids_object)

                            # TODO: XAI get path between source and target nodes (first create the function for this)

                            # If the target ID is given, we filter here from the predictions
                            # if 'to_kg_id' in query_plan[edge_qg_id] and target_node_id not in query_plan[edge_qg_id]['to_kg_id']:
                            if (
                                "subject_kg_id" in query_plan[edge_id]
                                and "object_kg_id" in query_plan[edge_id]
                                and target_node_id not in query_plan[edge_qg_id]["object_kg_id"]
                            ):
                                pass

                            else:
                                edge_kg_id = "e" + str(kg_edge_count)
                                # Get the ID of the predicted entity in result association
                                # based on the type expected for the association "to" node
                                # node_dict[id_to_predict] = query_plan[edge_qg_id]['from_type']
                                # node_dict[association[query_plan[edge_qg_id]['to_type']]] = query_plan[edge_qg_id]['to_type']
                                rel_to_predict = query_plan[edge_id]["relation_to_predict"]
                                rel_predicted = query_plan[edge_id]["relation_predicted"]
                                node_dict[source_node_id] = {"type": query_plan[edge_qg_id][f"{rel_to_predict}_types"]}
                                if label_to_predict:
                                    node_dict[source_node_id]["label"] = label_to_predict

                                node_dict[target_node_id] = {"type": association["type"]}
                                if "label" in association:
                                    node_dict[target_node_id]["label"] = association["label"]
                                else:
                                    # TODO: improve to avoid to call the resolver everytime
                                    labels_dict = get_entities_labels([target_node_id])
                                    if target_node_id in labels_dict and labels_dict[target_node_id]:
                                        node_dict[target_node_id]["label"] = labels_dict[target_node_id]["id"]["label"]

                                # edge_association_type = 'biolink:ChemicalToDiseaseOrPhenotypicFeatureAssociation'
                                # relation = 'RO:0002434' # interacts with
                                # relation = 'OBOREL:0002606'
                                association_score = str(association["score"])

                                model_id_label = model_id
                                if not model_id_label:
                                    model_id_label = "openpredict_baseline"

                                # See attributes examples: https://github.com/NCATSTranslator/Evidence-Provenance-Confidence-Working-Group/blob/master/attribute_epc_examples/COHD_TRAPI1.1_Attribute_Example_2-3-21.yml
                                edge_dict = {
                                    # TODO: not required anymore? 'association_type': edge_association_type,
                                    # 'relation': relation,
                                    # More details on attributes: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/docs/reference.md#attribute-
                                    "sources": [
                                        {
                                            "resource_id": "infores:openpredict",
                                            "resource_role": "primary_knowledge_source",
                                        },
                                        {"resource_id": "infores:cohd", "resource_role": "supporting_data_source"},
                                    ],
                                    "attributes": [
                                        {
                                            "description": "model_id",
                                            "attribute_type_id": "EDAM:data_1048",
                                            "value": model_id_label,
                                        },
                                        # {
                                        #     # TODO: use has_confidence_level?
                                        #     "description": "score",
                                        #     "attribute_type_id": "EDAM:data_1772",
                                        #     "value": association_score
                                        #     # https://www.ebi.ac.uk/ols/ontologies/edam/terms?iri=http%3A%2F%2Fedamontology.org%2Fdata_1772&viewMode=All&siblings=false
                                        # },
                                        # https://github.com/NCATSTranslator/ReasonerAPI/blob/1.4/ImplementationGuidance/Specifications/knowledge_level_agent_type_specification.md
                                        {
                                            "attribute_type_id": "biolink:agent_type",
                                            "value": "computational_model",
                                            "attribute_source": "infores:openpredict",
                                        },
                                        {
                                            "attribute_type_id": "biolink:knowledge_level",
                                            "value": "prediction",
                                            "attribute_source": "infores:openpredict",
                                        },
                                    ],
                                    # "knowledge_types": knowledge_types
                                }

                                # Map the source/target of query_graph to source/target of association
                                # if association['source']['type'] == query_plan[edge_qg_id]['from_type']:
                                edge_dict["subject"] = source_node_id
                                edge_dict["object"] = target_node_id

                                # TODO: Define the predicate depending on the association source type returned by OpenPredict classifier
                                if len(query_plan[edge_qg_id]["predicates"]) > 0:
                                    edge_dict["predicate"] = query_plan[edge_qg_id]["predicates"][0]
                                else:
                                    edge_dict["predicate"] = prediction_relation["predicate"]

                                # Add the association in the knowledge_graph as edge
                                # Use the type as key in the result association dict (for IDs)
                                knowledge_graph["edges"][edge_kg_id] = edge_dict

                                # Add the bindings to the results object
                                result = {
                                    "node_bindings": {},
                                    "analyses": [
                                        {
                                            "resource_id": "infores:openpredict",
                                            "score": association_score,
                                            "scoring_method": "Model confidence between 0 and 1",
                                            "edge_bindings": {edge_qg_id: [{"id": edge_kg_id}]},
                                        }
                                    ],
                                    # 'edge_bindings': {},
                                }
                                # result['edge_bindings'][edge_qg_id] = [
                                #     {
                                #         "id": edge_kg_id
                                #     }
                                # ]
                                result["node_bindings"][query_plan[edge_qg_id][f"{rel_to_predict}_qg_id"]] = [
                                    {"id": source_node_id}
                                ]
                                result["node_bindings"][query_plan[edge_qg_id][f"{rel_predicted}_qg_id"]] = [
                                    {"id": target_node_id}
                                ]
                                query_results.append(result)

                                kg_edge_count += 1
                                if kg_edge_count == n_results:
                                    break

    # Generate kg nodes from the dict of nodes + result from query to resolve labels
    for node_id, properties in node_dict.items():
        node_category = properties["type"]
        if isinstance(node_category, str) and not node_category.startswith("biolink:"):
            node_category = "biolink:" + node_category.capitalize()
        if isinstance(node_category, str):
            node_category = [node_category]
        node_to_add = {
            "categories": node_category,
        }
        if "label" in properties and properties["label"]:
            node_to_add["name"] = properties["label"]
        knowledge_graph["nodes"][node_id] = node_to_add

    return {
        "message": {"knowledge_graph": knowledge_graph, "query_graph": query_graph, "results": query_results},
        "query_options": query_options,
        "reasoner_id": "infores:openpredict",
        "schema_version": settings.TRAPI_VERSION,
        "biolink_version": settings.BIOLINK_VERSION,
        "status": "Success",
        # "logs": [
        #     {
        #         "code": None,
        #         "level": "INFO",
        #         "message": "No descendants found from Ontology KP for QNode 'n00'.",
        #         "timestamp": "2023-04-05T07:24:26.646711"
        #     },
        # ]
    }


example_trapi = {
    "message": {
        "query_graph": {
            "edges": {"e01": {"object": "n1", "predicates": ["biolink:treated_by", "biolink:treats"], "subject": "n0"}},
            "nodes": {
                "n0": {"categories": ["biolink:Disease", "biolink:Drug"], "ids": ["OMIM:246300", "DRUGBANK:DB00394"]},
                "n1": {"categories": ["biolink:Drug", "biolink:Disease"]},
            },
        }
    },
    "query_options": {"max_score": 1, "min_score": 0.5},
}
