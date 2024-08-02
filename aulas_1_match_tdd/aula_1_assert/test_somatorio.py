import unittest
import requests

from somatorio import soma_dois_numeros
from unittest.mock import patch

class TesteSomatorio(unittest.TestCase):
    def teste_soma_5_e_5_retorna_10(self):
        self.assertEqual(soma_dois_numeros(5,5), 10)
        
    def teste_soma_varias_entradas(self):
        x_y_saida = ((10, 10, 20), 
                     (5.2, 8.4, 13.6), 
                     (-9, 15, 6))
        for tupla in x_y_saida:
            with self.subTest(x_y_saida = x_y_saida):
                x, y, saida = tupla
                self.assertEqual(soma_dois_numeros(x, y), saida)
                
    def teste_parametros_diferentes_int_float(self):
        with self.assertRaises(AssertionError):
            soma_dois_numeros('a', 15)
            
# ------------->> Segunda Parte <<-------------

class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self._nome = nome
        self._sobrenome = sobrenome
        self._outros_dados = False
        
    def obter_todos_os_dados(self):
        # resposta = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        resposta = requests.get('') # Assim funciona para o teste
        if resposta.ok:
            self._outros_dados = True
            return 'CONECTADO'
        else:
            return 'FALHA CONEXÃO'
        

class TestePessoa(unittest.TestCase):
    def setUp(self) -> None:
        self._p1 = Pessoa('Wanderley', 'Ferreira')
        return super().setUp()
    
    def test_nome_e_str(self):
        self.assertIsInstance(self._p1._nome, str)
        
    def test_obter_dados_pessoa_OK(self):
        with patch('requests.get') as fake_data:
            fake_data.return_value.ok = True   
            self.assertEqual(self._p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self._p1._outros_dados)
            
    def test_obter_dados_pessoa_FAIL(self):
        with patch('requests.get') as fake_data:
            fake_data.return_value.ok = False   
            self.assertEqual(self._p1.obter_todos_os_dados(), 'FALHA CONEXÃO')
            
if __name__ == '__main__':
    unittest.main(verbosity=2)
