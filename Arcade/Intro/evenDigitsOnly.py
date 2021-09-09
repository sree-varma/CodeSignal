"""
Check if all digits of the given integer are even.
"""
def evenDigitsOnly(n):
    num=[int(i) for i in str(n)]
    for i in num:
        if i%2!=0:
            return False
    return True

