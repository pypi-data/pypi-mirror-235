import logging
import sys

import numpy as np

from hamal_utils.code.common import MONITOR_TAG_TMPL, EXTENSIONS
from hamal_utils.code.s3_utils.session import aws_session
from hamal_utils.code.utils.hash_util import hash_string


class CustomS3Client:
    def __init__(self):
        self._base_s3_client = aws_session.client('s3')

    def __getattr__(self, attr):
        if hasattr(self._base_s3_client, attr):
            return getattr(self._base_s3_client, attr)

        return super().__getattribute__(attr)

    def _get_log_tag(self, from_percent, to_percent):
        return MONITOR_TAG_TMPL.format(name=hash_string(sys.argv[0]), from_percent=from_percent, to_percent=to_percent)

    def _has_complete_tag(self, bucket, key, from_percent, to_percent):
        tags_response = self.get_object_tagging(bucket, key)

        if 'TagSet' not in tags_response:
            return False

        object_tags = tags_response['TagSet']
        log_tag_key = self._get_log_tag(from_percent, to_percent)

        for tag in object_tags:
            if log_tag_key == tag['Key']:
                return True

        return False

    def _tag_file_as_complete(self, bucket, key, from_percent, to_percent):
        log_tag_key = self._get_log_tag(from_percent, to_percent)
        tagging = {'TagSet': [{'Key': log_tag_key, 'Value': 'complete'}]}
        self.put_object_tagging(Bucket=bucket, Key=key, Tagging=tagging)

    def _validate_extensions(self, key):
        return not EXTENSIONS or any(key.lower().endswith(ext.lower()) for ext in EXTENSIONS)

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

        has_counter = from_percent != 0 or to_percent != 1
        counter = 0
        count = self.get_bucket_count(bucket, prefix) if has_counter else -1
        from_counter = np.floor(from_percent * count).astype(int)
        to_counter = np.floor(to_percent * count).astype(int) - 1

        logging.debug(f"running from {from_counter} to {to_counter}")

        for file in self._list_objects_v2_generator(
                bucket, delimiter, encoding_type, max_keys, prefix, fetch_owner, start_after, request_payer,
                expected_bucket_owner, optional_object_attributes):

            if has_counter and (counter < from_counter or counter > to_counter):
                break

            counter += 1

            key = file["Key"]

            if self._validate_extensions(key):
                continue

            if not ignore_log_tag and self._has_complete_tag(bucket, key, from_percent, to_percent):
                continue

            logging.debug(f"Running on item {counter}: {key}")
            yield file

            if enable_log_tag:
                self._tag_file_as_complete(bucket, key, from_percent, to_percent)

    def _list_objects_v2_generator(
            self, bucket,
            delimiter=None,
            encoding_type=None,
            max_keys=None,
            prefix=None,
            fetch_owner=None,
            start_after=None,
            request_payer=None,
            expected_bucket_owner=None,
            optional_object_attributes=None):

        args = {
            'Bucket': bucket,
            'Delimiter': delimiter,
            'EncodingType': encoding_type,
            'MaxKeys': max_keys,
            'Prefix': prefix,
            'FetchOwner': fetch_owner,
            'StartAfter': start_after,
            'RequestPayer': request_payer,
            'ExpectedBucketOwner': expected_bucket_owner,
            'OptionalObjectAttributes': optional_object_attributes
        }

        s3_args = {key: value for key, value in args.items() if value}

        while True:
            response = self.list_objects_v2(**s3_args)

            if 'Contents' not in response:
                break

            for file in response['Contents']:
                yield file

            if 'NextContinuationToken' not in response:
                break

            args['ContinuationToken'] = response['NextContinuationToken']

    def get_bucket_count(self, bucket, prefix=None):
        return len([_ for _ in self._list_objects_v2_generator(bucket, prefix=prefix)])
