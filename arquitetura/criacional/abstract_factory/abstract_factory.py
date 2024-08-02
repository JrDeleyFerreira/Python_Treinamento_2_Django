from abc import ABC, abstractmethod

# --------------->> Classes abstratas <<---------------
class VeiculoDeLuxo(ABC):
    @abstractmethod
    def busca_cliente(self) -> None: pass
    
class VeiculoPopular(ABC):
    @abstractmethod
    def busca_cliente(self) -> None: pass
    
    
# ===================================================================
# --------------->> Classes concretas da ZONA NOBRE <<---------------
class CarroDeLuxoZN(VeiculoDeLuxo):
    def busca_cliente(self) -> None:
        print('Carro de LUXO, da ZONA NOBRE, está à caminho do cliente.')
           
class MotoDeLuxoZN(VeiculoDeLuxo): # Classe concreta
    def busca_cliente(self) -> None:
        print('Moto de LUXO, da ZONA NOBRE, está à caminho do cliente.')
        
class CarroPopularZN(VeiculoPopular):
    def busca_cliente(self) -> None:
        print('Carro POPULAR, da ZONA NOBRE, está à caminho do cliente.')
             
class MotoPopularZN(VeiculoPopular): # Classe concreta
    def busca_cliente(self) -> None:
        print('Moto POPULAR, da ZONA NOBRE, está à caminho do cliente.')
        

# ===================================================================
# --------------->> Classes concretas da ZONA POPULAR <<---------------        
class CarroDeLuxoZP(VeiculoDeLuxo):
    def busca_cliente(self) -> None:
        print('Carro de LUXO, da ZONA POPULAR, está à caminho do cliente.')
           
class MotoDeLuxoZP(VeiculoDeLuxo): # Classe concreta
    def busca_cliente(self) -> None:
        print('Moto de LUXO, da ZONA POPULAR, está à caminho do cliente.')
        
class CarroPopularZP(VeiculoPopular):
    def busca_cliente(self) -> None:
        print('Carro POPULAR, da ZONA POPULAR, está à caminho do cliente.')
             
class MotoPopularZP(VeiculoPopular): # Classe concreta
    def busca_cliente(self) -> None:
        print('Moto POPULAR, da ZONA POPULAR, está à caminho do cliente.')
        
        
# ===================================================================    
# --------------->> Classe abstrata (Filha) <<---------------     
class VeiculoFactory(ABC): 
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoDeLuxo: pass
    
    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoDeLuxo: pass
    
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass
    
    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular: pass
    
    
# ===================================================================
# --------------->> Classes construtoras distintas <<---------------
class ZonaNobreFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoDeLuxo:
        return CarroDeLuxoZN()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoDeLuxo:
        return MotoDeLuxoZN()
    
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()
    
    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()

class ZonaPopularFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoDeLuxo:
        return CarroDeLuxoZP()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoDeLuxo:
        return MotoDeLuxoZP()
    
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZP()
    
    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZP()


# ===================================================================
# --------------->> Classe instanciável <<---------------
class ClienteChama:
    def busca_clientes(self):
        for factory in ZonaNobreFactory(), ZonaPopularFactory():
            
            carro_luxo = factory.get_carro_luxo()
            carro_luxo.busca_cliente()
            
            carro_popular = factory.get_carro_popular()
            carro_popular.busca_cliente()
            
            moto_luxo = factory.get_moto_luxo()
            moto_luxo.busca_cliente()
            
            moto_popular = factory.get_moto_popular()
            moto_popular.busca_cliente()
            
            
# ===================================================================
# --------------->> Como usar <<---------------
if __name__ == '__main__':
    cliente = ClienteChama()
    cliente.busca_clientes()
    
'''
Nesse modelo existe uma separação do serviço em Zonas.
Cada zona pode possuir um tipo de veíxulo, ou todos.
    - Cada 1 com suas especificações
O Cliente é genérico e pode estar em qualquer uma das zonas
'''