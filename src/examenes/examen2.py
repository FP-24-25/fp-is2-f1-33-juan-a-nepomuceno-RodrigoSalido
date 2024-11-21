'''
Created on 21 nov 2024

@author: rodri
'''
from __future__ import annotations
from typing import List, TypeVar, Generic
from abc import ABC, abstractmethod

E = TypeVar('E')

class AgregadoLineal(ABC, Generic[E]): #Sin modificar

    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def elements(self) -> List[E]:
        return self._elements

    @abstractmethod
    def add(self, e: E) -> None:
        pass

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        assert len(self._elements) > 0
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

class ColaConLimite(AgregadoLineal[E]):

    def __init__(self, capacidad: int):
        super().__init__()
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0.")
        self.capacidad = capacidad

    @classmethod
    def of(cls, capacidad: int) -> ColaConLimite[E]:
        """Método de factoría para crear una instancia de ColaConLimite."""
        return cls(capacidad)

    def add(self, e: E) -> None:
        """Agrega un elemento a la cola si no está llena. Lanza OverflowError si está llena."""
        if self.is_full:
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    @property
    def is_full(self) -> bool:
        """Verifica si la cola está llena."""
        return self.size >= self.capacidad

class AgregadoLineal(ABC, Generic[E]):   #Modificado

    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def elements(self) -> List[E]:
        return self._elements

    @abstractmethod
    def add(self, e: E) -> None:
        pass

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        assert len(self._elements) > 0, "No hay elementos para eliminar."
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    def contains(self, e: E) -> bool:
        """Verifica si un elemento dado se encuentra dentro del agregado."""
        return e in self._elements

    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        """
        Devuelve el primer elemento que cumple la condición especificada por func.
        Si no hay ningún elemento que cumpla la condición, devuelve None.
        """
        for element in self._elements:
            if func(element):
                return element
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        """
        Filtra los elementos según una condición especificada por func,
        devolviendo una lista con los elementos que cumplen la condición.
        """
        return [element for element in self._elements if func(element)]

if __name__ == "__main__":
#1. Implementación de una cola con límite de capacidad
    cola = ColaConLimite.of(3)  
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")
    
    try:
        cola.add("Tarea 4")
    except OverflowError as e:
        print(e)  
    
    print(cola.remove())  

#2. Modifica el tipo Agregado_Lineal
    class MiAgregado(AgregadoLineal[int]):
        def add(self, e: int) -> None:
            self._elements.append(e)

    agregado = MiAgregado()
    agregado.add_all([1, 2, 3, 4, 5])

    print(agregado.contains(3))  

    encontrado = agregado.find(lambda x: x > 3)
    print(encontrado)  

    pares = agregado.filter(lambda x: x % 2 == 0)
    print(pares)  

