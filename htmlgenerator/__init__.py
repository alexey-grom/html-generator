# encoding: utf-8

import sys

from htmlgenerator.node import Node


class Wrapper(object):
    def __init__(self, module):
        self.module = module

    def __getattr__(self, item):
        try:
            return getattr(self.module, item)
        except AttributeError:
            return Node(item)


sys.modules[__name__] = Wrapper(sys.modules[__name__])
