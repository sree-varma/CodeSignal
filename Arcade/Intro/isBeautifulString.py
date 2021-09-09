"""
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.
"""
def isBeautifulString(inputString):
    o=sorted([ord(i) for i in inputString])
    for i in range(1,len(o)):
        
        if o.count(o[i-1])<o.count(o[i]):
            return False
        if o[i]!=97 and o[i]-1  not in o:
            return False
            
    return True

