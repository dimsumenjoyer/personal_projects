import numpy as np
import sympy as sp

def fuck_my_life(v, h, theta):
    d = (v**2 * np.sin(theta) * np.cos(theta) + v * np.cos(theta) * ((v * np.sin(theta))**2 + 64 * h)**(1/2))/32
    return d
    
a1 = fuck_my_life(44,6.25,np.radians(40))
a2 = fuck_my_life(44,6.25,np.radians(42.5))
a3 = fuck_my_life(44,6.25,np.radians(45))
a4 = fuck_my_life(44,6.25,np.degrees(40))
a5 = fuck_my_life(44,6.25,np.degrees(42.5))
a6 = fuck_my_life(44,6.25,np.degrees(45))
#print(a1)
#print(a2)
#print(a3)
#print("____________________________________")
#print(a4)
#print(a5)
#print(a6)
#print("____________________________________")

b1 = fuck_my_life(35,6.25,np.radians(42.5))
b2 = fuck_my_life(40,6.25,np.radians(42.5))
b3 = fuck_my_life(45,6.25,np.radians(42.5))
b4 = fuck_my_life(35,6.25,np.degrees(42.5))
b5 = fuck_my_life(40,6.25,np.degrees(42.5))
b6 = fuck_my_life(45,6.25,np.degrees(42.5))
#print(b1)
#print(b2)
#print(b3)
#print("____________________________________")
#print(b4)
#print(b5)
#print(b6)

A = sp.Matrix([
        [1, 7, 4, 3],
        [0, 1, 2, 3],
        [3, 2, 0, 3],
        [1, 3, 1, 3]
    ])

#print(A.rref())

def definite_integral():
    x = sp.symbols("x")
    f = ((1/4)*x**5 - x**-3)
    integral = sp.integrate(f,(x,1,2**(1/2)))
    return integral

print(definite_integral())