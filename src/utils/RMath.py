from ..core import Rdmia as rdmia
from ..core import Rdm
from .QualitativeMetrics import QualitativeMetrics as qm
import math


class RMath(object):

    def __init__(self):
        self.E = rdmia.number(math.e)
        self.PI = rdmia.number(math.pi)

    #convert degrees to radians
    @staticmethod
    def degToRad(value):
        #rad = (value/180)*math.pi
        rad = 0.0
        if (type(value) is Rdm.Rdm):
            rad = math.radians(qm.midpoint(value))
        else:
            rad = math.radians(value)
        
        return rad

    #factorial
    @staticmethod
    def factorial(value):
        '''
        f = lambda t : t**(value-1.0)*math.e**(-t)
        return RMath.iSimpson(f,5000.0,0.0,99999999999.0)
        '''
        return rdmia.number(math.factorial(value))
        
    #natural logarithm
    @staticmethod
    def log(value):
        return rdmia.number(math.log(value))

    #exponential
    @staticmethod
    def exp(value):
        return rdmia.number(self.E**value)

    #square root
    @staticmethod
    def sqrt(value):
        if(type(value) is Rdm.Rdm):
            return value**(1.0/2.0)
        else:
            return rdmia.number(value**(1.0/2.0))

    #absolute value 
    @staticmethod
    def abs(value):
        return RMath.sqrt(value**2.0)

    
    #sine function by sin² + cos² = 1
    @staticmethod
    def sin(value):
        return rdmia.number(math.sin(RMath.degToRad(value)))
        '''
        r = 0.0
        r = RMath.sqrt(1.0 - (RMath.cos(value))**2.0)
        '''
        '''
        for k in range(0,10,1):
            r=((-1)**k)*(value**(1+2*k))/(math.factorial(1+2*k))
        '''

    #cosine
    @staticmethod
    def cos(value):
        return rdmia.number(math.cos(RMath.degToRad(value)))
        '''
        n = RMath.degToRad(value)
        r = 1.0
        for c in range(500):
            r += (((-1.0)**c)*(n**(2.0 * c)))/(math.factorial(2.0 * c))
        return r
        '''

    #tangent
    @staticmethod
    def tan(value):
        return RMath.sin(value)/RMath.cos(value)

    #secant
    @staticmethod
    def sec(value):
        return 1.0/RMath.cos(value)

    #cosecant
    @staticmethod
    def csc(value):
        return 1.0/RMath.sin(value)

    #cotangent
    @staticmethod
    def cot(value):
        return RMath.cos(value)/RMath.sin(value)

    #hyperbolic sine
    @staticmethod
    def sinh(value):
        return rdmia.number(math.sinh(RMath.degToRad(value)))
        #return (RMath.exp(value)/2.0)-(RMath.exp(-(value))/2.0)

    #hyperbolic cosine
    @staticmethod
    def cosh(value):
        return rdmia.number(math.cosh(RMath.degToRad(value)))
        #return (RMath.exp(-(value))/2.0)+(RMath.exp(value)/2.0)

    #hyperbolic tangent
    @staticmethod
    def tanh(value):
        return rdmia.number(math.tanh(RMath.degToRad(value)))
        #return RMath.sinh(value)/RMath.cosh(value)
        
    #hyperbolic secant
    @staticmethod
    def sech(value):
        return 1.0/RMath.cosh(value)

    #hyperbolic cosecant
    @staticmethod
    def csch(value):
        return 1.0/RMath.sinh(value)

    #hyperbolic cotangent
    @staticmethod
    def coth(value):
        return RMath.cosh(value)/RMath.sinh(value)
    
    #inverse sine
    @staticmethod
    def asin(value):
        return rdmia.number(math.asin(RMath.degToRad(value)))

    #inverse cosine
    @staticmethod
    def acos(value):
        return rdmia.number(math.acos(RMath.degToRad(value)))

    #inverse tangent
    @staticmethod
    def atan(value):
        return rdmia.number(math.atan(RMath.degToRad(value)))

    #inverse hyperbolic sine
    @staticmethod
    def asinh(value):
        return rdmia.number(math.asinh(RMath.degToRad(value)))

    #inverse hyperbolic cosine
    @staticmethod
    def acosh(value):
        return rdmia.number(math.acosh(RMath.degToRad(value)))

    #inverse hyperbolic tangent
    @staticmethod
    def atanh(value):
        return rdmia.number(math.atanh(RMath.degToRad(value)))