from pathlib import Path
import numpy as np
import pandas as pd

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2024' / 'data'
FILE_NAME = 'day_01.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Reading file
list_A = []
list_B = []
with open(DATA_FILE_PATH) as f:
    for line in f:
        if line != '\n':
            a,b = int(line.split(' ')[0]), int(line.split(' ')[-1])
            list_A.append(a)
            list_B.append(b)

# Part I
array_A = np.array(list_A)
array_B = np.array(list_B)

array_A.sort()
array_B.sort()

array_diff = np.abs(array_A - array_B)
array_diff_sum = np.sum(array_diff)

# Answer to Part I
print(array_diff_sum)

# Part II
value_counts = pd.Series(array_B).value_counts()
sum_total = 0
for i in array_A:
    if i in value_counts.keys():
        sum_total += i*value_counts[i]

# Answer to Part II
print(sum_total)
        