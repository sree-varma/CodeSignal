"""
Given the string, check if it is a palindrome.
"""

def checkPalindrome(inputString):
    s=[i for i in inputString]
    if s[:]!=s[::-1]:
        return False
    return True
