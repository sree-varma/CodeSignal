"""
Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
"""

def maxMultiple(divisor, bound):
    while bound>0:
        if bound%divisor==0:
            return bound
        bound-=1
