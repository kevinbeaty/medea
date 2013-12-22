from .encoder import medea


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
        destination = {}
        for attr in self.attributes:
            if hasattr(source, attr):
                value = getattr(source, attr)
                dest_attr = self.json_attrs.get(attr, attr)
                destination[dest_attr] = medea(value)

        return destination

    def from_json(self, source, destination):
        attributes = self.attributes
        for attr in attributes:
            source_attr = self.json_attrs.get(attr, attr)
            if source_attr in source:
                value = source[source_attr]
                setattr(destination, attr, value)

        return destination

    def pick(self, source):
        destination = {}

        attributes = self.attributes
        for attr in attributes:
            source_attr = self.json_attrs.get(attr, attr)
            if source_attr in source:
                value = source[source_attr]
                destination[attr] = value
        return destination


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
