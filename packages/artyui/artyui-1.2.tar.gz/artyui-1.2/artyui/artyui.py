import math
import numpy as np

# Logarithms

def log(x):
    return math.log(x)

def log2(x):
    return math.log(x, 2)

def log3(x):
    return math.log(x, 3)

def log4(x):
    return math.log(x, 4)

def log5(x):
    return math.log(x, 5)

def log10(x):
    return math.log10(x)

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
    return 3.14159256

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
    return np.floor(x)

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

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
    
def BiCo(x, y):
    return factorial(x) // (factorial(y) * factorial(x-y))

def AbValue(x):
    if x < 0:
        return -x
    else:
        return x
    
def median(a):
    sorted_a = sorted(a)
    n = len(sorted_a)
    if a % 2 == 0:
        return (sorted_a[n//2-1] + sorted_a[n//2])
    else:
        return sorted_a[n//2]
    
def geop(a, r, n):
    prog = [a * (r ** i) for i in range(n)]
    return prog

# System convertation

def bin_to_oct(binary):
    decimal = 0
    power = 0

    while binary != 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1

    octal = ""
    while decimal != 0:
        octal = str(decimal % 8) + octal
        decimal //= 8

    return octal

def bin_to_dec(binary):
    decimal = 0
    power = 0

    while binary != 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1

def bin_to_hex(binary):
    decimal = int(binary, 2)
    hex_num = hex(decimal)[2:]
    return hex_num.upper()

def oct_to_bin(octal):
    decimal = int(octal, 8)
    binary = bin(decimal)[2:] 
    return binary

def oct_to_dec(octal):
    decimal = int(octal, 8)
    return decimal

def oct_to_hex(octal):
    decimal = int(octal, 8)
    hex = hex(decimal)[2:]
    return hex.upper()

def dec_to_bin(decimal):
    bin = bin(decimal)[2:]
    return bin

def dec_to_oct(decimal):
    oct = oct(decimal)[2:]
    return oct

def dec_to_hex(decimal):
    hex = hex(decimal)[2:]
    return hex.upper()

def hex_to_binary(hexadecimal):
    binary = bin(int(hexadecimal, 16))[2:]
    return binary


def hex_to_octal(hexadecimal):
    octal = oct(int(hexadecimal, 16))[2:]
    return octal


def hex_to_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal
