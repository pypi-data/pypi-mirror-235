from hamal_utils.code.s3_utils.download_loop import run_func


def process_s3_bucket_decorator(_func):
    def wrapper_process_s3_bucket_decorator(*args, **kwargs):
        run_func(*args, **kwargs)

    return wrapper_process_s3_bucket_decorator
