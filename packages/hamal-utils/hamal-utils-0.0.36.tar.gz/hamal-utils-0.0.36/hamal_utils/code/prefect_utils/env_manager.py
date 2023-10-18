import os

from prefect.blocks.system import String

env_type = os.environ.get('IRON_ENV')


def get_env(name, default=None):
    if env_type is None:
        prefect_name = name.lower().replace('_', '-')
        return String.load(prefect_name)

    os_env_name = name.lower().replace('-', '_')
    return os.environ.get(os_env_name, default)
