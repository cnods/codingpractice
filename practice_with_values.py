
# Take a dictionary with scores and names and decide who has the
# highest average score.

def find_winner(scores):
    highest_avg = 0
    highest_avg_player = ""
    for player, scores in scores.items():
        avg = sum(scores) / len(scores)
        if avg > highest_avg:
            highest_avg = avg
            highest_avg_player = player
    return [highest_avg_player, highest_avg]


player_scores = {
    "Arthur": [85,90,92],
    "Bela": [75, 80, 85],
    "Carol": [90, 92, 95],
    "Deepak": [87, 89,91]
}

result = find_winner(player_scores)
print(result)