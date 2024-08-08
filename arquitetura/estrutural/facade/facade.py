from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict

# ---------------->> Interface Observable <<---------------->
class IObservable(ABC):
    @abstractmethod
    def state(self) -> None: ...
    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: ...
    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: ...
    @abstractmethod
    def _notify_observers(self) -> None: ...
    
# ---------------->> Class de Implementação do Observable <<---------------->
class WatherStation(IObservable):
    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}
        if new_state != self._state:
            self._state = new_state
            self._notify_observers()
    
    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)
    
    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()
        print()
            
    def reset_state(self):
        self._state = {}
        self._notify_observers()
        
# ---------------->> Interface Observer <<---------------->
class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: ...

# ---------------->> Classe Concreta Observer <<---------------->
class Smartphone(IObserver):
    def __init__(self, name: str, observable: IObservable) -> None:
        self._name = name
        self._observable = observable
    
    def update(self) -> None:
        obs_class_name = self._observable.__class__.__name__
        print(f'{self._name}, o objeto ({obs_class_name}) acabou de ser inicializado '
              f' => {self._observable.state}')

# <<--------------------------------->>
# ------------>> FACADE <<-------------
# <<--------------------------------->>
class WatherStationFacade:
    def __init__(self) -> None:
        self.wather_station = WatherStation()
        
        self.samsung_s20 = Smartphone('Samsung S20', self.wather_station)
        self.iphone_12_pro = Smartphone('IPhone 12 PRO', self.wather_station)
        
        self.wather_station.add_observer(self.samsung_s20)
        self.wather_station.add_observer(self.iphone_12_pro)
        
    def add_observer(self, observer: IObserver) -> None:
        self.wather_station.add_observer(observer)
        
    def remove_observer(self, observer: IObserver) -> None:
        self.wather_station.remove_observer(observer)
        
    def change_state(self, state: Dict) -> None:
        self.wather_station.state = state
        
    def remove_smartfone(self) -> None:
        self.wather_station.remove_observer(self.samsung_s20)

    def reset(self) -> None:
        self.wather_station.reset_state()

# ---------------->> Como usar <<---------------->
if __name__ == '__main__':
    # Ligação entre as classes
    wather_station = WatherStationFacade()
    
    wather_station.change_state({'Temperatura': '30°'})
    wather_station.change_state({'Temperatura': '30°'})
    wather_station.change_state({'Temperatura': '22°'})
    wather_station.change_state({'Umidade': '52%'})
    
    wather_station.remove_smartfone()
    wather_station.reset()
    
    wather_station.change_state({'Temperatura': '22°'})
    wather_station.change_state({'Umidade': '52%'})