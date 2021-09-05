"""
Given an array of strings, return another array containing all of its longest strings.
"""
def allLongestStrings(inputArray):
    o=[len(i) for i in inputArray]
    return [inputArray[i] for i, j in enumerate(o) if j == max(o)]
