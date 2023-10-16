import numpy as np
from numpy.polynomial.hermite import hermval, hermfit
from scipy.special import factorial, binom, erf
from functools import cached_property
from vector import Vector



class HermiteFunction(Vector):
    """A Hermite function series class."""
    
    @staticmethod
    def random(deg, normed=True):
        """Creates a, by default normed, Hermite function series
        of the given degree with normal distributed coefficients."""
        return HermiteFunction(Vector.random(deg+1, normed).coef)
    
    @staticmethod
    def fit(x, y, deg):
        """Creates a least squares Hermite function series fit
        with the given degree for the given x and y values."""
        #https://de.wikipedia.org/wiki/Multiple_lineare_Regression
        return HermiteFunction(c * np.sqrt(2**i*factorial(i)*np.sqrt(np.pi))
                for i, c in enumerate(hermfit(x, y/np.exp(-x**2/2), deg)))
    
    
    
    #function stuff
    @property
    def deg(self):
        """Degree of this series (index of the highest set coefficient)."""
        return len(self) - 1
    
    def __call__(self, x):
        return np.exp(-x**2/2) \
                * sum(c / np.sqrt(2**i * factorial(i) * np.sqrt(np.pi))
                * hermval(x, (0,)*i+(1,))
                for i, c in enumerate(self))
    
    def der(self, n=1):
        """Returns the n-th derivative of this series."""
        res = self
        for _ in range(n):
            res = (np.sqrt((i+1)/2) for i in range(len(res)-1)) * (res<<1) \
                    - (np.sqrt(i/2) for i in range(len(res)+1)) * (res>>1)
        return res
    
    def antider(self):
        """Returns F, r so that the antiderivative of this series is of form
        F(x) + r*HermiteFunction.zeroth_antiderivative(x)
        where F is also a Hermite series."""
        tmp = list(self)
        F = (len(self)-1) * [0]
        for i in reversed(range(1, len(self))):
            F[i-1] -= tmp[i] * np.sqrt(2/i)
            tmp[i-2] += tmp[i] * np.sqrt((i-1)/i)
        return HermiteFunction(F), tmp[0]
    
    @staticmethod
    def zeroth_antiderivative(x):
        """Evaluation of the antiderivative of the zeroth Hermite function."""
        return np.sqrt(np.sqrt(np.pi)/2) * (erf(x/np.sqrt(2)) + 1)
    
    def fourier(self):
        """Returns the Fourier transform (unitary, in angular frequency)
        of this series."""
        return HermiteFunction((-1j)**n * c for n, c in enumerate(self))
    
    @cached_property
    def kin(self):
        """The kinetic energy of this series."""
        #return -1/2 * self.dot(self.der(2))
        return abs(self.der())**2 / 2
    
    
    
    
    
    #def sympify(self, x=smp.Symbol('x')):
    #    r = 0
    #    for n, c in enumerate(self):
    #        r += c * smp.exp(-x**2/2)/smp.sqrt(2**n * smp.factorial(n)*smp.sqrt(smp.pi)) * smp.functions.special.polynomials.hermite(n, x)
    #    return r
    
    
    
    #python stuff
    def __str__(self):
        s = f'{self[0]:.1f} h_0'
        for i, c in enumerate(self[1:]):
            s += f' + {c:.1f} h_{i+1}'
        return s
