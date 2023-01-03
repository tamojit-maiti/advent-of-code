from pathlib import Path

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_6.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Constants
PACKET_MARKER_LENGTH = 4
MESSAGE_MARKER_LENGTH = 14

# Helper Functions

def all_unique(sliding_window : str) -> bool:
    sliding_set = set(sliding_window)
    if len(sliding_set) == len(sliding_window):
        return True
    else:
        return False

# Reading the data
with open(DATA_FILE_PATH) as f:
    for line in f:
        for i in range(len(line)-PACKET_MARKER_LENGTH):
            sliding_window = line[i:i+PACKET_MARKER_LENGTH]
            print(sliding_window)
            if all_unique(sliding_window=sliding_window):
                print('Answer to Part I')
                print(i+PACKET_MARKER_LENGTH)
                break
            else:
                pass

# Reading the data
with open(DATA_FILE_PATH) as f:
    for line in f:
        for i in range(len(line)-MESSAGE_MARKER_LENGTH):
            sliding_window = line[i:i+MESSAGE_MARKER_LENGTH]
            print(sliding_window)
            if all_unique(sliding_window=sliding_window):
                print('Answer to Part II')
                print(i+MESSAGE_MARKER_LENGTH)
                break
            else:
                pass
