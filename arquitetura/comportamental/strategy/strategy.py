from __future__ import annotations
from abc import ABC, abstractmethod

# Classe concreta - Entity
class Order: 
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount
        
    @property
    def total(self):
        return self._total
    
    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)

# Classe abstrata - Interface    
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, total_value: float) -> float: ...
    
# Implementa a interface
class TwentyPercent(DiscountStrategy):
    def calculate(self, total_value: float) -> float:
        return total_value - (total_value * 0.2)
    
if __name__ == '__main__':
    twenty_percent = TwentyPercent()
    order = Order(1000, twenty_percent)
    print(order.total, order.total_with_discount)