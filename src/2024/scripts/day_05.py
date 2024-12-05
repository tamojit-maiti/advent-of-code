from pathlib import Path
import numpy as np
import pandas as pd
import re

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2024' / 'data'
FILE_NAME = 'day_05.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Reading file
rules_list = []
checks = []
with open(DATA_FILE_PATH) as f:
    for line in f:
        if line != '\n':
            line = line.strip('\n')
            if line[2] == '|':
                rules_list.append((line[:2],line[3:]))
            elif line[2] == ',':
                checks.append(line)

## Preprocessing
for i in range(len(rules_list)):
    rules_list[i] = (int(rules_list[i][0]), int(rules_list[i][1]))
for i in range(len(checks)):
    checks[i] = list(eval(checks[i]))

# Part I
mid_num_list = []
for check in checks:
    passed = True
    for first_index in range(len(check)):
        for seccond_index in range(first_index + 1, len(check)):
            if (check[first_index], check[seccond_index]) in rules_list:
                pass
            else:
                passed = False
    if passed:
        mid_num_list.append(check[int((len(check) - 1)/2)])
# Answer to Part I
print(sum(mid_num_list))

# Part II
mid_num_list = []
for check in checks:
    passed = True
    for first_index in range(len(check)):
        for seccond_index in range(first_index + 1, len(check)):
            if (check[first_index], check[seccond_index]) in rules_list:
                pass
            else:
                check[first_index], check[seccond_index] = check[seccond_index], check[first_index]
                passed = False
    if passed == False:
        mid_num_list.append(check[int((len(check) - 1)/2)])
# Answer to Part II
print(sum(mid_num_list))