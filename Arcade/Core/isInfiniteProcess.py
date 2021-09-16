"""
Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.
"""


def isInfiniteProcess(a, b):
    
    if a>b:
        return True
    
    if a<b:
        while a!=b:
            if a>b:
                return True
                
            a+=1
            b-=1
                    
         
        
    return False

def isInfiniteProcess(a, b):
    return ((b-a)%2==1) or a>b
