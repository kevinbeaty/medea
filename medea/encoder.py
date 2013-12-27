""" A custom :class:`JSONEncoder` using Medea :class:`MedeaMapper` """
from json import JSONEncoder
from singledispatch import singledispatch


@singledispatch
def medea(obj):
    """ generic function to transform object before JSON encoding """
    return obj


@medea.register(list)
@medea.register(tuple)
@medea.register(set)
def medea_list(obj):
    return [medea(item) for item in obj]


@medea.register(dict)
def medea_dict(obj):
    return dict((key, medea(obj[key])) for key in obj)


class MedeaEncoder(JSONEncoder):
    """ :class:`JSONEncoder` delegating to medea dispatched function """
    def default(self, obj):
        encoded = medea(obj)
        if encoded is obj:
            return JSONEncoder.default(self, obj)
        return encoded
