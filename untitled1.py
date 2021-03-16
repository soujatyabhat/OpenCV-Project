# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:02:16 2020

@author: Sourick
"""

sum = 0
a = int(input())
for i in range (1,a+1):
    if a % i == 0:
        print(i)
        sum += 1

print(sum)