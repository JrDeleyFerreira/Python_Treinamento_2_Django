def soma_dois_numeros(x, y):
    assert isinstance(x, (int, float)), 'X deve ser do tipo INT ou FLOAT.'
    assert isinstance(y, (int, float)), 'Y deve ser do tipo INT ou FLOAT.'
    return round(x + y, 2)

'''
>>> soma_dois_numeros(15, 22)
37

>>> soma_dois_numeros('15', 22)
Traceback (most recent call last):
...
AssertionError: X precisa ser int ou float
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)