from pathlib import Path
import numpy as np

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_11.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

class Monkey:

    SUPER = 2*3*5*7*11*13*17*19

    def __init__(self, 
                monkey_id : int,
                items : list, 
                operation : str, 
                divisor : int, 
                monkey_1 : int, 
                monkey_2 : int):
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.monkey_1 = monkey_1
        self.monkey_2 = monkey_2
        self.counter = 0

    def operate(self, part_1 : bool = True) -> None:
        new_items = []
        for old in self.items:
            old = old%self.SUPER
            if part_1:
                new_items.append(int(eval(self.operation)/3))
            else:
                new_items.append(int(eval(self.operation)%self.SUPER))
            self.counter += 1
        self.items = np.array(new_items)
        return None

    def test(self) -> None:
        for item in self.items:
            if (item%self.divisor == 0):
                monkey_dict[self.monkey_1].items = np.append(monkey_dict[self.monkey_1].items, item)
            else:
                monkey_dict[self.monkey_2].items = np.append(monkey_dict[self.monkey_2].items, item)
        self.items = np.array([])
        return None

# Helper Functions
def get_monkey_id(line_chunk) -> int:
    return int(line_chunk[0].strip().strip(':').split(' ')[1])

def parse_lines(line_chunk) -> dict:
    monkey_id = get_monkey_id(line_chunk=line_chunk)
    items = np.array(line_chunk[1].strip().split(':')[1].strip().split(','),dtype = int)
    operation = line_chunk[2].split(':')[1].split('=')[1] # needs to be evaluated
    divisor = int(line_chunk[3].split(' ')[-1])
    monkey_1 = int(line_chunk[4].split(' ')[-1])
    monkey_2 = int(line_chunk[5].split(' ')[-1])
    
    info_dict = {
                'monkey_id': monkey_id,
                'items': items,
                'operation': operation,
                'divisor': divisor,
                'monkey_1': monkey_1,
                'monkey_2': monkey_2
                }
    return info_dict

# Variables 
monkey_dict = {}

# Reading the data
with open(DATA_FILE_PATH) as f:
    lines = f.readlines()
    line_chunks = [lines[7*i:7*i+7] for i in range(1 + int(len(lines)/7))]
    for line_chunk in line_chunks:
        monkey_dict[get_monkey_id(line_chunk)] = Monkey(**parse_lines(line_chunk))

# Twenty Rounds
for _ in range(20):
    for monkey_id in monkey_dict.keys():
        monkey_dict[monkey_id].operate()
        monkey_dict[monkey_id].test()

# Get top-2 max
counters = []
for monkey_id in monkey_dict.keys():
    counters.append(monkey_dict[monkey_id].counter)
sorted_counters = sorted(counters, reverse = True)

# Answer to Part I
print(sorted_counters[0] * sorted_counters[1])

# Variables 
monkey_dict = {}

# Reading the data
with open(DATA_FILE_PATH) as f:
    lines = f.readlines()
    line_chunks = [lines[7*i:7*i+7] for i in range(1 + int(len(lines)/7))]
    for line_chunk in line_chunks:
        monkey_dict[get_monkey_id(line_chunk)] = Monkey(**parse_lines(line_chunk))

# 10000 Rounds
for _ in range(10000):
    for monkey_id in monkey_dict.keys():
        monkey_dict[monkey_id].operate(part_1 = False)
        monkey_dict[monkey_id].test()

# Get top-2 max
counters = []
for monkey_id in monkey_dict.keys():
    counters.append(monkey_dict[monkey_id].counter)
sorted_counters = sorted(counters, reverse = True)

# Answer to Part II
print(sorted_counters[0] * sorted_counters[1])