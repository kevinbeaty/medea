""" A custom :class:`JSONEncoder` using Medea :class:`MedeaMapper` """
try:
    from flask.json import JSONEncoder
except:
    from json import JSONEncoder


try:
    from functools import singledispatch
except:
    from singledispatch import singledispatch


@singledispatch
def medea(obj):
    """ generic function to transform object before JSON encoding """
    return obj


@medea.register(list)
@medea.register(tuple)
def medea_list(obj):
    return [medea(item) for item in obj]

try:
    from werkzeug import LocalProxy

    @medea.register(LocalProxy)
    def unwrap_proxy(obj):
        return medea(obj._get_current_object())

except:
    pass


class MedeaEncoder(JSONEncoder):
    """ :class:`JSONEncoder` delegating to medea dispatched function """
    def default(self, obj):
        encoded = medea(obj)
        if encoded is obj:
            return JSONEncoder.default(self, obj)
        return encoded
