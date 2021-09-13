"""
Elections are in progress!

Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.


"""
def electionsWinners(votes, k):
    count=0
    i=0
    maxx=max(votes)
    while i<len(votes):
        
        if k>0 and k+votes[i]>maxx:
            count+=1
       
        if k==0 and votes[i]==maxx and votes.count(votes[i]==1:
            count+=1
        i+=1
        
    return count
    

