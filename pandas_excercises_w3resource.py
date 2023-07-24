import pandas as pd
import numpy as np

# 1
sol_1 = pd.Series([1, 2, 3, 4, 5])

# 2
sol_2 = pd.Series([1, 2, 3, 4, 5]).to_list()

# 3
sol_1 = pd.Series([1, 2, 3, 4, 5])
sol_3_1 = pd.Series([2, 3, 4, 5, 6])


def simple_calc(series1, series2):
    return series1 + series2, series1 - series2

# 5


sol_5 = pd.Series({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800})

# 6
np_ar = np.array([10, 20, 30, 40, 50])
sol_6 = pd.Series(np_ar)

# 7
sol_7 = pd.Series([100, 200, 'python', 300.12, 400])
sol_7_1 = pd.to_numeric(sol_7, errors='coerce')

# 8
sol_8 = pd.DataFrame({'col1': [1, 2, 3, 4, 5],
                      'col2': [1, 2, 3, 4, 5],
                      'col3': [1, 2, 3, 4, 5]})
sol_8_1 = pd.Series(sol_8['col1'])

# 9
sol_9 = pd.Series([100, 200, 'python', 300.12, 400])
array = np.array(sol_9)

# 10
sol_10 = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
sol_10 = sol_10.apply(pd.Series).stack().reset_index(drop=True)

# 11
sol_11 = pd.Series([100, 200, 'python', 300.12, 400])
sol_11 = sol_11.astype('str').sort_values()
print(sol_11)

# 12
