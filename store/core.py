import re

_adapters = {}
def register_adapter(adapter, prefix):
    global _adapters
    _adapters[prefix] = adapter

def create(path, **kwargs):
    try:
        prefix, fs_path = re.split("://", path, maxsplit=1)
        adaptor = _adapters[prefix](fs_path, **kwargs)
        return adaptor
    except ValueError:
        raise TypeError('Invalid path')
    except KeyError:
        raise KeyError('No adapter for prefix {}'.format(prefix))
