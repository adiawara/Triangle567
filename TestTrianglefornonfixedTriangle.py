# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""

import unittest         # calling on test case

import Triangle

from Triangle import *


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        try:
            self.assertEqual(Triangle.classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
            self.assertEqual(Triangle.classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        except:
            print("Test Failed")
        else: print(Triangle.classifyTriangle(3,4,5))

    #def testRightTriangleB(self): 
        #self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self):
        try:
            self.assertEqual(Triangle.classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        except:
            print("Test Failed")
        else:print(Triangle.classifyTriangle(1,1,1))

    def testIsoscelesTriangles(self):
        try:
            self.assertEqual(Triangle.classifyTriangle(4,5,5),'Isosceles','4,5,5 should be isosceles')
        except:
            print("Test Failed")
        else: print(Triangle.classifyTriangle(4,5,5))

    def testScaleneTriangles(self):
        try:
            self.assertEqual(Triangle.classifyTriangle(7,8,9),'Scalene','7,8,9 should be scalene')
        except:
            print("Test Failed")
        else: print(Triangle.classifyTriangle(7,8,9))

    def testIllegalTriangle(self):
        try:
            self.assertEqual('NotATriangle', Triangle.classifyTriangle(9, 2, 5))
        except:
            print("Test Failed")
        else: print(Triangle.classifyTriangle(9,2,5))

    def testInvalidInput_1(self):
        try:
            self.assertEqual('InvalidInput', Triangle.classifyTriangle(-1,- 1, -1))
        except:
            print("Test Failed")
        else: print(Triangle.classifyTriangle(-1, -1, -1))

    def testInvalidInput_2(self):
        try:
            self.assertEqual('InvalidInput', Triangle.classifyTriangle(0, 0, 0))
        except:
            print("Test Failed")
        else: print(Triangle.classifyTriangle(0,0,0))

    def testInvalidInput_3(self):
        try:
            self.assertEqual('InvalidInput', Triangle.classifyTriangle(8, 6, -10))
        except:
            print("Test Failed")
        else:print(Triangle.classifyTriangle(8,6, -10))
    def testInvalidInput_4(self):
        try:
            self.assertEqual('InvalidInput', Triangle.classifyTriangle(1, 1, 0))
        except:
            print("Test Failed")
        else: print(Triangle.classifyTriangle(1,1,0))

    def testInvalidInput_5(self):
        try:
            self.assertEqual('InvalidInput', Triangle.classifyTriangle(m, n, o))
        except:
            print("Test Failed")
        else: print(Triangle.classifyTriangle(m,n,o))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
