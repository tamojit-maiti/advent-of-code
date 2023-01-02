from pathlib import Path

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / 'data'
FILE_NAME = 'day_3.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Helper functions
def get_score(letter: str):
    if letter.isupper():
        return ord(letter) - 38
    if letter.islower():
        return ord(letter) - 96

def get_common(left: str, *kwargs):
    left_set = set(left)
    for arg in kwargs:
        common_set = left_set.intersection(set(arg))
        left_set = common_set
    common_list = list(left_set)
    return common_list

def get_split(line: str):
    n = len(line)
    left = line[0:int(n/2)]
    right = line[int(n/2):]

    return left, right
    
# Reading file
priority_sum = 0
with open(DATA_FILE_PATH) as f:
    for line in f:
        line = line.strip()
        left, right = get_split(line = line)
        common_list= get_common(left, right)
        priority_sum += sum([get_score(i) for i in common_list])

# Answer to Part I
print(priority_sum)

# Reading file
priority_sum = 0
list_of_three = []
with open(DATA_FILE_PATH) as f:
    for line in f:
        line = line.strip()
        list_of_three.append(line)
        if len(list_of_three)==3:
            common_list = get_common(list_of_three[0], *list_of_three[1:])
            priority_sum += sum([get_score(i) for i in common_list])
            list_of_three = []

# Answer to Part II
print(priority_sum)        