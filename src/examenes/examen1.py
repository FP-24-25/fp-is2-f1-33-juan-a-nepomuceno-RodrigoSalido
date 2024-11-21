'''
Created on 24 oct 2024

@author: rodri
'''
def P2(n:int, k:int, i:int = 1) -> int:
    if k > n:

        raise ValueError("k no puede ser mayor que n")
    if n < 0:

            raise ValueError("n no puede ser menor que 0")
    if k < 0:

            raise ValueError("k no puede ser menor que 0")
    if i < 0:

            raise ValueError("i no puede ser menor que 0")
    if i > k+1:

            raise ValueError("i no puede ser mayor que k+1")
    
    producto = 1
    for j in range(i, k - 1):  
        producto *= (n - j + 1)    

    return producto

n = 5
k = 4
i = 1
resultado = P2(n, k, i)
try:

    print(f"El resultado de P2({n}, {k}, {i}) es: {resultado}")

except (TypeError, ValueError) as e:

    print(f"Error: {e}")

import math
def C2(n:int, k:int) -> int:

    if k >= n:

        raise ValueError("k no puede ser mayor o igual que n")

    return math.factorial(n) // (math.factorial(k+1) * math.factorial(n - k - 1))
n = 4
k = 2
try:

    print(f"El número combinatorio de {n} y {k+1} es: {C2(n, k)}")

except (TypeError, ValueError) as e:

    print(f"Error: {e}")

def S2(n:int, k:int) -> float:
    n = 4
    k = 2
    assert n > 0, "El valor de n debe ser positivo"
    assert k > 0, "El valor de k debe ser positivo"
    
    if k > n:
        raise ValueError("k no puede ser mayor que n")
    suma = 0

    for i in range(k+1):

        termino = (-1)**i * C2(k, i) * (k - i)**(n+1)

        suma += termino

        resultado = (suma * math.factorial(k)) / (n * (math.factorial(k+2)))

    return resultado

try:

    print(f"El número S2(n, k) siendo n = {n} y k = {k} es: {resultado}")

except (TypeError, ValueError) as e:

    print(f"Error: {e}")

from collections import Counter
from typing import List, Tuple

def palabrasMasComunes(fichero: str, n: int = 5) -> List[Tuple[str, int]]:
    
    assert n > 1, "El valor de n debe ser mayor que 1."
    try:
    
        with open(fichero, encoding='utf-8') as file:
            texto = file.read().lower()  

    
        palabras = texto.split()

    
        contador = Counter(palabras)

    
        palabras_mas_comunes = contador.most_common(n)

        return palabras_mas_comunes

    except FileNotFoundError:

        print(f"El archivo '{fichero}' no existe")

        return None

resultado = palabrasMasComunes('../data/archivo_palabras.txt', 5)
print(f"Las palabras más comunes son: {resultado}")
