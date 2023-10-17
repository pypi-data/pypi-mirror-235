from hamal_utils.code.s3_utils.upload import run_process_on_s3_file


def process_s3_bucket_decorator(_func):
    def wrapper_process_s3_bucket_decorator(*args, **kwargs):
        run_process_on_s3_file(*args, **kwargs)

    return wrapper_process_s3_bucket_decorator
