"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.
"""
def variableName(name):
    special_characters = {' ','~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',  '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}

    
    if name[0].isdigit()==True:
        
        return False
    for n in name:
        
        if n in special_characters:
            return False
    return True
