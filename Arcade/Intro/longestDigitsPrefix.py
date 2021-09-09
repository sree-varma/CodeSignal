"""
Given a string, output its longest prefix which contains only digits.
"""
def longestDigitsPrefix(inputString):
    a=''
    for i in inputString:
        if i.isdigit()==True:
            a+=i
        else:
            break
    return a
        
