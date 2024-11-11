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

class Lista_ordenada_sin_repeticion(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]) -> None:
        super().__init__()
        self.__order = order  

    @staticmethod
    def of(order: Callable[[E], R]) -> Lista_ordenada_sin_repeticion[E, R]:
        return Lista_ordenada_sin_repeticion(order)

    def __index_order(self, e: E) -> int:
        for i, element in enumerate(self._elements):
            if self.__order(e) > self.__order(element):
                return i
        return len(self._elements)

    def add(self, e: E) -> None:
        if e not in self._elements:
            index = self.__index_order(e)
            self._elements.insert(index, e)

    def __str__(self) -> str:
        return f"ListaOrdenadaSinRepeticion({', '.join(map(str, self._elements))})"








