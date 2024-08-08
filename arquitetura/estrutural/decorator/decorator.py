from __future__ import annotations
from typing import List
from ingredientes import *
from copy import deepcopy

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
    

class SimplHotDog(HotDog):
    def __init__(self) -> None:
        self._name = 'Hot Dog Simples'
        self._ingredientes: List[Ingredientes] = [
            PaoHotDog(),
            Salsicha(),
            BatataPalha()
        ]
        
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
    def __init__(self, hotdog: HotDog) -> None:
        self._hotdog = hotdog
        
    @property
    def name(self) -> str:
        return self._hotdog.name
    
    @property
    def price(self) -> float:
        return self._hotdog.price
    
    @property
    def ingredientes(self) -> List[Ingredientes]:
        return self._hotdog.ingredientes
    
# ----->> Decorator Concreto <<-----
class BaconDecorator(HotDogDecorator):
    def __init__(self, hotdog: HotDog) -> None:
        super().__init__(hotdog)
        
        self._ingrediente_add = Bacon()
        self._ingredientes = deepcopy(self._hotdog.ingredientes)
        self._ingredientes.append(self._ingrediente_add)
        
    @property
    def name(self) -> str:
        return (f'{self._hotdog.name} + {self._ingrediente_add.__class__.__name__}')
    
    @property
    def price(self) -> float:
        return round(
            sum([ingrediente.price for ingrediente in self._ingredientes]),
            2
        )
    
    @property
    def ingredientes(self) -> List[Ingredientes]:
        return self._ingredientes

# ----->> Como usar <<-----
if __name__ == '__main__':
    simple_hotdog = SimplHotDog()
    print(simple_hotdog)
    special_hotdog = SpecialHotDog()
    print(special_hotdog)
    decorated_simple = HotDogDecorator(simple_hotdog)
    print(decorated_simple)
    
    bacon_simple = BaconDecorator(simple_hotdog)
    print(bacon_simple)
    bacon_simple = BaconDecorator(bacon_simple)
    print(bacon_simple)
    
    