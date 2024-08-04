from __future__ import annotations
from abc import ABC, abstractmethod

# ------------------>> Interface <<------------------
class Handler(ABC):
    def __init__(self) -> None:
        self._sucessor: Handler
    
    @abstractmethod
    def handle(self, letra: str) -> str: pass

# ------------------>> Classes concretas <<------------------
class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self._letras = ['A', 'B', 'C']
        self._sucessor = sucessor
        
    def handle(self, letra: str) -> str:
        if letra in self._letras:
            return f'{self.__class__.__name__} = Conseguiu tratar o valor {letra}'
        return self._sucessor.handle(letra)
    
class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self._letras = ['D', 'E', 'F']
        self._sucessor = sucessor
        
    def handle(self, letra: str) -> str:
        if letra in self._letras:
            return f'{self.__class__.__name__} = Conseguiu tratar o valor {letra}'
        return self._sucessor.handle(letra)

class HandlerUnsolved(Handler):        
    def handle(self, letra: str) -> str:
        return f'{self.__class__.__name__} = Não tratou {letra}'

# ------------------>> Como usar <<------------------
if __name__ == '__main__':
    handler_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)