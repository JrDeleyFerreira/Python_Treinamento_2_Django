from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict

# ------------------>> Receiver - Luz inteligente <<------------------
class Light:
    def __init__(self, name: str, room_name: str, ) -> None:
        self._name = name
        self._room_name = room_name
        self._color = 'Default Color'
        
    def on(self) -> None:
        print(f'{self._name}, in room {self._room_name} is now ON.')
        
    def off(self) -> None:
        print(f'{self._name}, in room {self._room_name} is now OFF.')
    
    # Pode criar uma nova classe concreta para implementar essa ação    
    def change_color(self, color: str) -> None:
        self._color = color
        print(f'{self._name}, in room {self._room_name} is now color: {self._color}')

# ------------------>> Interface de Comando <<------------------
class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...  

# ------------------>> Classe concreta de comando <<------------------
class LightOnAndOffCommand(ICommand):
    def __init__(self, light: Light) -> None:
        self._light = light
        
    def execute(self) -> None:
        self._light.on()
    
    def undo(self) -> None:
        self._light.off()

# ------------------>> Invoker - Controle remoto <<------------------
class RemoteController:
    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        
    def button_add_command(self, id_btn: str, command: ICommand) -> None:
        self._buttons[id_btn] = command
        
    # Os botões podem ter ciência um do outro para evitar ações desnecessárias
    def button_pressed_on(self, id_btn: str) -> None:
        if id_btn in self._buttons:
            self._buttons[id_btn].execute()
            
    def button_pressed_off(self, id_btn: str) -> None:
        if id_btn in self._buttons:
            self._buttons[id_btn].undo()

# ------------------>> Como usar <<------------------
if __name__ == '__main__':
    
    luz_suite = Light('Luz do quarto', 'Suite')
    luz_cozinha = Light('Luz cozinha', 'Cozinha')
    
    botao_luz_suite = LightOnAndOffCommand(luz_suite)
    botao_luz_cozinha = LightOnAndOffCommand(luz_cozinha)
    
    remote_controller = RemoteController()
    
    remote_controller.button_add_command('button_1', botao_luz_suite)
    remote_controller.button_add_command('button_2', botao_luz_cozinha)
    
    remote_controller.button_pressed_on('button_1')
    remote_controller.button_pressed_off('button_1')
    remote_controller.button_pressed_on('button_2')
    remote_controller.button_pressed_off('button_2')
    