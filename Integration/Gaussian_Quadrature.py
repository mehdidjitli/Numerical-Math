#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 00:20:57 2023

@author: mehdidjitli
"""
import numpy as np

#Function to integer with Gaussian-Quadrature

def f(x):
    y=x**2
    return y

##a and b are the lower and upper bound of the integral of f(x), n is the number of points for the Gaussian-Quadrature

def quadrature(a,b,n):
    if n==1:
        I=f(0)*2
    elif n==2:
        I=(f((-np.sqrt(3)/3)*(b-a)/2+(b+a)/2))+f((np.sqrt(3)/3)*(b-a)/2+(b+a)/2)
    elif n==3:
        I=(5/9)*f((-np.sqrt(15)/5)*(b-a)/2+(b+a)/2)+(8/9)*f(0*(b-a)/2+(b+a)/2)+(5/9)*f((np.sqrt(15)/5)*(b-a)/2+(b+a)/2)
    else:
        print("pas 1 ou 2 ou 3")
    return I*(b-a)/2 # Integral value

quad=quadrature(1,2,3)
print(quad)

