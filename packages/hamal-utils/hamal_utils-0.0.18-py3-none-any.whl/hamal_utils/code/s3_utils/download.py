import botocore

from hamal_utils.code.s3_utils.common import s3, src_bucket


def get_file_from_s3(file_key):
    try:
        # Download the image from S3
        obj = s3.get_object(Bucket=src_bucket, Key=file_key)
        return obj['Body'].read()

    except botocore.exceptions.NoCredentialsError:
        print("No AWS credentials found. Please check your credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")
