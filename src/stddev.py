# -*- coding: utf-8 -*-
"""
Standard deviation calculator - profiling
IVS Project 2
Author : Richard Míček (xmicek09)
Date : 16.4.2020
"""
import math_lib as math
import fileinput

num_array = ''
count = 0
average = 0
summ = 0

for line in fileinput.input():
    """Reads the standard input and parses it into an array
    """
    line.rstrip()
    num_array += line

num_array = num_array.split('\n')
num_array = [int(i) for i in num_array]
"""Converts the array from str to int
"""

for num in num_array:
    """Counting the average needed for the standard deviation calculation
    """
    average = math.add(average, num)
    count = math.add(count, 1)

average = math.div(average, count)

for num in num_array:
    """Counting the sum needed for the standard deviation calculation
    """
    summ = math.add(summ, math.exp(math.sub(num, average), 2))
    
deviation = math.ext(math.mul(math.div(1, (count - 1)), summ), 2)
"""Calculating the standard deviation
"""
print(deviation)