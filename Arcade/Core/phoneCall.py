"""
Some phone usage rate may be described as follows:

first minute of a call costs min1 cents,
each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
each minute after 10th costs min11 cents.
You have s cents on your account before the call. What is the duration of the longest call (in minutes rounded down to the nearest integer) you can have?
"""
def phoneCall(min1, min2_10, min11, s):
  
    if s<min1 and s<min2_10 and s<min11:
        return 0
      
    d=s-min1
    if d==0:
        return 1 # Talked  1 min
      
    i=2
    if d>0:
        
        while i<11: # For the next 10 mins
            
            d-=min2_10
            if d<=0:
                return i-1
            i+=1
    if d>0:
        while d>min11:
            
            d-=min11
            if d<min11:
                return i
            i+=1
        return i
