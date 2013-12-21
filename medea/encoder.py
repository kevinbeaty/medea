""" A custom :class:`JSONEncoder` using Medea :class:`MedeaMapper` """
from .support import JSONEncoder, unwrap_object, singledispatch


@singledispatch
def medea(obj):
    """ generic function to transform object before JSON encoding """
    unwrapped = unwrap_object(obj)
    if unwrapped is obj:
        return obj
    return medea(unwrapped)


@medea.register(list)
@medea.register(tuple)
def medea_list(obj):
    return [medea(item) for item in obj]


class MedeaEncoder(JSONEncoder):
    """ :class:`JSONEncoder` delegating to medea dispatched function """
    def default(self, obj):
        encoded = medea(obj)
        if encoded is obj:
            return JSONEncoder.default(self, obj)
        return encoded
