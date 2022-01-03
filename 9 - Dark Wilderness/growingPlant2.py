# Caring for a plant can be hard work, but since you tend to it regularly, 
# you have a plant that grows consistently. 
# Each day, its height increases by a fixed amount represented by the integer upSpeed. 
# But due to lack of sunlight, the plant decreases in height every night, by an amount represented by downSpeed.

# Since you grew the plant from a seed, it started at height 0 initially. 
# Given an integer desiredHeight, your task is to find how many days it'll take for the plant to reach this height.

# Day growth function
def day(height, upSpeed):
    height = height + upSpeed
    return height

# Night growth function
def night(height, downSpeed):
    height = height - downSpeed
    return height

# Function that shows when the plant grows on the desired day.
def solution(upSpeed, downSpeed, desiredHeight):
    
    # Initialise variable
    height = 0
    days = 0

    while height < desiredHeight:
        height = day(height, upSpeed)
        if  height < desiredHeight:
            height = night(height, downSpeed)
            days = days + 1

    return days+1

