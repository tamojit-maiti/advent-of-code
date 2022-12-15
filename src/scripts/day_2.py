from pathlib import Path

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / 'data'
FILE_NAME = 'day_2.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Dictionaries
opponent_dict = {
                'A':'Rock',
                'B':'Paper',
                'C':'Scissors'
            }
player_dict = {
                'X':'Rock',
                'Y':'Paper',
                'Z':'Scissors'
            }

player_score_dict = {
                'Rock':1,
                'Paper':2,
                'Scissors':3
            }

# Victory Map
victory_dict = {
                'Rock':['Scissors'],
                'Paper':['Rock'],
                'Scissors':['Paper']
                }

loss_dict = {
                'Rock':['Paper'],
                'Paper':['Scissors'],
                'Scissors':['Rock']
                }

victory_score_dict = {
                'draw':3,
                'lose':0,
                'win':6
                }
    
# Helper Functions
def game_outcome(opponent, player):
    if opponent == player:
        return 'draw'
    if opponent in victory_dict[player]:
        return 'win'
    else:
        return 'lose'

def game_score(opponent, player):
    score = 0
    score = score + player_score_dict[player]
    score = score + victory_score_dict[game_outcome(opponent=opponent, 
                                                    player=player)]
    return score

# Reading file
total_score = 0
with open(DATA_FILE_PATH) as f:
    for line in f:
        opponent = opponent_dict[line[0]]
        player = player_dict[line[2]]
        total_score += game_score(opponent=opponent, player=player)

# Answer to Part I
print(total_score)

# Dictionaries
outcome_dict = {
                'X':'lose',
                'Y':'draw',
                'Z':'win'
                }

def player_response(opponent, game_outcome):
    if game_outcome == 'draw':
        return opponent
    if game_outcome == 'win':
        return loss_dict[opponent][0]
    else:
        return victory_dict[opponent][0]
        
# Reading file
total_score = 0
with open(DATA_FILE_PATH) as f:
    for line in f:
        opponent = opponent_dict[line[0]]
        outcome_of_game = outcome_dict[line[2]]
        player_resp = player_response(opponent = opponent, 
                                        game_outcome = outcome_of_game)
        total_score += game_score(opponent=opponent, player=player_resp)

# Answer for Part 2
print(total_score)