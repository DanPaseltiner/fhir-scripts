from phdi.cloud.gcp import GcpCredentialManager
from phdi.fhir.transport.http import fhir_server_get
import json

"""
This script provides a brief example of using functionality from the PHDI repository to
easily query a GCP FHIR Store for patient resources.
"""

credential_manager = GcpCredentialManager()

# Set values required constructing a GCP FHIR Store URL
project_id = credential_manager.get_project_id()
dataset_id = "phdi-dev-dataset-phdi-357418"
location = "us-west1"
fhir_store_id = "phdi-dev-fhirstore"

# Construct FHIR Store URL.
base_url = "https://healthcare.googleapis.com/v1/projects"
fhir_store_url = [
    base_url,
    project_id,
    "locations",
    location,
    "datasets",
    dataset_id,
    "fhirStores",
    fhir_store_id,
    "fhir",
]
fhir_store_url = "/".join(fhir_store_url)

# Create query for Patient resources.
query = fhir_store_url + "/Patient"

# Submit query.
response = fhir_server_get(query, credential_manager)

# Pretty print the response from the FHIR Store, hopefully containing patient resources.
print(json.dumps(json.loads(response.content), sort_keys=True, indent=4))