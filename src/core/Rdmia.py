# Python
# Rdm-IA implementation
# Dirceu Maraschin
# Lucas Tortelli

from pyrdmia.core.Rdm import *

class Rdmia(object):

    # Default precision
    _precision = 0.01

    @property
    def precision(self):
        return type(self)._precision

    @staticmethod
    def setDotPrecision(val):
       _precision = 10**(-val)

    @staticmethod
    def one():
        return Rdm(1)
    
    @staticmethod
    def zero():
        return Rdm(0)

    @staticmethod
    def number(x,y=None):
        if y is None:
            return Rdm(x)
        else:
            return Rdm(x,y)

rdmia = Rdmia()
rdmia.zero()