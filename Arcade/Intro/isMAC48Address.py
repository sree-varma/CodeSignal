"""
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.
"""
def isMAC48Address(inputString):
    if inputString.count('-')!=5:
        return False
    
    if len(inputString)!=17:
        return False
    
    
    
    for i in inputString:
        
        if ord(i)==45:
            continue
        
        if ord(i)<48 or (ord(i)>57 and ord(i)<65):
            return False
        if ord(i)>70:
            return False
    return True


