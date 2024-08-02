from typing import Any

# class Meta(type):
#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         return super().__call__(*args, **kwds)

# class PessoaSingleton(Meta):
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls, *args, **kwargs)
    
#     def __init__(self, nome: str):
#         self._nome = nome
        
#     def __call__(self, x, y) -> Any:
#         print('Call chamado!', self._nome, x * y)
        
# p1 = PessoaSingleton('Wanderley')
# print(p1._nome)


class SingletonMeta(type):
    _instances = {}
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in self._instances:
            self._instances[self] = super().__call__(*args, **kwds)
        return self._instances[self]

class AppSettings(metaclass= SingletonMeta):  
    def __init__(self) -> None:
        print('OI')
        self.tema = 'Tema Escuro'
        self.font = 'Fira Code'
        
if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Drácula'
    print(as1.tema)
    
    as2 = AppSettings()
    print(as2.tema)