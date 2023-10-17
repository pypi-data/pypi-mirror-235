import logging
import uuid
from datetime import datetime
from itertools import zip_longest
from typing import Any, List, Optional

import requests
from rdflib import RDF, Graph, Literal, Namespace, URIRef
from rdflib.namespace import DC, RDFS, XSD

from trapi_predict_kit.config import settings

## Instantiate logging utility
log = logging.getLogger("uvicorn.error")
log.propagate = False
log_level = logging.getLevelName(settings.LOG_LEVEL)
log.setLevel(log_level)
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s: [%(module)s:%(funcName)s] %(message)s")
console_handler.setFormatter(formatter)
log.addHandler(console_handler)


def resolve_entities(label: str) -> Any:
    """Use Translator SRI Name Resolution API to get the preferred Translator ID"""
    resp = requests.post(
        "https://name-resolution-sri.renci.org/lookup",
        params={"string": label, "limit": 3},
        timeout=settings.TIMEOUT,
    )
    return resp.json()


def normalize_id_to_translator(ids_list: List[str]) -> dict:
    """Use Translator SRI NodeNormalization API to get the preferred Translator ID
    for an ID https://nodenormalization-sri.renci.org/docs
    """
    converted_ids_obj = {}
    resolve_curies = requests.get(
        "https://nodenormalization-sri.renci.org/get_normalized_nodes",
        params={"curie": ids_list},
        timeout=settings.TIMEOUT,
    )
    # Get corresponding OMIM IDs for MONDO IDs if match
    resp = resolve_curies.json()
    for converted_id, translator_ids in resp.items():
        try:
            pref_id = translator_ids["id"]["identifier"]
            log.info(converted_id + " > " + pref_id)
            converted_ids_obj[converted_id] = pref_id
        except Exception:
            log.error("❌️ " + converted_id + " > " + str(translator_ids))
    return converted_ids_obj


def get_entity_types(entity: str) -> Any:
    """Use Translator SRI NodeNormalization API to get the preferred Translator ID
    for an ID https://nodenormalization-sri.renci.org/docs
    """
    resolve_curies = requests.get(
        "https://nodenormalization-sri.renci.org/get_normalized_nodes",
        params={"curie": [entity]},
        timeout=settings.TIMEOUT,
    )
    # Get corresponding OMIM IDs for MONDO IDs if match
    resp = resolve_curies.json()
    if entity in resp:
        return resp[entity]["type"]
    return []


def get_entities_labels(entity_list: List[str]) -> Any:
    """Send the list of node IDs to Translator Normalization API to get labels
    See API: https://nodenormalization-sri.renci.org/apidocs/#/Interfaces/get_get_normalized_nodes
    and example notebook: https://github.com/TranslatorIIPrototypes/NodeNormalization/blob/master/documentation/NodeNormalization.ipynb
    """
    # TODO: add the preferred identifier CURIE to our answer also?
    label_results = {}
    entity_list = list(entity_list)
    for chunk in split_list(entity_list, 300):
        try:
            get_label_result = requests.get(
                "https://nodenormalization-sri.renci.org/get_normalized_nodes",
                params={"curie": chunk},
                timeout=settings.TIMEOUT,
            )
            label_results.update(get_label_result.json())
        except Exception as e:
            # Catch if the call to the API fails (API not available)
            logging.warn(
                f"Error getting entities labels from NodeNormalization API ({e}), it might be down: https://nodenormalization-sri.renci.org/docs"
            )
    return label_results


def split_list(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


OPENPREDICT_GRAPH = "https://w3id.org/openpredict/graph"
OPENPREDICT_NAMESPACE = "https://w3id.org/openpredict/"
BIOLINK = Namespace("https://w3id.org/biolink/vocab/")

OWL = Namespace("http://www.w3.org/2002/07/owl#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
SCHEMA = Namespace("http://schema.org/")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
PROV = Namespace("http://www.w3.org/ns/prov#")
MLS = Namespace("http://www.w3.org/ns/mls#")
OPENPREDICT = Namespace("https://w3id.org/openpredict/")


def get_run_metadata(scores: dict, model_features: dict, hyper_params: dict, run_id: Optional[str] = None) -> Graph:
    """Generate RDF metadata for a classifier and save it in data/openpredict-metadata.ttl, based on OpenPredict model:
    https://github.com/fair-workflows/openpredict/blob/master/data/rdf/results_disjoint_lr.nq

    :param scores: scores
    :param model_features: List of features in the model
    :param label: label of the classifier
    :return: Run id
    """
    g = Graph()
    g.bind("mls", Namespace("http://www.w3.org/ns/mls#"))
    g.bind("prov", Namespace("http://www.w3.org/ns/prov#"))
    g.bind("dc", Namespace("http://purl.org/dc/elements/1.1/"))
    g.bind("openpredict", Namespace("https://w3id.org/openpredict/"))

    if not run_id:
        # Generate random UUID for the run ID
        run_id = str(uuid.uuid1())

    run_uri = URIRef(OPENPREDICT_NAMESPACE + "run/" + run_id)
    run_prop_prefix = OPENPREDICT_NAMESPACE + run_id + "/"
    evaluation_uri = URIRef(OPENPREDICT_NAMESPACE + "run/" + run_id + "/ModelEvaluation")
    # The same for all run:
    implementation_uri = URIRef(OPENPREDICT_NAMESPACE + "implementation/OpenPredict")

    # Add Run metadata
    g.add((run_uri, RDF.type, MLS["Run"]))
    g.add((run_uri, DC.identifier, Literal(run_id)))
    g.add((run_uri, PROV["generatedAtTime"], Literal(datetime.now(), datatype=XSD.dateTime)))
    g.add((run_uri, MLS["realizes"], OPENPREDICT["LogisticRegression"]))
    g.add((run_uri, MLS["executes"], implementation_uri))
    g.add((run_uri, MLS["hasOutput"], evaluation_uri))
    g.add((run_uri, MLS["hasOutput"], URIRef(run_prop_prefix + "Model")))

    # Add Model, should we point it to the generated model?
    g.add((URIRef(run_prop_prefix + "Model"), RDF.type, MLS["Model"]))

    # Add implementation metadata
    g.add((OPENPREDICT["LogisticRegression"], RDF.type, MLS["Algorithm"]))
    g.add((implementation_uri, RDF.type, MLS["Implementation"]))
    g.add((implementation_uri, MLS["implements"], OPENPREDICT["LogisticRegression"]))

    # Add HyperParameters and their settings to implementation
    for hyperparam, hyperparam_setting in hyper_params.items():
        hyperparam_uri = URIRef(OPENPREDICT_NAMESPACE + "HyperParameter/" + hyperparam)
        g.add((implementation_uri, MLS["hasHyperParameter"], hyperparam_uri))
        g.add((hyperparam_uri, RDF.type, MLS["HyperParameter"]))
        g.add((hyperparam_uri, RDFS.label, Literal(hyperparam)))

        hyperparam_setting_uri = URIRef(OPENPREDICT_NAMESPACE + "HyperParameterSetting/" + hyperparam)
        g.add((implementation_uri, MLS["hasHyperParameter"], hyperparam_setting_uri))
        g.add((hyperparam_setting_uri, RDF.type, MLS["HyperParameterSetting"]))
        g.add((hyperparam_setting_uri, MLS["specifiedBy"], hyperparam_uri))
        g.add((hyperparam_setting_uri, MLS["hasValue"], Literal(hyperparam_setting)))
        g.add((run_uri, MLS["hasInput"], hyperparam_setting_uri))

    # TODO: improve how we retrieve features
    for feature in model_features:
        feature_uri = URIRef(
            OPENPREDICT_NAMESPACE + "feature/" + feature.replace(" ", "_").replace("(", "").replace(")", "")
        )
        g.add((feature_uri, RDF.type, MLS["Feature"]))
        g.add((feature_uri, DC.identifier, Literal(feature)))
        g.add((run_uri, MLS["hasInput"], feature_uri))

    # TODO: those 2 triples are for the PLEX ontology
    g.add((evaluation_uri, RDF.type, PROV["Entity"]))
    g.add((evaluation_uri, PROV["wasGeneratedBy"], run_uri))

    # Add scores as EvaluationMeasures
    g.add((evaluation_uri, RDF.type, MLS["ModelEvaluation"]))
    for key in scores:
        key_uri = URIRef(run_prop_prefix + key)
        g.add((evaluation_uri, MLS["specifiedBy"], key_uri))
        g.add((key_uri, RDF.type, MLS["EvaluationMeasure"]))
        g.add((key_uri, RDFS.label, Literal(key)))
        g.add((key_uri, MLS["hasValue"], Literal(scores[key], datatype=XSD.double)))
        # TODO: The Example 1 puts hasValue directly in the ModelEvaluation
        # but that prevents to provide multiple values for 1 evaluation
        # http://ml-schema.github.io/documentation/ML%20Schema.html#overview

    return g
