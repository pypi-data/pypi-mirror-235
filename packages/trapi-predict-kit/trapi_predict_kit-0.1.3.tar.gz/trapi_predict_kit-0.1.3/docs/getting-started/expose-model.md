This page explains how to integrate and expose a model through TRAPI using `trapi-predict-kit`.

## Define the endpoint

To expose a pre-trained model, you will need to create a function taking an input ID and returning predictions for it. We recommend to do it in a specific file, e.g. `predict.py`

The `trapi-predict-kit` package provides a decorator `@trapi_predict` to annotate your functions that generate predictions. Predictions generated from functions decorated with `@trapi_predict` can easily be imported in the Translator OpenPredict API, exposed as an API endpoint to get predictions from the web, and queried through the Translator Reasoner API (TRAPI).

The annotated predict functions are expected to take 2 input arguments: the input ID (string) and options for the prediction (dictionary). And it should return a dictionary with a list of predicted associated entities hits (see below for a practical example)

Here is an example:

```python
from trapi_predict_kit import trapi_predict, PredictOptions, PredictOutput

@trapi_predict(path='/predict',
    name="Get predicted targets for a given entity",
    description="Return the predicted targets for a given entity: drug (DrugBank ID) or disease (OMIM ID), with confidence scores.",
    edges=[
        {
            'subject': 'biolink:Drug',
            'predicate': 'biolink:treats',
            'object': 'biolink:Disease',
        },
        {
            'subject': 'biolink:Disease',
            'predicate': 'biolink:treated_by',
            'object': 'biolink:Drug',
        },
    ],
	nodes={
        "biolink:Disease": {
            "id_prefixes": [
                "OMIM"
            ]
        },
        "biolink:Drug": {
            "id_prefixes": [
                "DRUGBANK"
            ]
        }
    }
)
def get_predictions(
        input_id: str, options: PredictOptions
    ) -> PredictOutput:
    # Add the code the load the model and get predictions here
    predictions = {
        "hits": [
            {
                "id": "drugbank:DB00001",
                "type": "biolink:Drug",
                "score": 0.12345,
                "label": "Leipirudin",
            }
        ],
        "count": 1,
    }
    return predictions
```

If you generated a project from the template you will find it in the `predict.py` script.

## Define the API

You will need to instantiate a `TRAPI` class to deploy a Translator Reasoner API serving a list of prediction functions that have been decorated with `@trapi_predict`. For example:

```python
import logging

from trapi_predict_kit import TRAPI, settings
from my_model.predict import get_predictions


log_level = logging.INFO
logging.basicConfig(level=log_level)

openapi_info = {
    "contact": {
        "name": "Firstname Lastname",
        "email": "email@example.com",
        # "x-id": "https://orcid.org/0000-0000-0000-0000",
        "x-role": "responsible developer",
    },
    "license": {
        "name": "MIT license",
        "url": "https://opensource.org/licenses/MIT",
    },
    "termsOfService": 'https://github.com/your-org-or-username/my-model/blob/main/LICENSE.txt',

    "x-translator": {
        "component": 'KP',
        # TODO: update the Translator team to yours
        "team": [ "Clinical Data Provider" ],
        "biolink-version": settings.BIOLINK_VERSION,
        "infores": 'infores:openpredict',
        "externalDocs": {
            "description": "The values for component and team are restricted according to this external JSON schema. See schema and examples at url",
            "url": "https://github.com/NCATSTranslator/translator_extensions/blob/production/x-translator/",
        },
    },
    "x-trapi": {
        "version": settings.TRAPI_VERSION,
        "asyncquery": False,
        "operations": [
            "lookup",
        ],
        "externalDocs": {
            "description": "The values for version are restricted according to the regex in this external JSON schema. See schema and examples at url",
            "url": "https://github.com/NCATSTranslator/translator_extensions/blob/production/x-trapi/",
        },
    }
}

app = TRAPI(
    predict_endpoints=[ get_predictions ],
    info=openapi_info,
    title='OpenPredict TRAPI',
    version='1.0.0',
    openapi_version='3.0.1',
    description="""Machine learning models to produce predictions that can be integrated to Translator Reasoner APIs.
\n\nService supported by the [NCATS Translator project](https://ncats.nih.gov/translator/about)""",
    itrb_url_prefix="openpredict",
    dev_server_url="https://openpredict.semanticscience.org",
)
```

## Deploy the API

If you used the template to generate your project you can deploy the API with the `api` script defined in the `pyproject.toml` (refere to your generated project README for more details):

```bash
hatch run api
```

Otherwise you can use `uvicorn` or `gunicorn`:

```bash
uvicorn trapi.main:app --port 8808 --reload
```
