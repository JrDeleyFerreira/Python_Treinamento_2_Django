from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# ----->> Interface Composite <<-----
class IBoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None: pass
    @abstractmethod
    def get_price(self) -> float: pass
    
    def add(self, child: IBoxStructure) -> None: ...
    def remove(self, child: IBoxStructure) -> None: ...
    
# ----->> Classe concreta Composite <<-----
class Box(IBoxStructure):
    def __init__(self, name: str) -> None:
        self._name_box = name
        self._children: List[IBoxStructure] = []
    
    def print_content(self) -> None:
        print(f'\n{self._name_box}: ')
        for child in self._children:
            child.print_content()
    
    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children    
        ])
    
    def add(self, child: IBoxStructure) -> None:
        self._children.append(child)
        
    def remove(self, child: IBoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)

# ----->> Classe Leaf <<-----
class Product(IBoxStructure):
    def __init__(self, name: str, price: float) -> None:
        self._name_product = name
        self._price_product = price
    
    def get_price(self) -> float:
        return self._price_product
    
    def print_content(self) -> None:
        print(self._name_product, self._price_product)

# ----->> Como usar <<-----
if __name__ == '__main__':
    # Leaf
    camiseta1 = Product('Camiseta Azul', 47.9)
    camiseta2 = Product('Camiseta Cinza', 52.9)
    camiseta3 = Product('Camiseta Vermelha', 61.9)
    # Composite
    caixa_camisetas = Box('Caixa de Camisetas')
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)
    
    # Leaf
    smart_phone1 = Product('IPhone 12', 9000.9)
    smart_phone2 = Product('IPhone 14', 12749.9)
    # Composites
    caixa_smartphoes = Box('Caixa de SmartPhones')
    caixa_smartphoes.add(smart_phone1)
    caixa_smartphoes.add(smart_phone2)
    
    # Composite
    caixa_grande = Box('Caixa Produtos da China')
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphoes)
    
    caixa_grande.print_content()
    print()
    print(f'Valor total da caixa de Camisetas: $ {caixa_camisetas.get_price()}')
    print(f'Valor total da caixa de Smartphones: $ {caixa_smartphoes.get_price()}')
    print(f'Valor total da caixa China: $ {caixa_grande.get_price()}')
    