import numpy as np

from hamal_utils.code.s3_utils.common import count, s3


def list_file_from_bucket(src_bucket, s3_prefix='', from_percent=0, to_percent=1):
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

        s3_prefix = s3_prefix.rstrip('/')
        while True:
            if next_token:
                response = s3.list_objects_v2(Bucket=src_bucket, Prefix=s3_prefix, ContinuationToken=next_token)
            else:
                response = s3.list_objects_v2(Bucket=src_bucket, Prefix=s3_prefix)

            if 'Contents' in response:
                for file in response['Contents']:
                    if from_counter <= counter <= to_counter:
                        key = file["Key"]
                        print(f"Running on item {counter}: {key}")
                        yield file
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
