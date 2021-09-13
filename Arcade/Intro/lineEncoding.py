"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
"""

def lineEncoding(s):
    o=''
    c=1
    
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            c+=1
        else:
            if c>1:
                o+=str(c)+s[i-1]
            else:
                o+=s[i-1]
            c=1
    if c>1:
        o+=str(c)+s[i]
    else:
        o+=s[i]
    return o
            
            
