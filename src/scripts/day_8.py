from pathlib import Path
import numpy as np

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / 'data'
FILE_NAME = 'day_8.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

number_matrix = []

# Reading the data
with open(DATA_FILE_PATH) as f:
    
    for line in f:
        n_list = []
        for digit in line[:-1]:
            n_list.append(int(digit))
        number_matrix.append(n_list)

# Enter Numpy
number_matrix = np.array(number_matrix)
shadow_matrix_lr = np.zeros_like(number_matrix)
shadow_matrix_rl = np.zeros_like(number_matrix)
shadow_matrix_tb = np.zeros_like(number_matrix)
shadow_matrix_bt = np.zeros_like(number_matrix)

def is_visible(present, historical_max)-> bool:
    if present>historical_max:
        return True
    else:
        return False

def get_visible_elements(row : np.array, reverse : bool = False) -> np.array:
    if reverse:
        row = row[::-1]
    visible_elements = np.zeros_like(row)
    for i in range(len(row))[1:]:
        present = row[i]
        historical_max = max(row[:i])
        visible_elements[i] = is_visible(present, historical_max)
    visible_elements[0] = 1
    if reverse:
        visible_elements = visible_elements[::-1]
    return visible_elements

def process_shadow_matrix(shadow_matrix : np.array) -> np.array:
    shadow_matrix[0,:] = 1
    shadow_matrix[:,0] = 1
    shadow_matrix[-1,:] = 1
    shadow_matrix[:,-1] = 1
    return shadow_matrix

for i in range(len(number_matrix))[1:-1]:
    shadow_matrix_lr[i,:] = get_visible_elements(number_matrix[i,:])
    shadow_matrix_rl[i,:] = get_visible_elements(number_matrix[i,:], 
                                    reverse=True)
    shadow_matrix_tb[:,i] = get_visible_elements(number_matrix[:,i])
    shadow_matrix_bt[:,i] = get_visible_elements(number_matrix[:,i], 
                                    reverse=True)

shadow_matrix = process_shadow_matrix(shadow_matrix_bt 
                                        + shadow_matrix_tb 
                                        + shadow_matrix_rl 
                                        + shadow_matrix_lr)

# Answer to Part I
print(len(shadow_matrix[shadow_matrix>0]))

def get_score(present, historical):
    count = 0
    for past in historical[::-1]:
        count += 1
        if past>=present:
            break
        else:
            continue
    return count

def get_viewing_array(row : np.array, reverse: bool = False)-> np.array:
    if reverse:
        row = row[::-1]
    viewing_scores = np.zeros_like(row)
    for i in range(len(row))[1:-1]:
        present = row[i]
        historical = row[:i]
        viewing_scores[i] = get_score(present, historical)
    if reverse:
        viewing_scores = viewing_scores[::-1]
    return viewing_scores

score_matrix_lr = np.zeros_like(number_matrix)
score_matrix_rl = np.zeros_like(number_matrix)
score_matrix_tb = np.zeros_like(number_matrix)
score_matrix_bt = np.zeros_like(number_matrix)

for i in range(len(number_matrix))[1:-1]:
    score_matrix_lr[i,:] = get_viewing_array(number_matrix[i,:])
    score_matrix_rl[i,:] = get_viewing_array(number_matrix[i,:], 
                                    reverse=True)
    score_matrix_tb[:,i] = get_viewing_array(number_matrix[:,i])
    score_matrix_bt[:,i] = get_viewing_array(number_matrix[:,i], 
                                    reverse=True)

score_matrix = score_matrix_bt * score_matrix_tb * score_matrix_lr * score_matrix_rl

# Answer to Part II
print(np.max(score_matrix))
