import random
def roll_dice():
    return random.randint(1,6)

while True:
    players = input('Enter number of players: ')
    if players in ['2','3','4']:
        players = int(players)
        break
    else:
        print('Invalid!')

threshold = 35
max_score = 0
all_scores = [0 for every_player in range(players)]
while max_score < threshold:
    for i in range(players):
        print('\nPlayer', i + 1, 'turn!')
        print('Your total score until now is', all_scores[i])
        turn_score = 0
        while True:
            again = input('Do you want to take turn? (y)')
            if again != 'y':
                break
            roll = roll_dice()
            if roll != 1:
                turn_score += roll
                print(turn_score)
            else:
                print('You rolled a 1! Turn Lost')
                turn_score = 0
                break
        all_scores[i] += turn_score
        print('Current score: ', all_scores[i])
    print(all_scores)
    max_score = max(all_scores)
winner = all_scores.index(max_score)
print('Player', winner + 1, 'wins!')