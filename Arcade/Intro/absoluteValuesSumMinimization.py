"""
Given a sorted array of integers a, 
your task is to determine which element of a is closest to all other values of a. 
In other words, find the element x in a, which minimizes the following sum:
abs(a[0] - x) + abs(a[1] - x) + ...
"""
def absoluteValuesSumMinimization(a):
    s=[]
    for i in a:
        summ=[abs(j-i) for j in a]
        s.append(sum(summ))
    
    return a[s.index(min(s))]
