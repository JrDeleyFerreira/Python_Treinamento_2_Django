from __future__ import annotations
from abc import ABC, abstractmethod

# ----->> Interface existente <<-----
class IControll(ABC):
    @abstractmethod
    def top(self) -> None: pass
    @abstractmethod
    def down(self) -> None: pass
    @abstractmethod
    def left(self) -> None: pass
    @abstractmethod
    def rigth(self) -> None: pass

# ----->> Classe padrão já existente <<-----
class Control(IControll):
    def top(self) -> None:
        print('Movendo para cima.')
    def down(self) -> None:
        print('Movendo para baixo.')
    def left(self) -> None:
        print('Movendo para esquerda.')
    def rigth(self) -> None:
        print('Movendo para direita.')

# ----->> Classe a Adaptar comportamento <<-----
class NewControl():
    def move_to_top(self) -> None:
        print('NewControl: Movendo para cima.')
    def move_to_down(self) -> None:
        print('NewControl: Movendo para baixo.')
    def move_to_left(self) -> None:
        print('NewControl: Movendo para esquerda.')
    def move_to_rigth(self) -> None:
        print('NewControl: Movendo para direita.')
        
# ----->> Control Adapter Composição <<-----
class ControlAdapter():
    def __init__(self, new_control: NewControl) -> None:
        self._new_control = new_control
        
    def top(self) -> None:
        self._new_control.move_to_top()
    
    def down(self) -> None:
        self._new_control.move_to_down()
    
    def left(self) -> None:
        self._new_control.move_to_left()
    
    def rigth(self) -> None:
        self._new_control.move_to_rigth()

# ----->> Control Adapter Herança <<-----
class AdapterControlHeranca(Control, NewControl):
    def top(self) -> None:
        self.move_to_top()
        
    def down(self) -> None:
        self.move_to_down()
        
    def left(self) -> None:
        self.move_to_left()
        
    def rigth(self) -> None:
        self.move_to_rigth()

# ----->> Como usar <<-----
if __name__ == '__main__':
    new_control = NewControl()
    c1 = ControlAdapter(new_control)
    c1.top()
    c1.rigth()
    c1.down()
    c1.left()
    
    c2 = Control()
    c2.top()
    c2.rigth()
    c2.down()
    c2.left()
    
    c3 = AdapterControlHeranca()
    c3.top()
    c3.rigth()
    c3.down()
    c3.left()