from __future__ import annotations
from typing import List, Dict

# --->> Usuário externo à aplicação
class Cliente:
    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._addresses: List = []
    # Extrinsic
        self.address_number: int
        self.address_details: str
        
    def add_address(self, address: Address) -> None:
        self._addresses.append(address)
        
    def list_addresses(self) -> None:
        for addres in self._addresses:
            addres.show_address(self.address_number, self.address_details)

# --->> FlyWeight
class Address:
    def __init__(self, street: str, bairro: str, zip_code: str) -> None:
        self._rua = street
        self._bairro = bairro
        self._cep = zip_code
        
    def show_address(self, addres_number: int, address_detail: str) -> None:
        print(self._rua, addres_number, self._bairro, address_detail, self._cep)
        
# --->> Factory, sei lá pq
class AddressFactory:
    _addresses_fac: Dict = {} # Objeto proc flyweight
    
    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())
    
    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)
        
        try:
            address_flyweight = self._addresses_fac[key]
            print('Usando Objeto já criado!')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses_fac[key] = address_flyweight
            print('Criando Objeto aqui!')
            
        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()
    
    a1 = address_factory.get_address(rua='Silvio Horácio', bairro='Santa Mônica', cep='38.987-270')
    a2 = address_factory.get_address(rua='Silvio Horácio', bairro='Santa Mônica', cep='38.987-270')
    
    cliente = Cliente('Trossat')
    cliente.address_number = 471
    cliente.address_details = 'Casa'
    cliente.add_address(a1)
    cliente.list_addresses()
    
    cliente2 = Cliente('Joanna')
    cliente2.address_number = 900
    cliente2.address_details = 'Casa B - Fundos'
    cliente2.add_address(a2)
    cliente2.list_addresses()