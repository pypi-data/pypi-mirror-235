from hamal_utils.code.s3_utils.common import s3, build_file_key


def upload_object_to_s3(bucket, s3_prefix, file_key, body, flatten=True):
    file_key = file_key if not flatten else file_key.replace('/', '_')
    file_key = build_file_key(s3_prefix, file_key)
    s3.put_object(
        Body=body,
        Bucket=bucket,
        Key=file_key)
