'''
Created on 8 nov 2024

@author: rodri
'''
from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple

E = TypeVar('E')  
P = TypeVar('P')  
class Cola_de_prioridad(Generic[E, P]):
    def __init__(self) -> None:
        self._elements: List[E] = []
        self._priorities: List[P] = []

    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return self.size() == 0

    def elements(self) -> List[E]:
        return self._elements[:]

    def __index_order(self, priority: P) -> int:
        for i, existing_priority in enumerate(self._priorities):
            if priority < existing_priority:
                return i
        return len(self._priorities)

    def add(self, e: E, priority: P) -> None:
        index = self.__index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for element, priority in ls:
            self.add(element, priority)

    def remove(self) -> E:
        assert not self.is_empty()
        self._priorities.pop(0)
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed = []
        while not self.is_empty():
            removed.append(self.remove())
        return removed

    def decrease_priority(self, e: E, new_priority: P) -> None:
        if e in self._elements:
            index = self._elements.index(e)
            current_priority = self._priorities[index]
            if new_priority < current_priority:
                self._elements.pop(index)
                self._priorities.pop(index)
                self.add(e, new_priority)

    def __str__(self) -> str:
        return f"ColaPrioridad[{[(e, p) for e, p in zip(self._elements, self._priorities)]}]"

def test_cola_prioridad():
    cola = Cola_de_prioridad[str, int]()
    cola.add('Paciente A', 3)  
    cola.add('Paciente B', 2)  
    cola.add('Paciente C', 1)  

    assert cola.elements() == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de la cola es incorrecto."

    atencion = []
    while not cola.is_empty():
        atencion.append(cola.remove())

    assert atencion == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de atención no es correcto."

    print("Pruebas superadas exitosamente.")

if __name__ == '__main__':
    test_cola_prioridad()