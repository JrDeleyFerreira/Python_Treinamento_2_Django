from dataclasses import dataclass

@dataclass
class Ingredientes:
    price: float
    
@dataclass
class PaoHotDog(Ingredientes):
    price: float = 1.8
    
@dataclass
class Salsicha(Ingredientes):
    price: float = 1.75
    
@dataclass
class Milho(Ingredientes):
    price: float = 0.60
    
@dataclass
class BatataPalha(Ingredientes):
    price: float = 0.90

@dataclass
class QueijoRalado(Ingredientes):
    price: float = 1.45
    
@dataclass
class OvoDeCodorna(Ingredientes):
    price: float = 1.0
    
@dataclass
class Bacon(Ingredientes):
    price: float = 2.0