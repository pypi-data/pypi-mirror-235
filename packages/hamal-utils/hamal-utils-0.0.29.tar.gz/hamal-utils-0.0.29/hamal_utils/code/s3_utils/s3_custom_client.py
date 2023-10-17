import logging

import boto3
import numpy as np

from hamal_utils.code.common import count, MONITOR_TAG_TMPL
from hamal_utils.code.prefect_utils.access_manager import s3_access_data
from hamal_utils.code.s3_utils.s3_args import _get_s3_function_args


class CustomS3Client:
    def __init__(self):
        region_name, access_key_id, secret_access_key = s3_access_data()
        if access_key_id and secret_access_key:
            self._base_s3_client = boto3.client('s3', aws_access_key_id=access_key_id,
                                                aws_secret_access_key=secret_access_key)
        else:
            self._base_s3_client = boto3.client('s3')

    def __getattr__(self, attr):
        if hasattr(self._base_s3_client, attr):
            return getattr(self._base_s3_client, attr)

        return super().__getattribute__(attr)

    def is_file_processed(self, bucket, key, from_percent, to__percent):
        tags_response = self.get_object_tagging(bucket, key)

        if 'TagSet' not in tags_response:
            return False

        object_tags = tags_response['TagSet']
        log_tag_key = MONITOR_TAG_TMPL.format(name="", from_percent=from_percent, to_percent=to__percent)

        for tag in object_tags:
            if log_tag_key == tag['Key']:
                return True

        return False

    def tag_file_as_complete(self, bucket, key, from_percent, to__percent):
        log_tag_key = MONITOR_TAG_TMPL.format(name="", from_percent=from_percent, to_percent=to__percent)
        tagging = {'TagSet': [{'Key': log_tag_key, 'Value': 'complete'}]}
        self.put_object_tagging(Bucket=bucket, Key=key, Tagging=tagging)

    def list_objects_v2_generator(
            self,
            bucket,
            delimiter=None,
            encoding_type=None,
            max_keys=None,
            prefix=None,
            fetch_owner=None,
            start_after=None,
            request_payer=None,
            expected_bucket_owner=None,
            optional_object_attributes=None,
            from_percent=0,
            to_percent=1,
            enable_log_tag=True,
            ignore_log_tag=True):
        """
        Run a given function on objects from the bucket.
        given from_percent and to_percent both in range [0,1], the code will run the given function on the items in the bucket
        located between (total_count * from_percent) and (total_count * to_percent)
        :param from_percent: in range [0,1]. run on items from total_count * from_percent
        :param to_percent: in range [0,1]. run on items up to total_count * to_percent
        :return:
        """

        if from_percent > to_percent:
            raise Exception("from_percent must be smaller than to_percent")

        if from_percent > 1 or from_percent < 0 or to_percent > 1 or to_percent < 0:
            raise Exception("from_percent and to_percent must be in range [0,1]")

        counter = 0
        continuation_token = None
        from_counter = np.floor(from_percent * count).astype(int)
        to_counter = np.floor(to_percent * count).astype(int) - 1

        logging.debug(f"running from {from_counter} to {to_counter}")

        while True:
            args = _get_s3_function_args(
                CustomS3Client.list_objects_v2_generator, bucket, delimiter, encoding_type, max_keys, prefix,
                continuation_token, fetch_owner, start_after, request_payer, expected_bucket_owner,
                optional_object_attributes, continuation_token)

            response = self.list_objects_v2(**args)

            if 'Contents' not in response:
                continue

            for file in response['Contents']:
                if from_counter <= counter <= to_counter:
                    key = file["Key"]

                    if not ignore_log_tag and self.is_file_processed(bucket, key, from_percent, to_percent):
                        continue

                    logging.debug(f"Running on item {counter}: {key}")
                    yield file

                    if enable_log_tag:
                        self.tag_file_as_complete(bucket, key, from_percent, to_percent)

                counter += 1

            if 'NextContinuationToken' in response:
                continuation_token = response['NextContinuationToken']
            else:
                break

            if counter > to_counter:
                break
