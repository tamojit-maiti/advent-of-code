from pathlib import Path
import numpy as np

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2021' / 'data'
FILE_NAME = 'day_1_test.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Reading the data
numbers_list = []
with open(DATA_FILE_PATH) as f:
    for line in f:
        numbers_list.append(int(line))

count = 0
for i in range(len(numbers_list) - 1):
    if (numbers_list[i] - numbers_list[i+1]) < 0:
        count += 1
    
# Answer to Part I
print(count)

count = 0
k = 3
for i in range(len(numbers_list) - k):
    if (sum(numbers_list[i:i+k]) - sum(numbers_list[i+1:i+k+1])) < 0:
        count += 1
    
# Answer to Part II
print(count)
