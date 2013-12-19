try:
    from flask.json import JSONEncoder
except:
    from json import JSONEncoder

try:
    from werkzeug import LocalProxy
except:
    LocalProxy = ()


def unwrap_object(obj):
    """ Unwraps any known proxy object """
    if isinstance(obj, LocalProxy):
        obj = obj._get_current_object()
    return obj
