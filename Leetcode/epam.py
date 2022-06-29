def find_winner(votes):
    voting = {}
    winner = []
    max_votes = 0
    for i in votes:
        if i not in voting.keys():
            voting[i] = 1
        else:
            voting[i] += 1
        # max_votes = max(max_votes, voting[i])
        if voting[i] > max_votes:
            max_votes = voting[i]
            winner = [i]
        elif voting[i] == max_votes:
            winner.append(i)

    return winner


print(find_winner(['A', 'B', 'C', 'A', 'B', 'D', 'A', 'B']))
""""
63,02,458.35
72,44,205.00
76,78,857.30

1,35,46,663
"""

print(5)