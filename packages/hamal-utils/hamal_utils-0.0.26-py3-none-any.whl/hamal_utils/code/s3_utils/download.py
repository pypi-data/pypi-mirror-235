import botocore

from hamal_utils.code.s3_utils.common import s3


def get_file_from_s3(src_bucket, s3_prefix, file_key):
    try:
        # Download the image from S3
        s3_prefix = s3_prefix.rstrip('/')
        obj = s3.get_object(Bucket=src_bucket, Key=s3_prefix + '/' + file_key)
        return obj['Body'].read()

    except botocore.exceptions.NoCredentialsError:
        print("No AWS credentials found. Please check your credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")
