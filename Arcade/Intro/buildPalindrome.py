"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.
"""
def buildPalindrome(st):

    o = ""
    i = 0
    while st + o != (st + o)[::-1]:
        o = st[i] + o
        i+=1
    return st + o
