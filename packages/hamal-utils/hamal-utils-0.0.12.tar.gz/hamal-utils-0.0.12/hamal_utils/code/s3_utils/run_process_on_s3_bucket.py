from hamal_utils.decorator.s3_utils.s3_list_files import process_s3_bucket_decorator


@process_s3_bucket_decorator
def run_process_on_s3_bucket(_func):
    pass
