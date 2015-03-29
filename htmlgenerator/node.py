# encoding: utf-8


class Node(list):
    def __init__(self, name, *children, **attrs):
        super(Node, self).__init__(*children)
        self.name = name
        self.attrs = attrs.copy()

    def __repr__(self):
        from htmlgenerator.serializer import DefaultSerializer
        return DefaultSerializer().render(self)

    __str__ = __repr__
    __unicode__ = __repr__

    def __gt__(self, other):
        self.append(other)
        return other

    def __call__(self, *args, **kwargs):
        self.attrs.update(kwargs)
        self.extend(args)
        return self
