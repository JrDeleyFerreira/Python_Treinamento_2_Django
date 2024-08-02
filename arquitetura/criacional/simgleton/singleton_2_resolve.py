def singleton_dec(the_class):
    instances = {}
    
    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
            
    return get_class


@singleton_dec
class AppSettings:
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