from pathlib import Path
import numpy as np
import pandas as pd
import re

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2024' / 'data'
FILE_NAME = 'day_03.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Reading file
text = ''
with open(DATA_FILE_PATH) as f:
    text = f.read().replace('\n','')

# Part I
pattern = r"mul\(([0-9]+),([0-9]+)\)"
sum_product = 0
for match in re.finditer(pattern, string=text):
    first_num = int(match.group(1))
    second_num = int(match.group(2))
    sum_product += first_num * second_num

# Answer to Part I
print(sum_product)

# Part II
text = 'do()' + text + "don't()"
pattern_2 = r"do\(\)(.*?)don't\(\)"
enabled_text = ''
for match in re.finditer(pattern_2, string=text):
    enabled_text += match.group(1)

sum_product_2 = 0
for match_2 in re.finditer(pattern, string=enabled_text):
    first_num_2 = int(match_2.group(1))
    second_num_2 = int(match_2.group(2))
    sum_product_2 += first_num_2 * second_num_2

# Answer to Part II
print(sum_product_2)