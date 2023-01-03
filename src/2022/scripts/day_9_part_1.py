from pathlib import Path
import numpy as np

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_9.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

seq_direction_list = []

# Reading the data
with open(DATA_FILE_PATH) as f:
    for line in f:
        line = line.strip('\n')
        direction = line.split(' ')[0]
        n_steps = int(line.split(' ')[1])
        seq_direction_list.append((direction, n_steps))

# Helper Functions
def get_horizontal_length(seq_direction_list : list[tuple])-> int:
    steps_list = []
    for direction, n_steps in seq_direction_list:
        if (direction == 'R'):
            steps_list.append(n_steps)
        elif (direction == 'L'):
            steps_list.append(-n_steps)
        else:
            pass
    return max(np.cumsum(steps_list)) + 1

def get_vertical_length(seq_direction_list : list[tuple])-> int:
    steps_list = []
    for direction, n_steps in seq_direction_list:
        if (direction == 'U'):
            steps_list.append(n_steps)
        elif (direction == 'D'):
            steps_list.append(-n_steps)
        else:
            pass
    return max(np.cumsum(steps_list)) + 1

def construct_state_matrix(n_rows : int, n_cols : int) -> np.ndarray:
    return np.zeros(shape=[n_rows,n_cols], dtype=int)

def get_distance(head_row: int, 
                head_col: int, 
                tail_row: int, 
                tail_col: int) -> float:
    head_vector = np.array([head_row, head_col])
    tail_vector = np.array([tail_row, tail_col])
    return np.linalg.norm(head_vector - tail_vector)


class Rope:

    def __init__(self, state_matrix : np.ndarray):
        self.state_matrix = state_matrix
        # Starting positions for head and tail
        self.head_row = state_matrix.shape[0] - 1
        self.head_col = 0 
        self.tail_row = state_matrix.shape[0] - 1
        self.tail_col = 0 
        # Tail Visit Counter
        self.tail_visit_list = []
    
    def move_right(self, n_steps : int)-> None:
        for i in range(n_steps):
            self.head_col += 1
            if get_distance(self.head_row, self.head_col, self.tail_row, self.tail_col)>1.5:
                self.tail_row = self.head_row
                self.tail_col = self.head_col - 1
            self.tail_visit_list.append((self.tail_row, self.tail_col))    
        return None

    def move_left(self, n_steps : int)-> None:
        for i in range(n_steps):
            self.head_col -= 1
            if get_distance(self.head_row, self.head_col, self.tail_row, self.tail_col)>1.5:
                self.tail_row = self.head_row
                self.tail_col = self.head_col + 1
            self.tail_visit_list.append((self.tail_row, self.tail_col))    
        return None

    def move_up(self, n_steps : int)-> None:
        for i in range(n_steps):
            self.head_row -= 1
            if get_distance(self.head_row, self.head_col, self.tail_row, self.tail_col)>1.5:
                self.tail_row = self.head_row + 1
                self.tail_col = self.head_col
            self.tail_visit_list.append((self.tail_row, self.tail_col))    
        return None

    def move_down(self, n_steps : int)-> None:
        for i in range(n_steps):
            self.head_row += 1
            if get_distance(self.head_row, self.head_col, self.tail_row, self.tail_col)>1.5:
                self.tail_row = self.head_row - 1
                self.tail_col = self.head_col
            self.tail_visit_list.append((self.tail_row, self.tail_col))    
        return None

    def print_state(self):
        self.state_matrix = np.zeros_like(self.state_matrix)
        self.state_matrix[self.head_row, self.head_col] = 1
        self.state_matrix[self.tail_row, self.tail_col] = -1
        print(self.state_matrix)
        return None

    
# Flow
state_matrix = construct_state_matrix(n_rows = get_vertical_length(seq_direction_list),
                                        n_cols = get_horizontal_length(seq_direction_list))

r = Rope(state_matrix)

for direction, n_steps in seq_direction_list:
    if direction == 'L':
        r.move_left(n_steps)
    elif direction == 'R':
        r.move_right(n_steps)
    elif direction == 'U':
        r.move_up(n_steps)
    else:
        r.move_down(n_steps)

print(len(set(r.tail_visit_list)))
