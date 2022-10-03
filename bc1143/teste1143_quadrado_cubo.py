from bee1143_quadrado_cubo import quadradocubo

import unittest

class quadrado_cubo(unittest.TestCase):

    def test_quadradocubo(self):
        self.assertEqual(quadradocubo(1), ['1 1 1'])
        self.assertEqual(quadradocubo(3), ['1 1 1', '2 4 8', '3 9 27'])
        self.assertEqual(quadradocubo(5), ['1 1 1', '2 4 8', '3 9 27', '4 16 64', '5 25 125'])
        self.assertEqual(quadradocubo(7), ['1 1 1', '2 4 8', '3 9 27', '4 16 64', '5 25 125', '6 36 216', '7 49 343'])
        self.assertEqual(quadradocubo(9), ['1 1 1', '2 4 8', '3 9 27', '4 16 64', '5 25 125', '6 36 216', '7 49 343', '8 64 512', '9 81 729'])

if __name__ == '__main__':
    unittest.main()