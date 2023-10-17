import inspect


def _get_s3_function_args(func, *args):
    args_spec = inspect.getfullargspec(func)
    s3_function_args = {}

    for i in range(len(args_spec.args)):
        if i >= len(args):
            break

        value = args[i]
        if not value:
            continue
        name = args_spec.args[i + 1]  # index + 1 to ignore 'self' arg
        camel_case_name = name.title().replace("_", "")
        s3_function_args[camel_case_name] = value
    return s3_function_args
