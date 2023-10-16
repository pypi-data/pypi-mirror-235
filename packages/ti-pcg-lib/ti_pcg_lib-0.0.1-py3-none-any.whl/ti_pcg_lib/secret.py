from google.cloud import secretmanager
def access_secret_version(project_id, secret_id, version_id):
    """Function used to retrieve secrets from a GCP project 

    Args:
        project_id (str): if of the GCP project
        secret_id (str): id of the secret to retrieve
        version_id (str): number version of the secret

    Returns:
        str: secret value
    """
    secret_client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{ project_id }/secrets/{ secret_id }/versions/{ version_id }"

    response = secret_client.access_secret_version(request={"name": name})
    return format(response.payload.data.decode("UTF-8"))
