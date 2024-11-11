'''
Created on 19 oct 2024

@author: rodri
'''
def contar_palabras(fichero, sep, cad):

    contador = 0

    cad = cad.lower()

    try:

        with open(fichero, encoding='utf-8') as archivo:

            for linea in archivo:

                palabras = linea.lower().strip().split(sep)

                contador += palabras.count(cad)

    except FileNotFoundError:

        print(f"El archivo '{fichero}' no existe")

        return 0

    

    return contador

fichero ='../../data/lin_quijote.txt'

sep = ' '

cad = 'quijote'

try:

    print(f"El número de veces que aparece la palabra '{cad}' en el fichero '{fichero}' es: '{contar_palabras(fichero, sep, cad)}'")

except (TypeError, ValueError) as e:

    print(f"Error: {e}")

def buscar_lineas_con_cadena(fichero, cad):

    lineas_con_cadena = []

    try:

        cad = cad.lower()

        with open(fichero, encoding='utf-8') as archivo:

            for linea in archivo:

                if cad in linea.lower():

                    lineas_con_cadena.append(linea.strip())

    except FileNotFoundError:

        print(f"El archivo '{fichero}' no existe")

        return []

    return lineas_con_cadena

fichero = '../../data/lin_quijote.txt'

cad = 'quijote'

resultado = buscar_lineas_con_cadena(fichero, cad)

try:

    print(f"Las líneas en las que aparece la palabra '{cad}' son: ")

    for linea in resultado:

        print(linea)

except (TypeError, ValueError) as e:

    print(f"Error: {e}")

def palabras_unicas(fichero: str) -> list:

    palabras_unicas_set = set()

    try:

        with open(fichero, encoding='utf-8') as archivo:

            for linea in archivo:

                palabras = linea.lower().split()

                palabras_unicas_set.update(palabras)

    except FileNotFoundError:

        print(f"El archivo '{fichero}' no existe")

    return list(palabras_unicas_set)

fichero = '../../data/archivo_palabras.txt'

final = palabras_unicas(fichero)

try:

    print(f"Las palabras únicas en el fichero '{fichero}' son: ")

    print(final)

except (TypeError, ValueError) as e:

    print(f"Error: {e}")

from typing import Optional
def longitud_promedio_lineas(file_path:str, sep:str = ',') -> Optional[float]:

    total_longitud = 0

    total_lineas = 0

    try:

        with open(file_path, encoding='utf-8') as archivo:

            for linea in archivo:

                linea = linea.strip()

                if linea:

                    total_longitud += len(linea)

                    total_lineas += 1

        if total_lineas == 0:

            return None

        return total_longitud / total_lineas

    except FileNotFoundError:

        print(f"El archivo '{file_path}' no existe")

        return None

fichero = '../../data/palabras_random.csv'
conclusion = longitud_promedio_lineas(fichero)
if conclusion is not None:

    print(f"La longitud promedio de las líneas del fichero '{fichero}' es: {conclusion:.2f}")

else:

    print("No se pudo calcular la longitud media de las líneas")