# -*- coding: utf-8 -*-
"""Unit tests for custom math library.

Todo:
    -replace placeholder mathlib name with final name
    -more tests?

Usage:
    $ python -m unittest mathlib_unittest
    
    OR

    $ make test

Author:
    Denis Dzíbela xdzibe00
"""
import unittest
import mathlib_placeholder #<- placeholder, change to final name later

class TestBasicOperations(unittest.TestCase):
    """Test suite to test basic math operators (+,-,*,/)"""

    def test_addition(self):
        #basic function
        self.assertEqual(mathlib_placeholder.add(20, 30), 50)

        #commutativity
        self.assertEqual(mathlib_placeholder.add(42, 69), mathlib_placeholder.add(69, 42))
        
        #associativity
        # 10+(456+789)==(10+456)+789
        self.assertEqual(mathlib_placeholder.add(10, mathlib_placeholder.add(456, 798)), mathlib_placeholder.add(mathlib_placeholder.add(10, 456), 789))

        #identity element
        self.assertEqual(mathlib_placeholder.add(456, 0), 456)
        self.assertEqual(mathlib_placeholder.add(0, 12789), 12789)

    def test_subtraction(self):
        #basic function
        self.assertEqual(mathlib_placeholder.sub(456, 6), 450)
        self.assertEqual(mathlib_placeholder.sub(754298, 754298), 0)
        self.assertEqual(mathlib_placeholder.sub(4569823, 0), 4569823)

    def test_multiplication(self):
        self.assertEqual(mathlib_placeholder.mul(5, 10), 50)
        
        #commutativity
        self.assertEqual(mathlib_placeholder.mul(5, 10), mathlib_placeholder.mul(10, 5))
        
        #associativity
        #10*(5*2)==(10*5)*2
        self.assertEqual(mathlib_placeholder.mul(10, mathlib_placeholder.mul(5, 2)), mathlib_placeholder.mul(mathlib_placeholder.mul(10, 5), 2))

        #distributivity
        #4*(8+3)==4*11
        self.assertEqual(mathlib_placeholder.mul(4, mathlib_placeholder.add(8, 3)), mathlib_placeholder.mul(4, 11))

        #identity elemt
        self.assertEqual(mathlib_placeholder.mul(7896543210, 1), 7896543210)

        #times 0
        self.assertEqual(mathlib_placeholder.mul(261594873123, 0), 0)
    
    def test_division(self):
        #basic function
        self.assertEqual(mathlib_placeholder.div(5, 2), 2.5)
        
        #identity element
        self.assertEqual(mathlib_placeholder.div(48159, 1), 48159)
        
        #divide by 0
        self.assertRaisesRegex(mathlib_placeholder.div(420, 0), "*")

class TestAdvancedOperations(unittest.TestCase):
    """Test suite to test advanced operations (1,^,ROOT,...)"""


if __name__ == '__main__':
    unittest.main()