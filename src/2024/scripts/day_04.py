from pathlib import Path
import numpy as np
import pandas as pd
import re

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2024' / 'data'
FILE_NAME = 'day_04.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Reading file
text_list = []
with open(DATA_FILE_PATH) as f:
    for line in f:
        text_list.append(line.strip('\n'))

# text_list = ['1234', '5678', '9012','3456']
nrows = len(text_list)
ncols = len(text_list[0])

ncount = 0

# Part I
## horizontal
for i in text_list:
    matches = re.findall(pattern = r"(XMAS)", string=i)
    reverse_matches = re.findall(pattern = r"(XMAS)", string=i[::-1])
    ncount += len(matches) + len(reverse_matches)
## vertical
v_text_list = []
for col_id in range(len(text_list)):
    row_element = ''
    for row_id in range(len(text_list[col_id])):
        row_element += text_list[row_id][col_id]
    v_text_list.append(row_element)
for i in v_text_list:
    matches = re.findall(pattern = r"(XMAS)", string=i)
    reverse_matches = re.findall(pattern = r"(XMAS)", string=i[::-1])
    ncount += len(matches) + len(reverse_matches)

## Main Diagonal
md_text_list = []
for row_id in range(1,len(text_list)):
    diag_element = ''
    for k in range(len(text_list) - row_id):
        diag_entry = text_list[row_id + k][k]
        diag_element += diag_entry
    md_text_list.append(diag_element)
for col_id in range(1,len(text_list[0])):
    diag_element = ''
    for k in range(len(text_list) - col_id):
        diag_entry = text_list[k][col_id + k]
        diag_element += diag_entry
    md_text_list.append(diag_element)
md_text_list.append(''.join([text_list[i][i] for i in range(len(text_list))]))
## Non-main Diagonal
reverse_text_list = [i[::-1] for i in text_list]
nmd_text_list = []
for row_id in range(1,len(reverse_text_list)):
    diag_element = ''
    for k in range(len(reverse_text_list) - row_id):
        diag_entry = reverse_text_list[row_id + k][k]
        diag_element += diag_entry
    nmd_text_list.append(diag_element)
for col_id in range(1,len(reverse_text_list[0])):
    diag_element = ''
    for k in range(len(reverse_text_list) - col_id):
        diag_entry = reverse_text_list[k][col_id + k]
        diag_element += diag_entry
    nmd_text_list.append(diag_element)
nmd_text_list.append(''.join([reverse_text_list[i][i] for i in range(len(reverse_text_list))]))
## All diagonals
diag_text_list = md_text_list + nmd_text_list
## Counting
for i in diag_text_list:
    matches = re.findall(pattern = r"(XMAS)", string=i)
    reverse_matches = re.findall(pattern = r"(XMAS)", string=i[::-1])
    ncount += len(matches) + len(reverse_matches)
# Answer for Part I
print(ncount)

# Part II
filters_list = []
for row_id in range(0,len(text_list) - 2):
    filter = []
    for col_id in range(0,len(text_list) - 2):
        row = ''.join([text_list[row_id + i][col_id + j] for i in range(3) for j in range(3)])
        filter.append(row)
    filters_list += filter
## Reformat
for f_id in range(len(filters_list)):
    p = []
    for i in range(3):
        p.append(filters_list[f_id][3*i:3*i+3])
    filters_list[f_id] = p
# Filters for matches
def filter_match(p):
    if p[1][1] == 'A':
        if (p[0][0] == 'M') & (p[2][2]=='S') & (p[2][0]=='M') & (p[0][2]=='S'):
            return True
        elif (p[0][0] == 'M') & (p[2][2]=='S') & (p[2][0]=='S') & (p[0][2]=='M'):
            return True
        elif (p[0][0] == 'S') & (p[2][2]=='M') & (p[2][0]=='S') & (p[0][2]=='M'):
            return True
        elif (p[0][0] == 'S') & (p[2][2]=='M') & (p[2][0]=='M') & (p[0][2]=='S'):
            return True
        else:
            return False
    else:
        return False
## Count
match_count = 0
for f in filters_list:
    if filter_match(f):
        match_count += 1
# Answer to Part II
print(match_count)
