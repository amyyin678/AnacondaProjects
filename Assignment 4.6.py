#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 19:33:35 2017

@author: amyyin
"""

#Python for Everybody Assignment 4.6
def computepay(h,r):
    if h>40:
        pay=(40*r)+((h-40)*r*1.5)
    else:
        pay=(h*r)
    return pay

h = input("Enter Hours:")
hours = float(h)
r = input("Enter Rate:")
rate = float(r)
print(computepay(hours, rate))