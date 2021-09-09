"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
"""
def arrayMaximalAdjacentDifference(inputArray):
    o=[]
    for i in range(1,len(inputArray)):
        o.append(abs(inputArray[i-1]-inputArray[i]))
    return max(o)
