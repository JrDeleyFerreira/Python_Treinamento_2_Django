from __future__ import annotations
from abc import ABC, abstractmethod

class IRemoteControll(ABC):
    @abstractmethod
    def increase_volume(self) -> None: ...
    @abstractmethod
    def decrease_volume(self) -> None: ...
    @ abstractmethod
    def power(self) -> None: ...
    
class RemoteControl(IRemoteControll):
    def __init__(self, device: IDevice) -> None:
        self._device = device
    
    def increase_volume(self) -> None:
        self._device.volume += 5
    
    def decrease_volume(self) -> None:
        self._device.volume -= 5
    
    def power(self) -> None:
        self._device.power = not self._device.power

class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: pass
    
    @volume.setter
    def volume(self, volume: int) -> None: pass
    
    @property
    @abstractmethod
    def power(self) -> bool: pass
    
    @power.setter
    def power(self, click: bool) -> None: pass
    
class TV(IDevice):
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
    
    @property
    def volume(self) -> int: 
        return self._volume
    
    @volume.setter
    def volume(self, volume: int) -> None:
        if not self._power:
            print(f'Please, turn {self.__class__.__name__} ON')
            return
        if volume > 100 or volume < 0:
            return
        self._volume = volume
        print(f'Volume is now {self._volume}')
    
    @property
    def power(self) -> bool:
        return self._power
    
    @power.setter
    def power(self, click: bool) -> None:
        self._power = click
        power_status = 'ON' if self._power else 'OFF'
        print(f'{self.__class__.__name__} is now {power_status}')
        

if __name__ == '__main__':
    tv = TV()
    remote = RemoteControl(tv)
    
    remote.increase_volume()
    remote.power()
    
    for i in range(10):
        remote.increase_volume()
        
    remote.power()
    remote.decrease_volume()
    remote.power()
    
    for i in range(8):
        remote.decrease_volume()