from abc import ABC, abstractmethod

# --------------->> Classe abstrata <<---------------
class Veiculo(ABC):
    @abstractmethod
    def busca_cliente(self) -> None: pass
    
    
# --------------->> Classes concretas <<---------------
class CarroDeLuxo(Veiculo):
    def busca_cliente(self) -> None:
        print('Carro de LUXO está à caminho do cliente.')
           
class CarroPopular(Veiculo):
    def busca_cliente(self) -> None:
        print('Carro POPULAR está à caminho do cliente.')
         
class MotoDeLuxo(Veiculo): # Classe concreta
    def busca_cliente(self) -> None:
        print('Moto de LUXO está à caminho do cliente.')
            
class MotoPopular(Veiculo): # Classe concreta
    def busca_cliente(self) -> None:
        print('Moto POPULAR está à caminho do cliente.')
        
        
# --------------->> Classe abstrata (Filha) <<---------------     
class VeiculoFactory(ABC): # Não é mais instanciável, apenas disponibiliza a função comum
    def __init__(self, tipo) -> None:
        self._carro = self.get_type_car(tipo= tipo)
        
    def _busca_cliente(self) -> None:
        self._carro.busca_cliente()
    
    @staticmethod
    @abstractmethod
    def get_type_car(tipo: str) -> Veiculo: pass
        
        
# --------------->> Classes construtoras distintas <<---------------
class ZonaNobreFactory(VeiculoFactory): # Gera com parâmetros distintos
    @staticmethod
    def get_type_car(tipo: str) -> Veiculo:
        match tipo:
            case 'carro_luxo':
                return CarroDeLuxo()
            case 'carro_popular':
                return CarroPopular()
            case 'moto_luxo':
                return MotoDeLuxo()
            case 'moto_popular':
                return MotoPopular()
            case _:
                raise


class ZonaPopularFactory(VeiculoFactory): # Gera com parâmetros distintos
    @staticmethod
    def get_type_car(tipo: str) -> Veiculo:
        match tipo:
            case 'carro_popular':
                return CarroPopular()
            case 'moto_popular':
                return MotoPopular()
            case _:
                raise


# --------------->> Como usar <<---------------
if __name__ == '__main__':
    novo_carro_1 = ZonaNobreFactory('carro_luxo') # pode receber qlqr dos 4 tipos
    novo_carro_2 = ZonaPopularFactory('moto_popular') # recebe apenas os 2 populares
