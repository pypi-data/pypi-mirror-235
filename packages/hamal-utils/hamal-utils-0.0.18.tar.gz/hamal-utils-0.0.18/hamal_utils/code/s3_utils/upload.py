from hamal_utils.code.s3_utils.common import s3_prefix, s3


def upload_file_to_s3(bucket, file_key, body, flatten=True):
    key = file_key if not flatten else file_key.replace('/', '_')
    s3.put_object(
        Body=body,
        Bucket=bucket,
        Key=s3_prefix + key)
