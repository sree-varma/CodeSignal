"""
You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other. What is the value of the third integer?
"""

def extraNumber(a, b, c):
    return a^b^c
def extraNumber(a, b, c):
    for i in [a,b,c]:
        if [a,b,c].count(i)==1:
            return i
def extraNumber(a, b, c):
    if a!=b and a!=c:
        return a

    if b!=a and b!=c:
        return b
    if c!=a and c!=b:
        return c
