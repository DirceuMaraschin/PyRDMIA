from pyrdmia.core import Rdmia as rdmia
from pyrdmia.core import Rdm
from pyrdmia.utils import QualitativeMetrics as qm
import math

__all__ = ["RdmMath"]

class RdmMath(object):
    
    E = rdmia.number(math.e)
    PI = rdmia.number(math.pi)

    #convert degrees to radians
    @staticmethod
    def degToRad(value):
        #rad = (value/180)*RdmMath.PI
        print (qm)
        print (qm.centerI(rdmia.number(1)))
        rad = 0
        if (type(value) is Rdm):
            rad = math.radians(qm.centerI(value))
        else:
            rad = math.radians(value)
        
        if (type(rad) is Rdm):
            return rad
        else:
            return rdmia.number(rad)
    
    #definição da função seno por sin² + cos² = 1
    @staticmethod
    def sin(value):
        r = 0
        r = RdmMath.sqrt(1 - (RdmMath.cos(value))**2)
        return r

    @staticmethod
    def cos(rad):
        n = RdmMath.degToRad(rad)
        c = 0
        r = 1
        while(c<50):
            c += 1
            r += (((-1)**c)*(n**(2 * c)))/(math.factorial(2 * c))
        return r

    @staticmethod
    def exp(x):
        return RdmMath.E**x

    @staticmethod
    def sqrt(x):
        if(type(x) is Rdm):
            return x**(1.0/2.0)
        else:
            return rdmia.number(x**(1.0/2.0))

    @staticmethod
    def abs(x):
        return RdmMath.sqrt(x**2)

'''
    def acos(x, rnd=0):
        pass

    def acosh(x, rnd=0):
        pass

    def asin(x, rnd=0):
        pass

    def asinh(x, rnd=0):
        pass

    def atan(x, rnd=0):
        pass

    def atanh(x, rnd=0):
        pass

    def cos(x, rnd=0):
        pass

    def cosh(x, rnd=0):
        pass

    def cot(x, rnd=0):
        pass

    def csc(x, rnd=0):
        pass

    def exp(x, rnd=0):
        pass

    def log(x, rnd=0, base=2):
        pass

    def pow(x, y, rnd=0):
        pass

    def sec(x, rnd=0):
        pass

    def sinh(x, rnd=0):
        pass

    def sqrt(x, rnd=0):
        pass

    def tan(x, rnd=0):
        pass

    def tanh(x, rnd=0):
        pass
'''