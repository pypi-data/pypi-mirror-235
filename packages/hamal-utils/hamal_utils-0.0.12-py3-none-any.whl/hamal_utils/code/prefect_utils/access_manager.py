import os

from prefect.blocks.system import Secret

DEFAULT_REGION_NAME = 'eu-west-1'


def get_local_env_variables():
    region_name = os.environ.get("region_name") or DEFAULT_REGION_NAME
    if not region_name:
        raise Exception("Environment variable \'region_name\' missing! Please add region name for s3 client!")
    access_key_id = os.environ.get("access_key")
    if not access_key_id:
        raise Exception("Environment variable \'access_key\' missing! Please add access key for s3 client!")
    secret_access_key = os.environ.get("secret_access_key")
    if not secret_access_key:
        raise Exception("Environment variable \'secret_access_key\' missing! Please add access key for s3 client!")
    return region_name, access_key_id, secret_access_key


def prefect_access_variables():
    try:
        return {Secret.load("aws-access-key").get(), Secret.load("aws-secret-key").get()}
    except:
        print("An exception occurred while accessing Prefect Secrets. validate login and credentials")
        raise Exception("En exception occurred while accessing Prefect Secrets. validate login and credential")


def s3_access_data():
    env_type = os.environ.get('iron_env')
    # prefect env doesn't have "iron_env"
    if env_type is None:
        region_name = DEFAULT_REGION_NAME
        return region_name, prefect_access_variables()
    elif env_type == 'local':
        return get_local_env_variables()
    elif env_type == 'staging':
        return
    else:
        raise Exception("Unknown environment.")
