class SingletonMixim:
    def __str__(self) -> str:
        params = ','.join([f'{k} ={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__} - ({params})'
    
    def __repr__(self) -> str:
        return self.__str__()
    
class MonoStateSimple(SingletonMixim):
    _state = {
        # 'altura': 1.64,
        # 'idade': 34
    }
    
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._state
        return obj
    
    
    def __init__(self, nome= None, sobrenome= None) -> None:
        # self.__dict__ = self._state
        
        if nome is not None:
            self._nome = nome
        if sobrenome is not None:
            self._sobrenome = sobrenome

        
if __name__ == '__main__':
    m1 = MonoStateSimple(nome= 'Wanderley')
    m2 = MonoStateSimple(sobrenome= 'Ferreira')
    print(m1)
    print(m2)
    # print(m1, f'Idade= {m1.idade}', f'Altura= {m1.altura}')
    # print(m2, f'Idade= {m2.idade}', f'Altura= {m2.altura}')