"""
Given a string, find out if its characters can be rearranged to form a palindrome.
"""
def palindromeRearranging(inputString):
    o=[inputString.count(i)%2 for i in set(inputString)]
    
    if (sum(o))<=1:
        
        return True
    return False
