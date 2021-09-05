"""
Given a year, return the century it is in. 
The first century spans from the year 1 up to and including the year 100, 
the second - from the year 101 up to and including the year 200, etc.
"""
def centuryFromYear(year):
    if year-(year%100)>year:
        return (year-(year%100))/100-1
    if year-(year%100)==year:
        return (year/100)
    else:
        return (year-(year%100))/100+1
        
