from __future__ import annotations
from typing import List
from ingredientes import *
from copy import deepcopy

# ----->> Classe Property <<-----
class HotDog:
    _name: str
    _ingredientes: List[Ingredientes]
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> float:
        return round(
            sum([ingrediente.price for ingrediente in self.ingredientes]),
            2
        )
    
    @property
    def ingredientes(self) -> List[Ingredientes]:
        return self._ingredientes
    
    def __repr__(self) -> str:
        return f'{self.name} - ({self.price}) -> {self.ingredientes}'  
# ----->> Classe concreta de Objeto <<-----
class SimplHotDog(HotDog):
    def __init__(self) -> None:
        self._name = 'Hot Dog Simples'
        self._ingredientes: List[Ingredientes] = [
            PaoHotDog(),
            Salsicha(),
            BatataPalha()
        ]
# ----->> Classe concreta de Objeto <<-----      
class SpecialHotDog(HotDog):
    def __init__(self) -> None:
        self._name = 'Hot Dog Especial'
        self._ingredientes: List[Ingredientes] = [
            PaoHotDog(),
            Salsicha(),
            BatataPalha(),
            Milho(),
            QueijoRalado(),
            OvoDeCodorna(),
            Bacon()
        ]
# ----->> Decorator Genérico <<-----
class HotDogDecorator(HotDog):
    def __init__(self, hotdog: HotDog, ingrediente: Ingredientes) -> None:
        self._hotdog = hotdog
        self._ingrediente = ingrediente
        
        self._ingredientes = deepcopy(self._hotdog.ingredientes)
        self._ingredientes.append(self._ingrediente)
        
    @property
    def name(self) -> str:
        return f'{self._hotdog.name} + {self._ingrediente.__class__.__name__}'
    

# ----->> Como usar <<-----
if __name__ == '__main__':
    simple_hotdog = SimplHotDog()
    print(simple_hotdog)
    
    bacon_simple_hotdog = HotDogDecorator(simple_hotdog, Bacon())
    print(bacon_simple_hotdog)
    