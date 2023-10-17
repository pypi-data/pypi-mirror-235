import boto3

from hamal_utils.code.s3_utils.access_manager import s3_access_data

aws_access_key_id = ''
aws_secret_access_key = ''

# TODO: remove count argument and get bucket count from designated function
count = 10000000

region_name, access_key_id, secret_access_key = s3_access_data()
if access_key_id and secret_access_key:
    s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
else:
    s3 = boto3.client('s3')


def build_file_key(s3_prefix, file_key):
    if not s3_prefix:
        return file_key

    s3_prefix = s3_prefix.rstrip('/')
    return s3_prefix + '/' + file_key
