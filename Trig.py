__author__ = 'dominics'

import math

x = 90

def degrees_to_radians(x):
#This function converts degrees to radians
    deg = x
    deg = float(deg)
    rad = math.pi * deg / 180
    return rad
    #NOTE THIS FUNCTION HAS BEEN TESTED TO BE CORRECT

def radians_to_degrees(x):
#This function converts radians to degrees
    rad = x
    rad = float(rad)
    deg = 180 * rad / math.pi
    return deg
    #NOTE THIS FUNCTION HAS BEEN TESTED TO BE CORRECT

def sine_func(x):
    sine = math.sin(degrees_to_radians(x))
    print sine

sine_func(x)