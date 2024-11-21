'''
Created on 8 nov 2024

@author: rodri
'''
from __future__ import annotations
from typing import TypeVar, Generic, List

E = TypeVar('E')  

class Pila(Generic[E]):
    def __init__(self) -> None:
        self._elements: List[E] = []

    @classmethod
    def of(cls) -> Pila[E]:
        return cls()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)  

    def remove(self) -> E:
        assert len(self._elements) > 0
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while self._elements:
            removed_elements.append(self.remove())
        return removed_elements

    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return self.size() == 0

    def elements(self) -> List[E]:
        return self._elements[:]

    def __str__(self) -> str:
        return f"Pila({self._elements})"


def test_pila():
    pila = Pila.of()

    pila.add(1)
    pila.add(2)
    pila.add(3)

    assert pila.elements() == [3, 2, 1]

    top_element = pila.remove()
    assert top_element == 3
    assert pila.elements() == [2, 1]

    removed_elements = pila.remove_all()
    assert removed_elements == [2, 1]
    assert pila.is_empty()

    print("Pruebas superadas exitosamente.")

if __name__ == "__main__":
    test_pila()