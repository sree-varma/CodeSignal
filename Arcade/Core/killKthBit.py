"""
In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. The message contains several numbers that, when typed into a supercomputer, will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.

You figured out that some numbers have a modified single digit in their binary representation. More specifically, in the given number n the kth bit from the right was initially set to 0, but its current value might be different. It's now up to you to write a function that will change the kth bit of n back to 0.
"""

def killKthBit(n, k):
    return n -2**(k-1) if n & 2**(k-1) else n
def killKthBit(n, k):   
  o=[]
    m=n
    
    if n==0:
        return 0
    while n>0:
        o.append(n%2)
        n//=2
    
    if o[(k-1)]==0:
        return m
    else:
        o[(k-1)]=0
        
        print(o)
        
        s=0
        c=0
        for i in o:
            s+=i*2**c
            c+=1
        return s

