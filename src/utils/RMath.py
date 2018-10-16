
from pyrdmia.core import Rdmia as rdmia
from pyrdmia.core import Rdm
from .QualitativeMetrics import QualitativeMetrics as qm


import math

__all__ = ["RMath"]

class RMath(object):

    #convert degrees to radians
    @staticmethod
    def degToRad(value):
        #rad = (value/180)*math.pi
        rad = 0
        if (type(value) is Rdm):
            rad = math.radians(qm.midpoint(value))
        else:
            rad = math.radians(value)
        
        if (type(rad) is Rdm):
            return rad
        else:
            return rdmia.number(rad)
    
    #sine function by sin² + cos² = 1
    @staticmethod
    def sin(value):
        r = 0
        r = RMath.sqrt(1 - (RMath.cos(value))**2)
        return r

    #cosine
    @staticmethod
    def cos(value):
        n = RMath.degToRad(value)
        c = 0
        r = 1
        while(c<50):
            c += 1
            r += (((-1)**c)*(n**(2 * c)))/(math.factorial(2 * c))
        return r

    #tangent
    @staticmethod
    def tan(value):
        return RMath.sin(value)/RMath.cos(value)

    #exponential
    @staticmethod
    def exp(x):
        return math.e**x

    #square root
    @staticmethod
    def sqrt(x):
        if(type(x) is Rdm):
            return x**(1.0/2.0)
        else:
            return rdmia.number(x**(1.0/2.0))

    #absolute value 
    @staticmethod
    def abs(x):
        return RMath.sqrt(x**2)

    #secant
    @staticmethod
    def sec(value):
        return 1/RMath.cos(value)

    #cosecant
    @staticmethod
    def csc(value):
        return 1/RMath.sin(value)

    #cotangent
    @staticmethod
    def cot(value):
        return RMath.cos(value)/RMath.sin(value)

    #hyperbolic sine xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    @staticmethod
    def sinh(value):
        return (RMath.exp(value)/2.0)-(RMath.exp(-(value))/2.0)

    #hyperbolic cosine xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    @staticmethod
    def cosh(value):
        return (RMath.exp(-(value))/2.0)+(RMath.exp(value)/2.0)

    #hyperbolic tangent xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    @staticmethod
    def tanh(value):
        return RMath.sinh(value)/RMath.cosh(value)
        
    #hyperbolic secant xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    @staticmethod
    def sech(value):
        return 1.0/RMath.cosh(value)

    #hyperbolic cosecant xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    @staticmethod
    def csch(value):
        return 1.0/RMath.sinh(value)

    #hyperbolic cotangent xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    @staticmethod
    def coth(value):
        return RMath.cosh(value)/RMath.sinh(value)
    
    #natural logarithm
    @staticmethod
    def ln(x):
        n=1000.0
        return  n*((x**(1/n))-1)


'''
    #inverse sine
    def asin(x, rnd=0):
        pass

    #inverse hyperbolic sine
    def asinh(x, rnd=0):
        pass 

    #inverse cosine
    def acos(x, rnd=0):
        pass

    #inverse hyperbolic cosine
    def acosh(x, rnd=0):
        pass

    #inverse tangent
    def atan(x, rnd=0):
        pass

    #inverse hyperbolic tangent
    def atanh(x, rnd=0):
        pass

    def log(x, rnd=0, base=2):
        pass


'''