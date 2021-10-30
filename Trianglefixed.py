# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        #return 'InvalidInput'
        print("InvalidInput")
        
    if a <= 0 or b <= 0 or c <= 0:          #5th error fixed
        #return 'InvalidInput'
        print("InvalidInput")
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        #return 'InvalidInput';
        print("InvalidInput")
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):                      #error to rectify
        return 'NotATriangle'
        #print("NotATriangle")
        
    # now we know that we have a valid triangle 
    if a == b and b == c:                                                                   # 2nd error fixed
        return 'Equilateral'
        #print("Equilateral")
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) or ((c ** 2) + (b ** 2)) == (a ** 2):
        print("Right")
        #return 'Right'
    elif (a != b) and  (b != c) and (a != c):                                       # 4th error
        #return 'Scalene'
        print("Scalene")
    else:
        return print("Isosceles") #'Isosceles'

#classifyTriangle(3,4,5)
#classifyTriangle(3,3,3)
#classifyTriangle(3,4,4)
#classifyTriangle(7,8,9)
#classifyTriangle(7,8,0)
#classifyTriangle(300,8,9)
#classifyTriangle(30,8,9)
