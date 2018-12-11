import unittest
from Python_1 import matrix_rotate, maximum_comp, queens
import re


class TestMatrixRotate(unittest.TestCase):

    def test_matrix(self):
        matrix = [[1, 0, 8],
                  [3, 4, 1],
                  [0, 4, 2]]
        self.assertEqual(matrix_rotate(matrix), [[1, 3, 0], [0, 4, 4], [8, 1, 2]])

    def test_matrix2(self):
        matrix = [[1, 0, 1],
                  [1, 0, 1],
                  [1, 0, 1]]
        self.assertEqual(matrix_rotate(matrix), [[1, 1, 1], [0, 0, 0], [1, 1, 1]])

    def test_matrix3(self):
        matrix = [[1, 0, 8],
                  [3, 4, 1],
                  [0, 4, 2]]
        self.assertNotEqual(matrix_rotate(matrix), [[1, 0, 8], [3, 4, 1], [0, 4, 2]])


class TestMaxComp(unittest.TestCase):
    number = '73167176531330624919225119674426574742355349194934' \
             '96983520312774506326239578318016984801869478851843' \
             '85861560789112949495459501737958331952853208805511' \
             '12540698747158523863050715693290963295227443043557' \
             '66896648950445244523161731856403098711121722383113' \
             '62229893423380308135336276614282806444486645238749' \
             '30358907296290491560440772390713810515859307960866' \
             '70172427121883998797908792274921901699720888093776' \
             '65727333001053367881220235421809751254540594752243' \
             '52584907711670556013604839586446706324415722155397' \
             '53697817977846174064955149290862569321978468622482' \
             '83972241375657056057490261407972968652414535100474' \
             '82166370484403199890008895243450658541227588666881' \
             '16427171479924442928230863465674813919123162824586' \
             '17866458359124566529476545682848912883142607690042' \
             '24219022671055626321111109370544217506941658960408' \
             '07198403850962455444362981230987879927244284909188' \
             '84580156166097919133875499200524063689912560717606' \
             '05886116467109405077541002256983155200055935729725' \
             '71636269561882670428252483600823257530420752963450'

    def test_max_num(self):
        self.assertEqual(maximum_comp(self.number)[0], 99879)

    def test_max_comp(self):
        self.assertEqual(maximum_comp(self.number)[1], 40824)

    def test_max_pos(self):
        self.assertEqual(maximum_comp(self.number)[2:], (364, 369))


class TestQueens(unittest.TestCase):

    def test_not_cross(self):
        figures = [[1, 7], [2, 4], [3, 2], [4, 8], [5, 6], [6, 1], [7, 3], [8, 5]]
        self.assertEqual(queens(figures), 'Ферзи нигде не пересекаются')

    def test_cross(self):
        figures = [[1, 7], [2, 6], [3, 2], [4, 8], [5, 4], [6, 1], [7, 3], [8, 5]]
        self.assertEqual(queens(figures), 'Ферзи бью друг друга')

    def test_not_cross2(self):
        figures = [[3, 2], [5, 6], [1, 7], [4, 8], [2, 4], [6, 1], [7, 3], [8, 5]]
        self.assertEqual(queens(figures), 'Ферзи нигде не пересекаются')

    def test_cross2(self):
        figures = [[1, 8], [2, 4], [3, 2], [4, 8], [5, 6], [6, 1], [7, 3], [8, 5]]
        self.assertEqual(queens(figures), 'Ферзи бью друг друга')





if __name__ == 'main':
    unittest.main()