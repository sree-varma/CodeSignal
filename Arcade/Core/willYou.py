"""
Once Mary heard a famous song, and a line from it stuck in her head. That line was "Will you still love me when I'm no longer young and beautiful?". Mary believes that a person is loved if and only if he/she is both young and beautiful, but this is quite a depressing thought, so she wants to put her belief to the test.

Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.

A person contradicts Mary's belief if one of the following statements is true:

they are young and beautiful but not loved;
they are loved but not young or not beautiful.

"""
def willYou(young, beautiful, loved):
    return loved != (young and beautiful)
  
def willYou(young, beautiful, loved):
    if young==beautiful==loved:
        return False
    if (young==True  and beautiful==True) and loved==False:
        
        return True
    if loved==True and (young==False or beautiful==False) :
        return True
    return False
