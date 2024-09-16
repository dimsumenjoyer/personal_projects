# 9/10/2024

#import numpy as np
from sympy import *

A = Matrix(
    [[1, -1, 1, 0],
    [0, 1, -8, 8],
    [0, 0, 1, 1]])

A = A.rref()[0]

pprint(A)