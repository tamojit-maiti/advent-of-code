from pathlib import Path
import numpy as np

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_25.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Toy Problem
a = [-2,12,15,21,1,34,67,72]

if a[0]>=a[1]: 
    max_num = a[0]
    second_max_num = a[1]
else:
    max_num = a[1]
    second_max_num = a[0]    

for i in a[2:]:
    if i>max_num:
        second_max_num = max_num
        max_num = i
    elif i>second_max_num:
        second_max_num = i

print(max_num)
print(second_max_num)

x_guess = 35
lambda_ = 0.09
x_old = x_guess
for i in range(100):
    x_new = x_old - lambda_*(2*x_old + 7)
    x_old = x_new
    print(i, x_new)
