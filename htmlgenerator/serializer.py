# encoding: utf-8

from __future__ import unicode_literals
import types

from six import iteritems

from htmlgenerator.node import Node


__all__ = ('NodeSerializer',
           'HTMLSerializer',
           'LazySerializer',
           'DefaultSerializer', )


class NodeSerializer(object):
    NODE_FORMAT = '<{name}{attrs}>{nested}</{name}>'

    def render(self, *nodes):
        return ''.join(map(self.render_node,
                           nodes))

    def render_attributes(self, node):
        result = map(lambda (key, value): '{}="{}"'.format(key, value),
                     iteritems(node.attrs))
        result = ' '.join(result)
        if not result:
            return ''
        return ' ' + result

    def render_nested(self, node):
        result = (self.render_node(child)
                  for child in node)
        return ''.join(result)

    def render_node(self, node):
        if not isinstance(node, Node):
            return unicode(node)
        attrs = self.render_attributes(node)
        nested = self.render_nested(node)
        return self.NODE_FORMAT.format(name=node.name,
                                       attrs=attrs,
                                       nested=nested)


def flatten(sequence):
    iterators = [iter(sequence), ]
    while iterators:
        for item in iterators[-1]:
            if isinstance(item, types.GeneratorType):
                iterators.append(iter(item))
                break
            else:
                yield item
        else:
            iterators.pop()


class LazySerializer(NodeSerializer):
    NODE_START_FORMAT = '<{name}{attrs}>'
    NODE_END_FORMAT = '</{name}>'

    def render(self, *nodes):
        return (part
                for node in nodes
                for part in self.render_node(node))

    def render_nested(self, node):
        return (part
                for child in node
                for part in self.render_node(child))

    def render_node(self, node):
        if not isinstance(node, Node):
            for value in self.render_value(node):
                yield value

        else:
            attrs = self.render_attributes(node)
            yield self.NODE_START_FORMAT.format(name=node.name,
                                                attrs=attrs)
            for child in self.render_nested(node):
                yield child
            yield self.NODE_END_FORMAT.format(name=node.name)

    def render_value(self, value):
        if isinstance(value, types.GeneratorType):
            return (item
                    for part in value
                    for item in self.render_node(part))
        return (unicode(value), )


DefaultSerializer = NodeSerializer
