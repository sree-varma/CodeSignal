"""
Given an array of integers, find the pair of adjacent elements 
that has the largest product and return that product.
"""
def adjacentElementsProduct(inputArray):
    prod=[]
    for i in range(len(inputArray)-1):
        prod.append(inputArray[i]*inputArray[i+1])
    return max(prod)
