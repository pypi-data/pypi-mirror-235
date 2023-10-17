import boto3
import numpy as np
from hamal_utils.code.prefect_utils.access_manager import s3_access_data


src_bucket = 'hamal-red-feed-excaliber'
dest_bucket = 'hamal-data-pipelines-dev'
folder = "silver/unique-red/"

aws_access_key_id = ''
aws_secret_access_key = ''

max_items = 1000

# TODO: remove count argument and get bucket count from designated function
count = 10000000

region_name, access_key_id, secret_access_key = s3_access_data()
if access_key_id and secret_access_key:
    s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
else:
    s3 = boto3.client('s3')

def run_func(func, from_percent=0, to_percent=1):
    """
    Run a given function on objects from the bucket.
    given from_percent and to_percent both in range [0,1], the code will run the given function on the items in the bucket
    located between (total_count * from_percent) and (total_count * to_percent)
    :param func: The function to run. Must receive a single parameter which is the file (as presented in response['Contents'])
    :param from_percent: in range [0,1]. run on items from total_count * from_percent
    :param to_percent: in range [0,1]. run on items up to total_count * to_percent
    :return:
    """

    if from_percent > to_percent:
        raise Exception("from_percent must be smaller than to_percent")

    if from_percent > 1 or from_percent < 0 or to_percent > 1 or to_percent < 0:
        raise Exception("from_percent and to_percent must be in range [0,1]")

    try:
        counter = 0
        next_token = None

        from_counter = np.floor(from_percent * count).astype(int)
        to_counter = np.floor(to_percent * count).astype(int) - 1

        print(f"running from {from_counter} to {to_counter}")

        while True:
            if next_token:
                response = s3.list_objects_v2(Bucket=src_bucket, MaxKeys=max_items, ContinuationToken=next_token)
            else:
                response = s3.list_objects_v2(Bucket=src_bucket, MaxKeys=max_items)

            if 'Contents' in response:
                for file in response['Contents']:
                    if from_counter <= counter <= to_counter:
                        key = file["Key"]
                        print(f"Running on item {counter}: {key}")
                        func(file)
                    counter += 1

            if 'NextContinuationToken' in response:
                next_token = response['NextContinuationToken']
            else:
                break

            if counter > to_counter:
                break
    except Exception as err:
        raise Exception(
            f"Tech team's code hit an exception, This isn't your fault :)\nPlease contact Tech team\nerr: {err}")
