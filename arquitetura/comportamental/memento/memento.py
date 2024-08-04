from __future__ import annotations
from typing import Any, Dict, List
from copy import deepcopy

# -->> Classe Memento <<--
class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state', state)
        
    def get_state(self) -> Dict:
        return self._state
    
    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError('Imutable Class')

# -->> Classe objeto com estados <<--
class ImageEditor:
    def __init__(self, name: str, width: int, hight: int) -> None:
        self._name = name
        self._width = width
        self._higth = hight
        
    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))
    
    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()
        
    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'
    
# -->> Classe de controle <<--
class CareTaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: List[Memento] = []
        
    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())
        
    def restore(self) -> None:
        if not self._mementos:
            return
        self._originator.restore(self._mementos.pop())

    
# ------------------>> Como usar <<------------------
if __name__ == '__main__':
    img = ImageEditor('Foto_Família.jpg', 240, 240)
    cartaker = CareTaker(img)
    
    cartaker.backup()
    
    img._name = 'Eu_na_praia.jpg'
    img._higth = 500
    cartaker.backup()
    
    img._name = 'Eu_em_Maceio.jpg'
    img._width = 360
    cartaker.backup()
    
    print(img)
    
    cartaker.restore()
    print(img)
    cartaker.restore()
    print(img)
    cartaker.restore()
    print(img)
    cartaker.restore()
    print(img)
    cartaker.restore()
    print(img)
    cartaker.restore()
    print(img)
    cartaker.restore()
    print(img)
    cartaker.restore()
    print(img)
    