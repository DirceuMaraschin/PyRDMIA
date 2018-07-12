# PyRDMIA Python Library 2018
# RDM-IA implementation by
# Dirceu Maraschin Jr
# Lucas Tortelli

'''
This file contains the main class responsible for creating 
the RDM type and all standard operations and complex operations 
defined following the original concepts of RDM arithmetic.
'''

import numpy as np
import sys

class Rdm(object):
    _lower = 0.0 
    _upper = 0.0 
    _alpha = 0.0 
    f = None

    def __init__(self,x,y=None):
        self._alpha = 0.01
        self._lower = np.float64(x)
        self._upper = np.float64(x) if y is None  else np.float64(y)
        self._f = lambda alpha: self._lower + alpha*(self._upper - self._lower) 

    def lower(self):
        return self._lower

    def upper(self):
        return self._upper

    def __checkValue(self,other):
        if(type(other) is not Rdm):
            other = Rdm(other)
        return other

    def __str__(self):
        return "["+str(self._lower)+" , "+str(self._upper)+"]"

    def __repr__(self):
        return "[%r, %r]" % (self._lower, self._upper)

    def __getitem__(self):
        return np.array([self._lower,self._upper])

    #Default operations since they are all or initially RDM numbers.
    def __add__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha_self) + other._f(alpha_other))
        
        return Rdm(min(values),max(values))

    def __sub__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha_self) - other._f(alpha_other))
        
        return Rdm(min(values),max(values))

    def __mul__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha_self) * other._f(alpha_other))
        
        return Rdm(min(values),max(values))

    def __div__(self,other):
        other = self.__checkValue(other)
        
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha_self) / other._f(alpha_other))
        
        return Rdm(min(values),max(values))

    #default operations given that possibly an initial number is not an RDM number
    def __rdiv__(self,other):
        other = self.__checkValue(other)
        
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha_other) / self._f(alpha_self))
        
        return Rdm(min(values),max(values))

    def __rsub__(self,other):
        other = self.__checkValue(other)
        
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha_other) - self._f(alpha_self))
        
        return Rdm(min(values),max(values))

    def __radd__(self,other):
        other = self.__checkValue(other)
        
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha_other) + self._f(alpha_self))
        
        return Rdm(min(values),max(values))

    def __rmul__(self,other):
        other = self.__checkValue(other)
        
        values = []
        rupper = 1+self._alpha
        for alpha_self in np.arange(0,rupper,self._alpha):
            for alpha_other in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha_other) * self._f(alpha_self))
        
        return Rdm(min(values),max(values))

    def __eq__(self,other):
        other = self.__checkValue(other)
        if((other.lower() == self.lower()) and (other.upper() == self.upper())):
            return True
        else:
            return False