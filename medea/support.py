try:
    from flask.json import JSONEncoder
except:
    from json import JSONEncoder


try:
    from functools import singledispatch
except:
    from singledispatch import singledispatch

@singledispatch
def unwrap_object(obj):
    """ Unwraps any known proxy object """
    return obj

try:
    from werkzeug import LocalProxy
    @unwrap_object.register(LocalProxy)
    def unwrap_proxy(obj):
        return obj._get_current_object()
except:
    pass
