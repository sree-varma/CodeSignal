"""
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.
"""

def digitDegree(n):
   
    if sum([int(i) for i in str(n)])==n:
        return 0
    count=1
    
    
    while n%10>0:
        n=sum([int(i) for i in str(n)])
        count+=1
        if n<10:
            return count-1
    return count
        


