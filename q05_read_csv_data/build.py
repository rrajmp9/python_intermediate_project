# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
# Enter code here
path = './data/ipl_matches_small.csv'
def read_ipl_data_csv(path = './data/ipl_matches_small.csv', dtype = '|S50'):
    ipl_matches_array = np.genfromtxt(path, dtype = '|S50', delimiter = ',', skip_header = 1)
    return ipl_matches_array

print read_ipl_data_csv(path)


