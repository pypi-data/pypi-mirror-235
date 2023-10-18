from hamal_utils.code.prefect_utils.env_manager import get_env

MONITOR_TAG_TMPL = "hamalutils-{name}-{from_percent}-{to_percent}"

_EXTENSIONS_FROM_ENV = get_env('LIST_FILES_EXTENSIONS')

EXTENSIONS = _EXTENSIONS_FROM_ENV.split(',') if _EXTENSIONS_FROM_ENV else None
