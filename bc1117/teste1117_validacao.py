from bee1117_Validacao import notasValidas

import unittest

class teste_notas(unittest.TestCase):

    def test_notas_validas(self):
        self.assertEqual(notasValidas(4.5, 8.2), 6.35)
        self.assertEqual(notasValidas(8, 7.5), 7.75)
        self.assertEqual(notasValidas(6.6, 9), 7.8)
        self.assertEqual(notasValidas(3, 10), 6.5)
        self.assertEqual(notasValidas(9, -5), "Nota inválida")

if __name__ == '__main__':
    unittest.main()
