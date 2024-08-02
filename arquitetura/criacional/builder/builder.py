from abc import ABC, abstractmethod
from typing import Any

# ----------------->> Classe Entity <<-----------------
class User:
    def __init__(self) -> None:
        self._nome: str | None = None
        self._idade: int | None = None
        self._phnes: list[str] | Any = []

# ----------------->> Classe Abstrata | Interface <<-----------------
class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): ... # Essa propriedade vai acessar todas as da Entity
    
    @abstractmethod
    def add_name(self, name: str): ... # Métodos set
    
    @abstractmethod
    def add_age(self, idade: int): ...
    
    @abstractmethod
    def add_phone(self, phone_number: str): ...
    
# ----------------->> Classe Concreta <<-----------------
class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        self.reset()
        
    def reset(self):
        self._result = User()
    
    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data
    
    def add_name(self, name: str):
        self._result._nome = name
    
    def add_age(self, idade: int):
        self._result._idade = idade
    
    def add_phone(self, phone: str):
        self._result._phnes.append(phone)

# ----------------->> Classe Construtora <<-----------------
class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder
        
    def with_name_and_age(self, name: str, age: int):
        self._builder.add_name(name= name)
        self._builder.add_age(idade= age)
        return self._builder.result
    
# ----------------->> Como Usar <<-----------------
if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    
    user1 = user_director.with_name_and_age('Wanderley', 34)
    