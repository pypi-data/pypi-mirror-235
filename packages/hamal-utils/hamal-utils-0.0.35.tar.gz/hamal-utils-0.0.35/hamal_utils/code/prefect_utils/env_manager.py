import os

from prefect.blocks.system import String

env_type = os.environ.get('IRON_ENV')


def get_env(name, default=None):
    if env_type is None:
        return String.load(name)

    return os.environ.get(name, default)
