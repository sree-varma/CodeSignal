"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
"""
def addBorder(picture):
    l=len(picture[0])
    n='*'*(l+2)
    o=[n]
    for i in picture:
        o.append("*"+i+"*")
    o.append(n)
    return o    
    
