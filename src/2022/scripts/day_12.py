from pathlib import Path
import numpy as np

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_12.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Helper Functions 
def alpha_to_num(char: str) -> int:
    if char == 'S':
        return 0
    if char == 'E':
        return 27
    else:
        return ord(char) - 96

def get_neighbours(position : tuple, matrix: np.array) -> list[tuple]:
    x = position[0]
    y = position[1]
    all_neighbours_list = [(x-1, y), (x+1, y), (x, y-1),(x, y+1)]
    actual_neighbours_list = [n for n in all_neighbours_list if is_valid_point(n, matrix)]
    travellable_neighbours_list = [n for n in actual_neighbours_list if is_travellable(position, n, matrix)]
    return travellable_neighbours_list

def is_travellable(position: tuple, n: tuple, matrix: np.array) -> list[tuple]:
    diff = matrix[n[0],n[1]] - matrix[position[0],position[1]]
    if (diff <=1):
        return True
    else:
        return False

def is_reverse_travellable(position: tuple, n: tuple, matrix: np.array) -> list[tuple]:
    diff = matrix[n[0],n[1]] - matrix[position[0],position[1]]
    if (diff >=-1):
        return True
    else:
        return False

def get_reverse_neighbours(position : tuple, matrix: np.array) -> list[tuple]:
    x = position[0]
    y = position[1]
    all_neighbours_list = [(x-1, y), (x+1, y), (x, y-1),(x, y+1)]
    actual_neighbours_list = [n for n in all_neighbours_list if is_valid_point(n, matrix)]
    travellable_neighbours_list = [n for n in actual_neighbours_list if is_reverse_travellable(position, n, matrix)]
    return travellable_neighbours_list

def get_unvisited_neighbours(position: tuple, 
                                matrix: np.array,
                                points_visited: list[tuple]
                            ):
    actual_neighbours_list = get_neighbours(position=position,
                                            matrix=matrix)
    unvisited_neighbours = [n for n in actual_neighbours_list if n not in points_visited]
    return unvisited_neighbours

def get_unvisited_reverse_neighbours(position: tuple, 
                                matrix: np.array,
                                points_visited: list[tuple]
                            ):
    actual_neighbours_list = get_reverse_neighbours(position=position,
                                            matrix=matrix)
    unvisited_neighbours = [n for n in actual_neighbours_list if n not in points_visited]
    return unvisited_neighbours

def is_valid_point(position: tuple, matrix: np.array) -> bool:
    x = position[0]
    y = position[1]
    if x>=0 and x<matrix.shape[0] and y>=0 and y<matrix.shape[1]:
        return True
    else:
        return False    

# Reading the data
with open(DATA_FILE_PATH) as f:
    lines = []
    for line in f:
        line = line.strip()
        line = [alpha_to_num(i) for i in line]
        lines.append(line)

lines = np.array(lines, dtype = int)

# Constants
STARTING_POSITION = (np.where(lines == 0)[0][0],np.where(lines == 0)[1][0])
END_POSITION = (np.where(lines == 27)[0][0],np.where(lines == 27)[1][0])

# Variables
points_visited = []
active_points = [STARTING_POSITION]
count = 0

# Part I
while END_POSITION not in list(set(active_points)):
    count += 1
    new_points = []
    for point in active_points:
        unvisited_neighbours = get_unvisited_neighbours(position = point, 
                                                    matrix = lines, 
                                                    points_visited = points_visited
                                                    )
        new_points += unvisited_neighbours
    points_visited += active_points
    points_visited = list(set(points_visited))
    active_points = list(set(new_points))
    active_points = list(set(active_points))

# Answer to Part I
print(count)

# Reading the data
with open(DATA_FILE_PATH) as f:
    lines = []
    for line in f:
        line = line.strip()
        line = [alpha_to_num(i) for i in line]
        lines.append(line)

lines = np.array(lines, dtype = int)

# Constants
STARTING_POSITION = (np.where(lines == 27)[0][0],np.where(lines == 27)[1][0])
END_POSITION = (np.where(lines == 1)[0][0],np.where(lines == 1)[1][0])

# Variables
points_visited = []
active_points = [STARTING_POSITION]
count = 0

def value_not_reached(active_points: list[tuple], matrix: np.array) -> bool:
    for point in active_points:
        if matrix[point[0],point[1]] == 1:
            return False
    return True

# Part I
while value_not_reached(list(set(active_points)), matrix = lines):
    count += 1
    new_points = []
    for point in active_points:
        unvisited_neighbours = get_unvisited_reverse_neighbours(position = point, 
                                                    matrix = lines, 
                                                    points_visited = points_visited
                                                    )
        new_points += unvisited_neighbours
    points_visited += active_points
    points_visited = list(set(points_visited))
    active_points = list(set(new_points))
    active_points = list(set(active_points))

# Answer to Part II
print(count)