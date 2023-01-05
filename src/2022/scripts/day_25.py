from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_25.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

def parse_input(DATA_FILE_PATH) -> list:
    snafu_dict = {'2': '2',
                    '1':'1',
                    '0':'0',
                    '-':'-1',
                    '=':'-2'
                }
    with open(DATA_FILE_PATH) as f:
        snafu_numbers_list = []
        for line in f:
            line = line.strip()
            snafu_number = []
            for c in line:
                snafu_number.append(int(snafu_dict[c]))
            snafu_numbers_list.append(snafu_number)
    return snafu_numbers_list

def snafu_to_decimal(snafu_number: list[int]) -> int:
    n = len(snafu_number)
    decimal_num = 0
    for i in range(n):
        decimal_num += (5**i) * snafu_number[-1-i]
    return decimal_num

def decimal_to_snafu(decimal_number: int) -> list:
    snafu_number = []
    while decimal_number != 0:
        remainder = decimal_number%5
        if remainder>2:
            remainder = remainder - 5
            decimal_number = int(decimal_number/5) + 1
        else:
            decimal_number = int(decimal_number/5)
        snafu_number.append(remainder)
    return snafu_number[::-1]

def parse_output(snafu_number: list) -> str:
    snafu_dict = {'2': '2',
                '1':'1',
                '0':'0',
                '-':'-1',
                '=':'-2'
                }
    inv_snafu_dict = {int(value):key for key,value in snafu_dict.items()}
    output_str = ''
    for i in snafu_number:
        output_str += inv_snafu_dict[i]
    return output_str

if __name__ == '__main__':
    snafu_numbers_list = parse_input(DATA_FILE_PATH)
    sum_decimal = sum([snafu_to_decimal(n) for n in snafu_numbers_list])
    sum_snafu = decimal_to_snafu(sum_decimal)
    output_snafu = parse_output(sum_snafu)
    # Answer to Part I
    print(output_snafu)