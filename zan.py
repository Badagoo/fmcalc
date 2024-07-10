'''
Name: Functions
Author: Zan Gikovski
Input: cakeShape, cakeRadius, cakeLength, cakeWidth, cakeHeight, cakePortion
Output: cakeVolume, servingAmount

This module stores the functions
'''

import math


###########################
'''
Name: calcServing
Author: Zan Gikovski
Input: cakeShape, cakeRadius, cakeLength, cakeWidth, cakeHeight, cakePortion
Output: servingAmount
Purpose: To calculate the amount of portions from an inputted cake size
'''

#User enters cake shape, serving size
def calcServing(cakeShape=0, cakeRadius=0, cakeLength=0, cakeWidth=0, cakeHeight=0, cakePortion=0):
    if cakeShape == 1: ### 1 refers to Circular base
        cakeVolume = math.pi * cakeRadius ** 2 * cakeHeight #pi * radius^2 * height
        servingAmount = cakeVolume / cakePortion
        return servingAmount
    if cakeShape == 2: ### 2 refers to Rectangular base
        cakeVolume = cakeLength * cakeWidth * cakeHeight #Length * Width * Height
        servingAmount = cakeVolume / cakePortion
        return servingAmount
    
sampleInputCircle = {"cakeShape": 1, "cakeRadius": 5, "cakeHeight": 10, "cakePortion": 2}

sampleCircle = calcServing(**sampleInputCircle)
sampleRect = calcServing(cakeShape=2, cakeLength=5, cakeWidth=5, cakeHeight=10, cakePortion=2)
print(sampleCircle)
print(sampleRect)