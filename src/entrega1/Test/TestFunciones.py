'''
Created on 19 oct 2024

@author: rodri
'''
def producto(n:int, k:int) -> int:

    if k >= n:

        raise ValueError("k no puede ser mayor que n")

    res:int = 1

    for i in range(0, k):

        res *= (n - i + 1)

        

    return res

n = 4

k = 2

try:

    print("El producto de " + str(n) + " y " + str(k) + " es: " + str(producto(n, k)))

except (TypeError, ValueError) as e:

    print(f"Error: {e}")
    
def producto_secuencia_geometrica(a1, r, k) -> int:

    producto = 1

    for n in range(1, k + 1):

        an = a1 *(r ** (n - 1))

        producto *= an

    return producto

a1 = 3

r = 5

k = 2

try:

    print(f"El producto de la secuencia geométrica con a1 = '{a1}' r = '{r}' y k = '{k}' es: '{producto_secuencia_geometrica(a1, r, k)}'")

except (TypeError, ValueError) as e:

    print(f"Error: {e}")


import math
def combinatorio(n, k) -> int:

    if k > n:

        raise ValueError("k no puede ser mayor que n")

    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
n = 4
k = 2

try:

    print("El número combinatorio de " + str(n) + " y " + str(k) + " es: " + str(combinatorio(n, k)))

except (TypeError, ValueError) as e:

    print(f"Error: {e}")

def S(n, k) -> float:

    suma = 0

    for i in range(k):

        termino = (-1)**i * combinatorio(k + 1, i + 1) * (k- i)**n

        suma += termino

    resultado = suma / math.factorial(k)

    return resultado
n = 4
k = 2

try:

    print("El número S(n, k) siendo n = " + str(n) + " y  k = " + str(k) + " es: " + str(S(n, k)))

except (TypeError, ValueError) as e:

    print(f"Error: {e}")

def newton(f, f_der, x0, epsilon, max_iter=100) -> float:
    x = x0
    for n in range(max_iter):

        fx = f(x)

        if abs(fx) <= epsilon:

            print(f"Raíz encontrada:{x} después de {n+1} iteraciones")

            return x

        fpx = f_der(x)

        if fpx == 0:

            print("La derivada es 0. No se puede continuar")

            return float('inf')

        x = x - fx / fpx

    print("Se alcanzó el número máximo de iteraciones")

    return x

def f(x):

    return 2*x**2

def f_der(x):

    return 4*x
x0 = 3
epsilon = 1e-3
try:

    print("Resultado de la función 5 con a = " + str(x0) + " y  e = " + str(epsilon) + ", f(x) y f'(x) es: " + str(newton(f, f_der, x0, epsilon)))

except (TypeError, ValueError) as e:

    print(f"Error: {e}")



