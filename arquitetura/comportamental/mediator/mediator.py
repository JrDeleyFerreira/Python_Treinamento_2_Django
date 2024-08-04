from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# ------------------>> Interface de Comunicação <<------------------
class IColleague(ABC):
    def __init__(self) -> None:
        self._name: str
        
    @abstractmethod
    def broadcast(self, msg: str) -> None: pass
    @abstractmethod
    def direct(self, msg: str) -> None: pass

# ------------------>> Classe Agentes <<------------------    
class Pessoa(IColleague):
    def __init__(self, name: str, mediator: IMediator) -> None:
        self._name = name
        self._mediator = mediator
        
    def broadcast(self, msg: str) -> None:
        self._mediator.show_broadcast(self, msg)
    
    def direct(self, msg: str) -> None:
        print(msg)
        
    def sender_direct(self, receiver: str, msg: str) -> None:
        self._mediator.contact_direct(self, receiver, msg)

# ------------------>> Interface de Mediação <<------------------    
class IMediator(ABC):        
    @abstractmethod
    def show_broadcast(self, person: IColleague, msg: str) -> None: ...
    @abstractmethod
    def contact_direct(self, sender: IColleague, receiver: str, msg: str) -> None: ...

# ------------------>> Classe de ambiente de comunicação <<------------------    
class ChatRoom(IMediator):
    def __init__(self) -> None:
        self._collegues: List[IColleague] = []
        
    def is_collegue(self, collegue: IColleague) -> bool:
        return collegue in self._collegues
        
    def add(self, collegue: IColleague) -> None:
        if not self.is_collegue(collegue):
            self._collegues.append(collegue)
            
    def remove(self, collegue: IColleague) -> None:
        if self.is_collegue(collegue):
            self._collegues.remove(collegue)
            
    def show_broadcast(self, person: IColleague, msg: str) -> None:
        if not self.is_collegue(person): 
            return
        print(f'{person._name} disse: {msg}')
        
    def contact_direct(self, sender: IColleague, receiver: str, msg: str) -> None:
        if not self.is_collegue(sender): 
            return
        
        receiver_obj: List[IColleague] = [
            collegue for collegue in self._collegues
            if collegue._name == receiver
        ]
        
        if not receiver_obj: return
        
        receiver_obj[0].direct(
            f'{sender._name}: para {receiver_obj[0]._name} = {msg}'
        )
        
# ------------------>> Como usar <<------------------
if __name__ == '__main__':
    chat = ChatRoom() # Primeiro criamos o ambiente
    
    # Cria e Adiciona agentes ao ambiente 
    joao = Pessoa('João', chat)
    felipe = Pessoa('Felipe', chat)
    aline = Pessoa('Aline', chat)
    
    chat.add(joao)
    chat.add(aline)
    
    joao.broadcast('Olá, pessoal!')
    aline.broadcast('Oi, como estão tds vcs?')
    felipe.broadcast('Ainda não fui adicionado.') # Ainda não foi add ao chat , então não aparece a msg
    
    print()
    
    joao.sender_direct('Aline', 'Oi, Maria, tudo bem?')
    aline.sender_direct('João', 'Oi, seu bobo!')