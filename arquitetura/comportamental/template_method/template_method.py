from abc import ABC, abstractmethod

class IAbstract(ABC):
    def template_method(self) -> None:
        self.hook()
        self.print_in_all_concrete()
        self.operation1()
        self.operation2()
    
    def print_in_all_concrete(self) -> None:
        print('Método comum a todos os objetos concretos - Vim da Interface')
        
    def hook(self) -> None: pass
    
    @abstractmethod
    def operation1(self) -> None: pass
    @abstractmethod
    def operation2(self) -> None: pass 
    
    
class ConcreteClass(IAbstract):
    def operation1(self) -> None:
        print('Operação 1 concluída!')
    
    def operation2(self) -> None:
        print('Operação 2 concluída!')
        
class ConcreteClass2(IAbstract):
    def hook(self) -> None:
        print(f'OPA, a classe {self.__class__.__name__} possui HOOKS')
        
    def operation1(self) -> None:
        print('Operação 1, da segunda classe concreta, concluída!')
    
    def operation2(self) -> None:
        print('Operação 2, da segunda classe concreta, concluída!')
        
        
if __name__ == '__main__':
    c1 = ConcreteClass()
    c1.template_method()
    
    print()
    
    c2 = ConcreteClass2()
    c2.template_method()