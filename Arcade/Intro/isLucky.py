"""
Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.
"""
def isLucky(n):
    
    num=[int(i) for i in str(n)]
    if len(num)%2!=0:
        return False
    l=int(len(num)/2)
    
    if sum(num[:l])==sum(num[l:]):
        return True
    return False
