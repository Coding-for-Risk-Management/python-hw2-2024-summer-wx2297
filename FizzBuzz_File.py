#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:18:48 2024

@author: muxilin
"""

import numpy as np

def FizzBuzz(start, finish):
    # Create a range of numbers
    numvec = np.arange(start, finish + 1)
    
    # Create an object array of the same shape
    objvec = np.array(numvec, dtype=object)
    
    # Apply FizzBuzz conditions using np.mod
    fizzbuzz_mask = (np.mod(numvec, 3) == 0) & (np.mod(numvec, 5) == 0)
    fizz_mask = (np.mod(numvec, 3) == 0) & ~fizzbuzz_mask
    buzz_mask = (np.mod(numvec, 5) == 0) & ~fizzbuzz_mask
    
    objvec[fizzbuzz_mask] = 'fizzbuzz'
    objvec[fizz_mask] = 'fizz'
    objvec[buzz_mask] = 'buzz'
    
    return objvec

# Test the function
start = 1
finish = 15
result = FizzBuzz(start, finish)
print(result)
