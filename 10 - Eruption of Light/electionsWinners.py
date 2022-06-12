# Elections are in progress!
#Given an array of the numbers of votes given to each of the candidates so far, 
# and an integer k equal to the number of voters who haven't cast their vote yet, 
# find the number of candidates who still have a chance to win the election.

#The winner of the election must secure strictly more votes than any other candidate. 
# If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.

def solution(votes, k):

    # Parameter initialization
    votes_final = []
    max_actual = 0
    winner = 0

    # If everyone has voted:
    if k == 0:
        votes.sort()
        if votes[len(votes)-1] == votes[len(votes)-2]:
            return 0
        else:
            return 1
        
    # Find the maximun number of votes per candidate and the maximun number of votes in this moment
    for number in votes:

        votes_final.append(number+k)

        if number > max_actual:
            max_actual = number

    # When someone has the possibility of win, add 1
    for number in votes_final:
        if number > max_actual:
            winner = winner + 1

    return winner