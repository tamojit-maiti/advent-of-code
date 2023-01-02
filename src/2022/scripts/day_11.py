from pathlib import Path
from itertools import islice

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / 'data'
FILE_NAME = 'day_11_test.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

class Monkey:
    def __init__(self, 
                items : list, 
                operation : str, 
                operator : int, divisor : int, 
                monkey_1 : int, 
                monkey_2 : int):
        self.items = items
        self.operation = operation
        self.operator = operator
        self.divisor = divisor
        self.monkey_1 = monkey_1
        self.monkey_2 = monkey_2

    def throw_away(self, item):
        pass

    def receive(self, item):
        pass 

    def operate(self, operation):
        pass

    def test(self, ):
        pass

    def inspect(self):
        pass

    def __repr__(self) -> str:
        return (self.items, 
                self.operation, 
                self.operator, 
                self.divisor, 
                self.monkey_1, 
                self.monkey_2)
    
# Reading the data
with open(DATA_FILE_PATH) as f:
    lines = islice(f, 7)

    for line in lines:
        print(line)
