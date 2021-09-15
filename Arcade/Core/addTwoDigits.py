"""
You are given a two-digit integer n. Return the sum of its digits.
"""
def addTwoDigits(n):
    return sum([int(i) for i in str(n)])
def addTwoDigits(n):
    return (n%10+n//10)
def addTwoDigits(n):
    a=0
    while n>0:
        a+=n%10
        n=n//10
    return a
