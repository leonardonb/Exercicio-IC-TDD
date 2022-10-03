from bee1132_multiplo13 import soma_mult13

import unittest

class teste_somamult13(unittest.TestCase):

    def test_somamult13(self):
        self.assertEqual(soma_mult13(0, 0), 0)
        self.assertEqual(soma_mult13(100, 101), 201)
        self.assertEqual(soma_mult13(200, 87), 15072)
        self.assertEqual(soma_mult13(-137, -243), -18822)
        self.assertEqual(soma_mult13(-15, 0), -107)

if __name__ == '__main__':
    unittest.main()