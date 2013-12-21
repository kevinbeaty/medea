from .encoder import medea
from .support import unwrap_object


class MedeaMapper(object):
    def __init__(self, *attrs, **json_attrs):
        self.attributes = set(attrs) | set(json_attrs)
        self.json_attrs = dict((attr, self.json_attr(attr)) for attr in attrs)
        self.json_attrs.update(json_attrs)

    def __call__(self, source):
        return self.to_json(source)

    def json_attr(self, attr):
        return attr

    def to_json(self, source):
        return self._map_json(source, None, True)

    def from_json(self, source, destination=None):
        return self._map_json(source, destination, False)

    def _map_json(self, source, destination, to_json):
        if destination is None:
            destination = {}
        source = unwrap_object(source)
        destination = unwrap_object(destination)

        attributes = self.attributes
        for attr in attributes:
            if self._hasattr(source, attr, to_json):
                value = self._getattr(source, attr, to_json)
                self._setattr(destination, attr, value, to_json)

        return destination

    def _hasattr(self, source, attr, to_json):
        if not to_json:
            attr = self.json_attrs.get(attr, attr)

        if isinstance(source, dict):
            return attr in source

        return hasattr(source, attr)

    def _getattr(self, source, attr, to_json):
        if not to_json:
            attr = self.json_attrs.get(attr, attr)

        if isinstance(source, dict):
            return source[attr]

        return getattr(source, attr)

    def _setattr(self, destination, attr, value, to_json):
        if to_json:
            attr = self.json_attrs.get(attr, attr)

        if isinstance(destination, dict):
            if to_json:
                value = medea(value)
            destination[attr] = value
        else:
            setattr(destination, attr, value)


class MedeaCamelMapper(MedeaMapper):
    def json_attr(self, attr):
        cs = []
        upper = False
        for c in attr:
            if c == '_':
                upper = True
            elif upper:
                cs.append(c.upper())
                upper = False
            else:
                cs.append(c)
        return ''.join(cs)
