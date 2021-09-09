"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet;
i.e. replace a with b, replace b with c, etc (z would be replaced by a).
"""
def alphabeticShift(inputString):
    o=""
    for i in inputString:
        
        if ord(i)<122:
            o+=chr(ord(i)+1)
        if ord(i)==122:
            o+=chr(97)
        
    return o
