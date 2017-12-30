import unittest
from circle import area_circle
from math import pi

class Test_area(unittest.TestCase):
    def test_area_pos_num(self):
        '''Test case for positive numbers with Zero
        '''
        self.assertAlmostEqual(area_circle(1),pi)
        self.assertAlmostEqual(area_circle(0),0)
        self.assertAlmostEqual(area_circle(5),pi*(5**2))
        self.assertAlmostEqual(area_circle(2.15),pi*(2.15**2))

    def test_area_neg_num(self):
        '''Test case for negative numbers
        '''
        self.assertRaises(ValueError,area_circle,-2)#Assuming that for -2 area_circle will raise ValueError

    def test_area_others(self):
        '''Test cases for other values of redius like True,False,"Any string",etc(except int and float)
        '''
        self.assertRaises(TypeError,area_circle,2+5j)
        self.assertRaises(TypeError,area_circle,True)
        self.assertRaises(TypeError,area_circle,False)
