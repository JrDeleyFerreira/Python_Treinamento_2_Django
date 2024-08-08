from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict

# ----->> Interface <<-----
class IUser(ABC):
    firstname: str
    lastname: str
    
    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass
    @abstractmethod
    def get_all_user_data(self) -> Dict: ...

# ----->> Classe Real, com a lógica de back <<-----
class RealUser(IUser):
    def __init__(self, first_name: str, last_name: str) -> None:
        sleep(2) # Simulando requisição
        self._firstname = first_name
        self._lasname = last_name
        
    def get_addresses(self) -> List[Dict]:
        sleep(2) # Simulando requisição
        return [
            {'rua': 'Av. Brasil', 'numero': 104},
            {'rua': 'Silvio Hernesto', 'numero': 331},
        ]
    
    def get_all_user_data(self) -> Dict:
        sleep(2) # Simulando requisição
        return {'cpf': '100.100.100.88', 'rg': 'MG-11.111.111'}

# ----->> Classe Lazzy Loading <<-----
class UserProxy(IUser):
    def __init__(self, first_name: str, last_name: str) -> None:
        self._firstname = first_name
        self._lastname = last_name
        self._real_user: RealUser # Lazzy instanciation / Inicialização preguiçosa
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict
        
    # A instância está acima, porém, ainda não existe
    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self._firstname, self._lastname)
    
    def get_addresses(self) -> List[Dict]:
        self.get_real_user()
        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()
        return self._cached_addresses
    
    def get_all_user_data(self) -> Dict:
        self.get_real_user()
        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()
        return self._all_user_data

# ----->> Como usar <<-----
if __name__ == '__main__':
    user_me = UserProxy('Wanderley D.', 'Ferreira Jr.')
    print(user_me._firstname, user_me._lastname)
    
    # Leva 6 segundo, porém carrega no cache
    print(user_me.get_all_user_data())
    print(user_me.get_addresses())
    print()
    
    # Agora é instatâneo, pq já foi carregado
    for i in range(20):
        print(user_me.get_all_user_data())
    
    print()
    for i in range(20):
        print(user_me.get_addresses())
    