from pathlib import Path

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_4.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

count_1 = 0
count_2 = 0
# Reading the data
with open(DATA_FILE_PATH) as f:
    for line in f:
        left_area = line.split(',')[0]
        right_area = line.split(',')[1]
        left_set = set([i for i in range(int(left_area.split('-')[0]), 
                                            int(left_area.split('-')[1]) + 1)])
        right_set = set([i for i in range(int(right_area.split('-')[0]), 
                                            int(right_area.split('-')[1]) + 1)])
        if (right_set.issubset(left_set)) or (left_set.issubset(right_set)):
            count_1 += 1
        if len(right_set.intersection(left_set))>0:
            count_2 += 1

# Answer to Part I
print(count_1)

# Answer to Part II
print(count_2)