"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network
that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses.
One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.
"""
def isIPv4Address(inputString):
    b=[i for i in inputString]
    if '.' not in b:
        return False
    
    a=inputString.split('.')
    
    print(a)
    
    if len(a)!=4:
        return False
    if "" in a:
        return False
        
    for i in a:
        
        if i.isnumeric()==False:
            return False
        
        if int(i)>255:
            return False
        
        if i[0]=='0' and len(i)>1:
            
            return False
    return True
