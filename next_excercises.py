import pandas as pd
import numpy as np
import random

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

# 12

sol_12 = pd.Series([100, 200, 'python', 300.12, 400])
add = [500, 'php']

sol_12 = sol_12.append(pd.Series(add), ignore_index = True)


#13
sol_13 = pd.Series([_ for _ in range(11)])
def subset(series, slicer=5):
    return series[:slicer]

#14 

sol_14 = pd.Series([_ for _ in range(5)], index=['A', 'B', 'C', 'D', 'E'])
sol_14 = sol_14.reindex(['B', 'A', 'C', 'D', 'E'])

#15

sol_15 = pd.Series([random.randrange(1, 15) for _ in range(15)]).agg(['std', 'mean'])

#16

sol_16 = pd.Series([_ for _ in range(1,15)])
sol_16_1 = pd.Series([_ for _ in range(8, 20)])

#17 

sol_17 = pd.Series([_ for _ in range(1, 6)])
sol_17_1 = pd.Series([_ for _ in range(2, 11, 2)])

sol_17_2 = pd.Series(np.union1d(sol_17, sol_17_1))
sol_17_3 = pd.Series(np.intersect1d(sol_17, sol_17_1))
result = sol_17_2[~sol_17_2.isin(sol_17_3)]
print(result)

#18 

sol_18 = pd.Series([round(random.uniform(0, 10), 6) for _ in range(10)])
sol_18 = np.percentile(sol_18, [0, 25, 50, 75, 100])

#19

sol_19 = pd.Series([random.randint(0, 10) for _ in range(40)])
sol_19 = sol_19.value_counts()

#20 

sol_20 = pd.Series([random.randint(0, 10) for _ in range(10)])
sol_20 = pd.Series(map(lambda number: number if number == max(sol_20, key=sol_20.tolist().count) else 'Other', sol_20))

#21 

sol_21 = pd.Series([random.randint(1, 10) for _ in range(10)])
sol_21 = list(filter(lambda x: x % 5 == 0, sol_21))
print(sol_21)

#22 

sol_22 = pd.Series([random.randint(1, 10) for _ in range(22)])
print(sol_22[:11])
sol_22 = sol_22.take([0, 2, 4, 6, 10])
print(sol_22)
