import numpy as np
from numpy import log as ln
import sympy as sp
from sympy import Matrix

def f(n):
    return (8*n) / (((2*n - 1)**2) * ((2*n + 1)**2))

def summation0():
    ns = np.linspace(1,500000,500000)
    ys = []
    for i in range(len(ns)):
        y = f(ns[i])
        ys.append(y)
    sum = np.sum(ys)
    print(sum)
    return

def summation(higher_order_function, lower_bound, upper_bound):
    y = 0
    for i in range(lower_bound, upper_bound):
        y += higher_order_function(i)
    return y

def rowReduce():
    m = Matrix(
        [[1, 1, 0, 2],
        [4, 2, 1, 7],
        [4, 0, 0, 4]])
    row_reduce = m.rref()
    print(row_reduce)
    return

def fibonacciSequence(n):
    if n < 0:
        print("Error: Invalid Input\n")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacciSequence(n - 1) + fibonacciSequence(n - 2)

def testConvergenceOrDivergence():
    return

#summation0()
#print(summation(f, 1, 500000))

print(summation(lambda n: (8*n) / (((2*n - 1)**2) * ((2*n + 1)**2)), 1, 500000))
print(summation(lambda n: 3 / (1 + np.log(n)), 1, 500000))
print(summation(lambda n: (n + 1) / ((8*n) * (n**2 + 6*n)), 1, 500000))
#print(summation(lambda n: ((9*n - 8) / (n**2 - 2*n)), 1, 500000)) # diverges
print(summation(lambda n: 3 / (n**2 + n**3), 1, 5000000))
print(summation(lambda n: 9**n/n**9, 1, 50))