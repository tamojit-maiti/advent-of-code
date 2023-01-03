from pathlib import Path

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_5.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

class Queue:

    def __init__(self, 
                index : int,
                value : list = []) -> None:
        self.index = index
        self.value = value

    def add(self, add_list : list) -> None:
        for element in add_list[::-1]:
            self.value.append(element)

    def add_stack(self, add_list : list) -> None:
        for element in add_list:
            self.value.append(element)
    
    def pop(self, n : int) -> list:
        popped_list = [self.value[-i] for i in range(n,0,-1)]
        self.value = self.value[:-n]
        return popped_list

    @staticmethod
    def transfer(from_index: int, to_index: int, n: int) -> None:
        from_queue = queue_state[from_index]
        to_queue = queue_state[to_index]
        popped_list = from_queue.pop(n)
        to_queue.add(popped_list)
        return None

    @staticmethod
    def stack_transfer(from_index: int, to_index: int, n: int) -> None:
        from_queue = queue_state[from_index]
        to_queue = queue_state[to_index]
        popped_list = from_queue.pop(n)
        to_queue.add_stack(popped_list)
        return None

queue_dict = {
                1:['R','P','C','D','B','G'],
                2:['H','V','G'],
                3:['N','S','Q','D','J','P','M'],
                4:['P','S','L','G','D','C','N','M'],
                5:['J','B','N','C','P','F','L','S'],
                6:['Q','B','D','Z','V','G','T','S'],
                7:['B','Z','M','H','F','T','Q'],
                8:['C','M','D','B','F'],
                9:['F','C','Q','G']
            }

queue_state = {}
for i in range(1,10,1):
    queue_state[i] = Queue(index = i, value=queue_dict[i])

# Reading the data
with open(DATA_FILE_PATH) as f:
    for line in f:
        if line.startswith('move'):
            digits = line.split(' ')
            n, from_index, to_index = int(digits[1]), int(digits[3]), int(digits[5])
            Queue.transfer(from_index = from_index,
                    to_index = to_index,
                    n = n)
        else:
            pass

print('Answer to Part I')
answer_1 = ''
for i in range(1,10):
    answer_1 += queue_state[i].value[-1]
print(answer_1)

# Reset States
queue_dict = {
                1:['R','P','C','D','B','G'],
                2:['H','V','G'],
                3:['N','S','Q','D','J','P','M'],
                4:['P','S','L','G','D','C','N','M'],
                5:['J','B','N','C','P','F','L','S'],
                6:['Q','B','D','Z','V','G','T','S'],
                7:['B','Z','M','H','F','T','Q'],
                8:['C','M','D','B','F'],
                9:['F','C','Q','G']
            }

queue_state = {}
for i in range(1,10,1):
    queue_state[i] = Queue(index = i, value=queue_dict[i])

# Reading the data
with open(DATA_FILE_PATH) as f:
    for line in f:
        if line.startswith('move'):
            digits = line.split(' ')
            n, from_index, to_index = int(digits[1]), int(digits[3]), int(digits[5])
            Queue.stack_transfer(from_index = from_index,
                    to_index = to_index,
                    n = n)
        else:
            pass

print('Answer to Part II')
answer_2 = ''
for i in range(1,10):
    answer_2 += queue_state[i].value[-1]
print(answer_2)