# -*- coding: utf-8 -*-
"""Unit tests for custom math library.

Todo:
    -more tests?

Example:
    $ python3 -m unittest mathlib_unittest
    
    OR

    $ make test

Author:
    Denis Dzíbela xdzibe00
"""
import unittest
import math_lib

class TestBasicOperations(unittest.TestCase):
    """Test suite to test basic math operators (+,-,*,/)"""

    def test_addition(self):
        #basic function
        self.assertEqual(math_lib.add(20, 30), 50)
        self.assertEqual(math_lib.add(0.5, .5), 1)

        #commutativity
        self.assertEqual(math_lib.add(42, 69), math_lib.add(69, 42))
        
        #associativity
        # 10+(456+789)==(10+456)+789
        self.assertEqual(math_lib.add(10, math_lib.add(456, 789)), math_lib.add(math_lib.add(10, 456), 789))

        #identity element
        self.assertEqual(math_lib.add(456, 0), 456)
        self.assertEqual(math_lib.add(0, 12789), 12789)

    def test_subtraction(self):
        #basic function
        self.assertEqual(math_lib.sub(456, 6), 450)
        self.assertEqual(math_lib.sub(754298, 754298), 0)
        self.assertEqual(math_lib.sub(4569823, 0), 4569823)

    def test_multiplication(self):
        self.assertEqual(math_lib.mul(5, 10), 50)
        self.assertEqual(math_lib.mul(1, 0.5), 0.5)
        
        #commutativity
        self.assertEqual(math_lib.mul(5, 10), math_lib.mul(10, 5))
        
        #associativity
        #10*(5*2)==(10*5)*2
        self.assertEqual(math_lib.mul(10, math_lib.mul(5, 2)), math_lib.mul(math_lib.mul(10, 5), 2))

        #distributivity
        #4*(8+3)==4*11
        self.assertEqual(math_lib.mul(4, math_lib.add(8, 3)), math_lib.mul(4, 11))

        #identity elemt
        self.assertEqual(math_lib.mul(7896543210, 1), 7896543210)

        #times 0
        self.assertEqual(math_lib.mul(261594873123, 0), 0)
    
    def test_division(self):
        #basic function
        self.assertEqual(math_lib.div(5, 2), 2.5)
        
        #identity element
        self.assertEqual(math_lib.div(48159, 1), 48159)
        
        #divide by 0
        self.assertRaises(ZeroDivisionError, math_lib.div, 42, 0)

class TestAdvancedOperations(unittest.TestCase):
    """Test suite to test advanced operations (1,^,ROOT,...)"""
    def test_factorial(self):
        self.assertEqual(math_lib.fact(0), 1)
        self.assertEqual(math_lib.fact(1), 1)
        self.assertEqual(math_lib.fact(5), 120)

        #only defined for positive integers
        self.assertRaises(ValueError, math_lib.fact, 10.5)
        self.assertRaises(ValueError, math_lib.fact, -10)
        self.assertRaises(ValueError, math_lib.fact, -10.5)

    def test_exponent(self):
        #test 0 ^ 0
        self.assertEqual(math_lib.exp(0, 0), 1)

        #test n ^ 0
        self.assertEqual(math_lib.exp(500, 0), 1)
        self.assertEqual(math_lib.exp(-423, 0), 1)

        #basic function
        self.assertEqual(math_lib.exp(500, 2), math_lib.mul(500, 500))
        self.assertEqual(math_lib.exp(-500, 2), math_lib.mul(500, 500))
        self.assertAlmostEqual(math_lib.exp(5, -3), 0.008)

        #root extraction
        self.assertEqual(math_lib.exp(4, 0.5), 2)
        self.assertRaises(ValueError, math_lib.exp, -4, 0.5)
        self.assertAlmostEqual(math_lib.exp(-8, 0.33), -2)

    def test_root_exttraction(self):
        #basic function
        self.assertEqual(math_lib.ext(4, 2), 2)
        self.assertEqual(math_lib.ext(8, 3), 2)
        self.assertAlmostEqual(math_lib.ext(11.313708499, 3.5), 2.000000) #add more zeroes for arbitrary precision

        #even root of negative number
        self.assertRaises(ValueError, math_lib.ext, -4, 2)
        self.assertRaises(ValueError, math_lib.ext, -126, 10)

        #odd root of negative number
        self.assertAlmostEqual(math_lib.ext(-8, 3), -2)
        self.assertAlmostEqual(math_lib.ext(-243, 5), -3)

    def test_abs(self):
        self.assertEqual(math_lib.abs(0), 0)
        self.assertEqual(math_lib.abs(-1357), 1357)
        self.assertEqual(math_lib.abs(456), math_lib.abs(-456))


if __name__ == '__main__':
    unittest.main()