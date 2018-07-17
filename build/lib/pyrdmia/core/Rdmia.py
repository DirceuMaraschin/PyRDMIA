# PyRDMIA Python Library 2018
# RDM-IA implementation by
# Dirceu Maraschin Jr
# Lucas Tortelli

'''
This file is responsible for creating RDM numbers and setting the 
precision of operation in calculations using PyRDMIA.
'''

from pyrdmia.core.Rdm import *

class Rdmia(object):

    # Default precision
    _precision = 0.01

    @staticmethod
    def precision():
        return Rdmia._precision

    @staticmethod
    def setDotPrecision(val):
       Rdmia._precision = 10**(-val)

    @staticmethod
    def one():
        return Rdm(1.0,None,Rdmia._precision)
    
    @staticmethod
    def zero():
        return Rdm(0.0,None,Rdmia._precision)

    @staticmethod
    def number(x,y=None):
        if y is None:
            return Rdm(x,None,Rdmia._precision)
        else:
            return Rdm(x,y,Rdmia._precision)
