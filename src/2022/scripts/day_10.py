from pathlib import Path
import numpy as np

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_10.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Variables
CYCLE = 1
X = 1
running_sum = 0
cycle_x_log = []

# Reading the data
with open(DATA_FILE_PATH) as f:
    for line in f:
        line = line.strip('\n')
        if line == 'noop':
            cycle_x_log.append((CYCLE,X))
            CYCLE += 1
            
        else:
            digit = int(line.split(' ')[1])
            cycle_x_log.append((CYCLE,X))
            cycle_x_log.append((CYCLE + 1,X))
            CYCLE += 2
            X += digit
        if CYCLE in [20,60,100,140,180,220]:
            running_sum += CYCLE * X

# Answer to Part I
print(running_sum)

# Helper Functions
def get_dot_hash(cycle: int, x: int) -> str:
    draw_row = cycle%40
    sprite_loc = [x,x+2,x+1]
    if draw_row in sprite_loc:
        return '#'
    else:
        return '.'

output_str = ''
for cycle, x in cycle_x_log:
    output_str += get_dot_hash(cycle, x)
    if (cycle%40==0):
        output_str += '\n'

# Answer to Part II
print(output_str)