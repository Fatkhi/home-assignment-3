# -*- coding: utf-8 -*-

import unittest
import math

from calculator import Calculator


class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

#	add       

    def testAdd(self):
        self.assertEqual(10, self.calculator.add(3, 7))

    def testAddNegative(self):
        self.assertEqual(0, self.calculator.add(10, -10))

    def testAddDecimal(self):
        self.assertEqual(1, self.calculator.add(.5, .5))

    def testAddStringWithNumber(self):
        self.assertEqual(3, self.calculator.add('1', 2))

    def testAddExp(self):
        self.assertEqual(10.2, self.calculator.add('1e1', .2))

    def testAddRandomString(self):
        self.assertEqual('error', self.calculator.add('1e1asfasf', .2))

#	subtract

    def testSubtract(self):
        self.assertEqual(0, self.calculator.subtract(10, 10))

    def testSubtractNegative(self):
        self.assertEqual(-17, self.calculator.subtract(-3, 14))

    def testSubtractDecimal(self):
        self.assertEqual(.4, self.calculator.subtract(.7, .3))

    def testSubtractStringWithNumber(self):
        self.assertEqual(10, self.calculator.subtract('13', 3))

    def testSubtractExp(self):
        self.assertEqual(0, self.calculator.subtract('1e1', 10))

    def testSubtractRandomString(self):
        self.assertEqual('error', self.calculator.subtract('13lasfkllklaskf', 3))

#	multiply        

    def testMultiply(self):
        self.assertEquals(0, self.calculator.multiply(5, 0))

    def testMultiplyNegative(self):
        self.assertEquals(-12, self.calculator.multiply(3, -4))

    def testMultiplyDecimal(self):
        self.assertEquals(1, self.calculator.multiply(.1, 10))

    def testMultiplyStringWithNumber(self):
        self.assertEquals(30, self.calculator.multiply('10', 3))

    def testMultiplyExp(self):
        self.assertEquals(1e3, self.calculator.multiply(1e2, 10))

    def testMultiplyRandomString(self):
        self.assertEquals('error', self.calculator.multiply('hi', 'there'))

#	divide

    def testDivide(self):
        self.assertEquals(5, self.calculator.divide(10, 2))

    def testDivideNull(self):
        self.assertRaises(ValueError, self.calculator.divide, 3, 0)

    def testDivideNegative(self):
        self.assertEquals(4, self.calculator.divide(-24, -6))

    def testDivideDecimal(self):
        self.assertEquals(100, self.calculator.divide(10, .1))

    def testDivideStringWithNumber(self):
        self.assertEquals(25, self.calculator.divide('100', 4))

    def testDivideExp(self):
        self.assertEquals(10, self.calculator.divide(1e2, 10))

    def testDivideRandomString(self):
        self.assertEquals('error', self.calculator.divide('hi', 'there'))

#	cos

    def testCosZero(self):
        self.assertEqual(1, self.calculator.cos(0))

    def testCosPi(self):
        self.assertEqual(-1, self.calculator.cos(math.pi))

    def testCosRange(self):
    	value = self.calculator.cos(1)
        self.assertLess(0, value)
        self.assertGreater(1, value)


