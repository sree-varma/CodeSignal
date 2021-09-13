"""
Determine if the given character is a digit or not.
"""
def isDigit(symbol):
    # if symbol.isdigit()==True:
    #     return True
    # else:
    #     return False
    if ord(symbol)<48 or ord(symbol)>57:
        return False
    return True
