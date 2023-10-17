import math
import numpy as np

# Logarithms

def log2(x):
    if x <= 0:
        return None
    return math.log(x, 2)

def log3(x):
    if x <= 0:
        return None
    return math.log(x, 3)

def log4(x):
    if x <= 0:
        return None
    return math.log(x, 4)

def log5(x):
    if x <= 0:
        return None
    return math.log(x, 5)

# Trigonometric functions
  # Radians

def cosr(x):
    return math.cos(x)

def sinr(x):
    return math.sin(x)

def tanr(x):
    return math.tan(x)

def arscosr(x):
    return math.acos(x)

def arssinr(x):
    return math.asin(x)

def arstanr(x):
    return math.atan(x)

def sinecr(x):
    return 1 / np.sin(x)

def cosecr(x):
    return 1 / np.cos(x)

def tanecr(x):
    return 1 / np.tan(x)

  # Degrees

def cosc(x):
    return math.degrees(math.cos(x))

def sinc(x):
    return math.degrees(math.sin(x))

def tanc(x):
    return math.degrees(math.tan(x))

def arscosc(x):
    return math.degrees(math.acos(x))

def arssinc(x):
    return math.degrees(math.asin(x))

def arstanc(x):
    return math.degrees(math.atan(x))

def sinecc(x):
    return math.degrees(1 / np.sin(x))

def cosecc(x):
    return math.degrees(1 / np.cos(x))

def tanecc(x):
    return math.degrees(1 / np.tan(x))

# Exponential functions

  # Exponential functions

def exp(x):
    return np.exp(x)

def exp2(x):
    return np.exp2(x)

  # Hyperbolic functions

def sinh(x):
    return np.sinh(x)

def cosh(x):
    return np.cosh(x)

def tanh(x):
    return np.tanh(x)

# NaN

def NaN(x):
    return np.isnan(x)

# Constants

def pi():
    return math.pi

def e():
    return math.e

def tau():
    return math.tau

def phi():
    return 1.618033988749895

def C():
    return 0.577215664901532

# Rounding

def ceil(x):
    return np.ceil(x)

def round(x):
    return round(x)

def floor(x):
    return math.floor(x)

# Working with numbers

def sqrt(x):
    return math.sqrt(x)

def power(x, y):
    return x ** y

def frac(x):
    return x % 1

def intpart(x):
    return np.trunc(x)

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x