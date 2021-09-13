"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
"""
def deleteDigit(n):
    s=str(n)
    num=[]
    for i in range(len(s)):
        num.append(int(s[:i]+s[i+1:]))
    return(max(num))
