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
    return map(medea, obj)


def register_mapper(dispatch_type, mapper):
    medea.register(dispatch_type, lambda obj: mapper.to_json(obj))


class MedeaEncoder(JSONEncoder):
    """ :class:`JSONEncoder` delegating to medea dispatched function """
    def default(self, obj):
        return medea(obj)
