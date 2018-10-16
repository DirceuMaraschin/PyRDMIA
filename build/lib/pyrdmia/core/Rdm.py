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
from pyrdmia.support.error import IntervalError
from pyrdmia.support.error import TypeIntervalError
from pyrdmia.support.error import UndefinedValueIntervalError
from pyrdmia.support.error import IntervalDivisionByZero

class Rdm(object):
    _lower = 0.0 
    _upper = 0.0 
    _alpha = 0.0 
    f = None

    def __init__(self,x,y,precision=0.01):
        self._alpha = precision
        self._lower = np.float64(x)
        self._upper = np.float64(x) if y is None  else np.float64(y)
        #self.__isEmpty = True
        self._f = lambda alpha: self._lower + alpha*(self._upper - self._lower) 

    def lower(self):
        return self._lower

    def upper(self):
        return self._upper

    def __checkValue(self,other):
        if(type(other) is not Rdm):
            other = Rdm(other,None)
        return other

    #def isEmpty(self):
    #    return self.__isEmpty

    def __str__(self):
        return "["+str(self._lower)+", "+str(self._upper)+"]"

    def __repr__(self):
        return "[%r, %r]" % (self._lower, self._upper)

    def __getitem__(self):
        return np.array([self._lower,self._upper])


    def __iter__(self):
        raise TypeError

        
    #Default operations since they are all or initially RDM numbers.
    def __add__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        if(id(self) != id(other)):
            for alpha_self in np.arange(0,rupper,self._alpha):
                for alpha_other in np.arange(0,rupper,self._alpha):
                    values.append(self._f(alpha_self) + other._f(alpha_other))
        else:
            for alpha in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha) + other._f(alpha))
        return Rdm(min(values),max(values))

    def __sub__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        if(id(self) != id(other)):
            for alpha_self in np.arange(0,rupper,self._alpha):
                for alpha_other in np.arange(0,rupper,self._alpha):
                    values.append(self._f(alpha_self) - other._f(alpha_other))
        else:
            for alpha in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha) - other._f(alpha))
        return Rdm(min(values),max(values))

    def __mul__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        if(id(self) != id(other)):
            for alpha_self in np.arange(0,rupper,self._alpha):
                for alpha_other in np.arange(0,rupper,self._alpha):
                    values.append(self._f(alpha_self) * other._f(alpha_other))
        else:
            for alpha in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha) + other._f(alpha))
        return Rdm(min(values),max(values))

    def __div__(self,other):
        other = self.__checkValue(other)
        if(other.lower()*other.upper() <= 0): #division test by zero
            raise IntervalDivisionByZero()
        else:            
            values = []
            rupper = 1+self._alpha
            if(id(self) != id(other)):
                for alpha_self in np.arange(0,rupper,self._alpha):
                    for alpha_other in np.arange(0,rupper,self._alpha):
                        values.append(self._f(alpha_self) / other._f(alpha_other))
            else:
                for alpha in np.arange(0,rupper,self._alpha):
                    values.append(self._f(alpha) / other._f(alpha))
            return Rdm(min(values),max(values))

    #default operations given that possibly an initial number is not an RDM number
    def __rsub__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        if(id(self) != id(other)):
            for alpha_self in np.arange(0,rupper,self._alpha):
                for alpha_other in np.arange(0,rupper,self._alpha):
                    values.append(other._f(alpha_other) - self._f(alpha_self))
        else:
            for alpha in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha) - self._f(alpha))
        return Rdm(min(values),max(values))

    def __radd__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        if(id(self) != id(other)):
            for alpha_self in np.arange(0,rupper,self._alpha):
                for alpha_other in np.arange(0,rupper,self._alpha):
                    values.append(other._f(alpha_other) + self._f(alpha_self))
        else:
            for alpha in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha) + self._f(alpha))
        return Rdm(min(values),max(values))

    def __rmul__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        if(id(self) != id(other)):
            for alpha_self in np.arange(0,rupper,self._alpha):
                for alpha_other in np.arange(0,rupper,self._alpha):
                    values.append(other._f(alpha_other) * self._f(alpha_self))
        else:
            for alpha in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha) * self._f(alpha))
        return Rdm(min(values),max(values))

    def __rdiv__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        if(id(self) != id(other)):
            for alpha_self in np.arange(0,rupper,self._alpha):
                for alpha_other in np.arange(0,rupper,self._alpha):
                    values.append(other._f(alpha_other) / self._f(alpha_self))
        else:
            for alpha in np.arange(0,rupper,self._alpha):
                values.append(other._f(alpha) / self._f(alpha))
        return Rdm(min(values),max(values))

    #control
    '''
    def __checkValue(self,other):
        if(type(other) is not Rdm):
            other = Rdm(other)
        self.__validateDefinedValue(other)
        return other

    def __validateDefinedValue(self,other):
        if(other.isEmpty or self.isEmpty):
            raise UndefinedValueIntervalError("Invalid operation! The interval are empty.")
    '''
    
    #complementary and unary operations 
    def __pow__(self,other):
        other = self.__checkValue(other)
        values = []
        rupper = 1+self._alpha
        if(id(self) != id(other)):
            for alpha_self in np.arange(0,rupper,self._alpha):
                for alpha_other in np.arange(0,rupper,self._alpha):
                    values.append(self._f(alpha_self) ** other._f(alpha_other))
        else:
            for alpha in np.arange(0,rupper,self._alpha):
                values.append(self._f(alpha) ** other._f(alpha))
        return Rdm(min(values),max(values))

    def __or__(self, other):
        other = self.__checkValue(other)
        return Rdm(max(self.lower(),other.lower()),min(self.upper(),other.upper()))

    def __and__(self,other):
        other = self.__checkValue(other)
        return Rdm(min(self.lower(),other.lower()),max(self.upper(),other.upper()))

    def __invert__(self):
        return Rdm(self.upper(),self.lower())

    def __neg__(self):
        return Rdm(-self.upper(),-self.lower())

    def __eq__(self,other):
        other = self.__checkValue(other)
        if((other.lower() == self.lower()) and (other.upper() == self.upper())):
            return True
        else:
            return False

    def __contains__(self,other):
        if(type(other) is not Rdm):
            if(self.lower() <= other and self.upper() >= other):
                return True
            else:
                return False
        else:
            if((other.lower() >= self.lower()) and (self.upper() >= other.upper())):
                return True
            else:
                return False

    def __lt__(self,other):
        other = self.__checkValue(other)
        if((self.lower() < other.lower()) and (self.upper() < other.upper())):
            return True
        else:
            return False

    def __le__(self,other):
        other = self.__checkValue(other)
        if((self.lower() <= other.lower()) and (self.upper() <= other.upper())):
            return True
        else:
            return False

    def __gt__(self,other):
        other = self.__checkValue(other)
        if((self.lower() > other.lower()) and (self.upper() > other.upper())):
            return True
        else:
            return False

    def __ge__(self,other):
        other = self.__checkValue(other)
        if((self.lower() >= other.lower()) and (self.upper() >= other.upper())):
            return True
        else:
            return False

    __truediv__ = __div__
    __rtruediv__ = __rdiv__
    __ror__ = __or__
    __rand__ = __and__
    __rpow__ = __pow__