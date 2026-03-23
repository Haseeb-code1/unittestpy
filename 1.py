import unittest
from calcul import calculator
class Test_Calculator(unittest.TestCase):
    def setUp(self):
        self.cal=calculator()

    def tearDown(self):
        del self.cal
    def test_Add_positiveValues(self):

        self.assertEqual(self.cal.add(1, 2), 3)

    def test_subtract_positiveValues(self):

        self.assertEqual(self.cal.subtract(1, 2), -1)

    def test_divide_positiveValues(self):

        self.assertEqual(self.cal.divide(10,5),2)
    def test_multiplyPositiveValues(self):

        self.assertEqual(self.cal.multiply(10,4),40)