def verificacao(command: str) -> None:
    match command:
        case 'cd':
            print('Comando cd digitado.')
        case ['ls' | 'list']:
            print('Comando de listagem selecionado')
        case _:
            print('Nenhum comando válido digitado')