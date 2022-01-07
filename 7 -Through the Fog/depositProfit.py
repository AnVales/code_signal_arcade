# You have deposited a specific amount of money into your bank account. 
# Each year your balance increases at the same growth rate. 
# With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.

# Solution function
def solution(deposit, rate, threshold):

    # Gains benefit every time step
    for times in range(1000):
        deposit = deposit * (1 + (rate/100))
        if deposit >= threshold:
            return(times+1)
