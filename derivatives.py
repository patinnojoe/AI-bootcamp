import sympy as sp

x = sp.Symbol("X")
f = x**2

deriavtive_func = f.diff(x)

print(deriavtive_func)