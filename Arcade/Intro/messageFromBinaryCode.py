"""
You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.
"""
def messageFromBinaryCode(code):
    i=0
    o=''
    while i<len(code):
        j=0
        d=0
        k=int(code[i:i+8])
        while k!=0:
            r=k%10
            d+=r*(2**j)
            k=k//10
            j+=1
        i+=8
        o+=chr(decimal)
    return o
