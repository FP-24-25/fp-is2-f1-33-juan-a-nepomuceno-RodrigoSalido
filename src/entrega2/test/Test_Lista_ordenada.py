'''
Created on 8 nov 2024

@author: rodri
'''
from __future__ import annotations
from typing import Callable, Generic, List, TypeVar
from abc import ABC, abstractmethod

E = TypeVar('E')
R = TypeVar('R')

class AgregadoLineal(ABC, Generic[E]):

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

class Lista_ordenada(AgregadoLineal[E], Generic[E, R]):

    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self.__order = order

    @staticmethod
    def of(order: Callable[[E], R]) -> Lista_ordenada[E, R]:
        return Lista_ordenada(order)

    def __index_order(self, e: E) -> int:
        for index, element in enumerate(self._elements):
            if self.__order(e) < self.__order(element):
                return index
        return len(self._elements)

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)

    def __repr__(self) -> str:
        elementos = ', '.join(map(str, self._elements))
        return f"ListaOrdenada({elementos})"



if __name__ == "__main__":
    print("TEST DE LISTA ORDENADA:")
    print("#" * 48)

    lista = Lista_ordenada.of(lambda x: x)
    print("Creación de una lista con criterio de orden lambda x: x")
    print("Se añade en este orden: 3, 1, 2")
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print(f"Resultado de la lista: {lista}")

    print("#" * 48)

    removed_element = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed_element}")

    print("#" * 48)

    lista.add(3)
    lista.add(1)
    lista.add(2)
    removed_all = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_all}")

    print("#" * 48)

    print("Comprobando si se añaden los números en la posición correcta...")
    lista.add(3)
    lista.add(1)
    lista.add(2)
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(10)
    print(f"Lista después de añadirle el 10: {lista}")
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")