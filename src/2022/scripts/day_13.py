from pathlib import Path
import numpy as np

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_25.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

l1 = np.array([[ 2, 1, -1, -1, -1],[ 1, 4, 3, -1, -1], [ 3, 1, 0, -1, -1]])
l2 = np.array([[ 0.7, 0.4, 1.5, 2.0, 4.4 ], [ 0.8, 4.0, 0.3, 0.11, 0.53], [ 0.6, 7.4, 0.22, 0.71, 0.06]])
print(l2[l1[l1>-1]])