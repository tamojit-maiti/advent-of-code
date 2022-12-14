from pathlib import Path

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / 'data'
FILE_NAME = 'day_1.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Reading file
numbers_list = []
sum_numbers_list = []
with open(DATA_FILE_PATH) as f:
    for line in f:
        if line != '\n':
            numbers_list.append(int(line))
        else:
            sum_numbers_list.append(sum(numbers_list))
            numbers_list = []

# Answer to Part I
print(max(sum_numbers_list))

# Answer to Part II
print(sum(sorted(sum_numbers_list, reverse = True)[:3]))

