""" A custom :class:`JSONEncoder` using Medea :class:`MedeaMapper` """
from .support import JSONEncoder, unwrap_object


class MedeaEncoder(JSONEncoder):
    """ :class:`JSONEncoder` to handle :class:`MedeaEncoderMixin` classes """
    def default(self, obj):
        obj = unwrap_object(obj)
        if isinstance(obj, MedeaEncoderMixin):
            return obj.to_json()
        return JSONEncoder.default(self, obj)


class MedeaEncoderMixin(object):
    """ Mixin for objects that define a :func:`to_json` function using
    a :class:`MedeaMapper` defined as `__medea_mapper__` attribute in
    mixed in class """
    __medea_mapper__ = None

    def to_json(self):
        mapper = self.__medea_mapper__
        if mapper:
            return mapper.to_json(self)

        return {}
