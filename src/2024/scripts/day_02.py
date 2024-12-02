from pathlib import Path
import numpy as np
import pandas as pd

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2024' / 'data'
FILE_NAME = 'day_02.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

# Reading file
list_reports = []
with open(DATA_FILE_PATH) as f:
    for line in f:
        if line != '\n':
            nums = line.split(' ')
            nums = np.array([int(i) for i in nums])
            list_reports.append(nums)

# Part I
def is_safe(num_list: np.array):
    num_list = pd.Series(num_list)
    diff_list = num_list.diff().dropna()
    if diff_list.iloc[0]>0:
        for i in diff_list:
            if i<=0:
                return False

    elif diff_list.iloc[0]<0:
        for i in diff_list:
            if i>=0:
                return False
    else:
        return False
        
    
    abs_diff_list = np.abs(diff_list)
    if ((min(abs_diff_list)>=1) and (max(abs_diff_list)<=3)):
        return True
    else:
        return False

# Answer to Part I
num_safereports = 0
for report in list_reports:
    if is_safe(report):
        num_safereports += 1
print(num_safereports)

# Part II
num_safereport_variants = 0
for report in list_reports:
    if is_safe(report):
        num_safereport_variants += 1
    else: 
        report = list(report)
        report_variants_list = []
        for i in range(len(report)):
            report_pop = report.copy()
            report_pop.pop(i)
            report_variants_list.append(np.array(report_pop))
        num_safe_variants = 0
        for variant in report_variants_list:
            if is_safe(variant):
                num_safe_variants += 1
        if num_safe_variants>0:
            num_safereport_variants += 1
print(num_safereport_variants)