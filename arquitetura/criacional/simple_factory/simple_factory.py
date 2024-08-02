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
        print('Carro de POPULAR está à caminho do cliente.')
        

# --------------->> Classe construtora <<---------------
class VeiculoFactory:
    # Forma sem devolver o objeto real - WRAPPER
    # def __init__(self, tipo) -> None:
    #     self._carro = self.get_type_car(tipo= tipo)
        
    # def busca_cliente(self) -> None:
    #     self._carro.busca_cliente()
    
    @staticmethod
    def get_type_car(tipo: str) -> Veiculo:
        match tipo:
            case 'luxo':
                return CarroDeLuxo()
            case 'popular':
                return CarroPopular()
            case _:
                raise
              

# --------------->> Como utilizar <<---------------    
if __name__ == '__main__':
    novo_carro_1 = VeiculoFactory().get_type_car('luxo')
    novo_carro_2 = VeiculoFactory().get_type_car('popular')
# OU com o __init__
    # carro_1 = VeiculoFactory('luxo')
    # carro_1.busca_cliente()