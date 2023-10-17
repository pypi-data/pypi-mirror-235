import os

MONITOR_TAG_TMPL = "hamalutils-{name}-{from_percent}-{to_percent}"

_EXTENSIONS_FROM_ENV = os.environ.get('EXTENSIONS')

EXTENSIONS = _EXTENSIONS_FROM_ENV.split(',') if _EXTENSIONS_FROM_ENV else None
