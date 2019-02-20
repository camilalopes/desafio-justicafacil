import unittest
from diarios.diario_scrapper import diario_scrapper as diario

class TesteDiarioScrapper(unittest.TestCase):
    def test_data(self):
        self.assertEqual(diario.lista_hash(''), 'Uma data inválida foi passada')
        
if __name__ == '__main__':
    unittest.main()
