"""
Check if the given string is a correct time representation of the 24-hour clock.
"""
def validTime(time):
    s=time.split(':')
    
    if int(s[0])>=0 and int(s[0])<24:
        
        if int(s[1])>=0 and int(s[1])<60:
            
            return True
    return False
