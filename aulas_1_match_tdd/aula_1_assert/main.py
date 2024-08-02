from somatorio import soma_dois_numeros

try:
    print(soma_dois_numeros('15', 2))
except AssertionError as error:
    print(f'Soma inválida: {error}')
