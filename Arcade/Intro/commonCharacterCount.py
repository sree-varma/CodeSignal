"""
Given two strings, find the number of common characters between them.
"""
def commonCharacterCount(s1, s2):
    count=0
    for i in s1:
        if i in s2:
            count+=1
            r = s2.index(i)
            s2=s2[:r]+s2[r+1:]
            
    return count



