"""
You have deposited a specific amount of money into your bank account. 
Each year your balance increases at the same growth rate.
With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.
"""

def depositProfit(deposit, rate, threshold):
    y=0
    while deposit<threshold:
        deposit+=deposit*(rate/100)
        y+=1
    return y
