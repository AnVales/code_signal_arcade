# Call two arms equally strong if the heaviest weights they each are able to lift are equal.

# Call two people equally strong if their strongest arms are equally strong 
# (the strongest arm can be both the right and the left), and so are their weakest arms.

# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

# Solution function
def solution(yourLeft, yourRight, friendsLeft, friendsRight):

    # Make a sorted list with arms
    your_arms = [yourLeft, yourRight]
    your_arms = sorted(your_arms)

    friend_arms = [friendsLeft, friendsRight]
    friend_arms = sorted(friend_arms)

    return your_arms == friend_arms

