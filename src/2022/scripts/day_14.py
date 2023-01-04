from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_14.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Reading the data
with open(DATA_FILE_PATH) as f:
    points_list = []
    for line in f:
        line = line.strip().split(' -> ')
        points = [(int(point.split(',')[0]), int(point.split(',')[1])) for point in line]
        points_list.append(points)

# Generate matrix
def generate_matrix(points_list: list[tuple]) -> np.array:
    all_edge_points = []
    for segments in points_list:
        for points in segments:
            all_edge_points.append(points)
    max_x = max([p[0] for p in all_edge_points])
    max_y = max([p[1] for p in all_edge_points])
    screen = np.zeros((max_y, max_x + 2))
    return screen

# Visualize matrix
def draw_matrix(screen: np.array) -> None:
    plt.imshow(X = screen)
    plt.show()
    return None

# Generate Segments
def generate_segments(from_point: tuple, to_point: tuple) -> list[tuple]:
    points_in_segment = []
    if from_point[0] == to_point[0]:
        for i in range(from_point[1],to_point[1] + np.sign(to_point[1] - from_point[1]), np.sign(to_point[1] - from_point[1])):
            points_in_segment.append((from_point[0], i))
    if from_point[1] == to_point[1]:
        for i in range(from_point[0],to_point[0] + np.sign(to_point[0] - from_point[0]), np.sign(to_point[0] - from_point[0])):
            points_in_segment.append((i, from_point[1]))
    return points_in_segment

# Generate Wall Points
def generate_wall_points(points_list: list[tuple]) -> list[tuple]:
    wall_points = []
    for segment in points_list:
        segment_points = []
        for i in range(len(segment) - 1):
            segment_points += generate_segments(from_point = segment[i],
                                            to_point = segment[i+1])
        wall_points += segment_points
    return wall_points

# Draw walls on screen
def fix_walls(screen: np.array, wall_points: list[tuple]) -> np.array:
    for wall_point in wall_points:
        screen[wall_point[1]-1, wall_point[0]-1] = 1
    return screen

screen = generate_matrix(points_list)
wall_points = generate_wall_points(points_list)
screen = fix_walls(screen, wall_points)
draw_matrix(screen)
