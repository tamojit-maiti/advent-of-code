from pathlib import Path
import numpy as np

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / 'data'
FILE_NAME = 'day_9_test.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

class Rope:

    def __init__(self, n_links : int, state_matrix: np.ndarray) -> None:
        self.n_links = n_links
        self.state_matrix = state_matrix
        # Link Positions
        self.link_pos_dict = {i:(state_matrix.shape[0] - 1, 0) for i in range(1, n_links + 1)}

    def print_state(self) -> None:
        print(self.link_pos_dict)
        for label, pos in self.link_pos_dict.items():
            print(pos)
            self.state_matrix[pos[0], pos[1]] = label
        print(self.state_matrix)

state_matrix = np.zeros((6,6))
r = Rope(n_links = 4, state_matrix = state_matrix)
r.print_state()