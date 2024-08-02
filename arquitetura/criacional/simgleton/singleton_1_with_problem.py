class AppSettings:
    _instance = None
    
    def __init__(self) -> None:
        self.tema = 'Tema escuro'
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Tema Drácula' # Modifica o tema
    
    as2 = AppSettings() # Nova instância redefine o tema
    print(as1.tema)