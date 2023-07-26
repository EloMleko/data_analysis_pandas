import pandas as pd
import numpy as np
import random
from collections import Counter
# 12

sol_12 = pd.Series([100, 200, 'python', 300.12, 400])
add = [500, 'php']

sol_12 = sol_12.append(pd.Series(add), ignore_index=True)


# 13
sol_13 = pd.Series([_ for _ in range(11)])


def subset(series, slicer=5):
    return series[:slicer]

# 14


sol_14 = pd.Series([_ for _ in range(5)], index=['A', 'B', 'C', 'D', 'E'])
sol_14 = sol_14.reindex(['B', 'A', 'C', 'D', 'E'])

# 15

sol_15 = pd.Series([random.randrange(1, 15)
                   for _ in range(15)]).agg(['std', 'mean'])

# 16

sol_16 = pd.Series([_ for _ in range(1, 15)])
sol_16_1 = pd.Series([_ for _ in range(8, 20)])

# 17

sol_17 = pd.Series([_ for _ in range(1, 6)])
sol_17_1 = pd.Series([_ for _ in range(2, 11, 2)])

sol_17_2 = pd.Series(np.union1d(sol_17, sol_17_1))
sol_17_3 = pd.Series(np.intersect1d(sol_17, sol_17_1))
result = sol_17_2[~sol_17_2.isin(sol_17_3)]

# 18

sol_18 = pd.Series([round(random.uniform(0, 10), 6) for _ in range(10)])
sol_18 = np.percentile(sol_18, [0, 25, 50, 75, 100])

# 19

sol_19 = pd.Series([random.randint(0, 10) for _ in range(40)])
sol_19 = sol_19.value_counts()

# 20

sol_20 = pd.Series([random.randint(0, 10) for _ in range(10)])
sol_20 = pd.Series(map(lambda number: number if number == max(
    sol_20, key=sol_20.tolist().count) else 'Other', sol_20))

# 21

sol_21 = pd.Series([random.randint(1, 10) for _ in range(10)])
sol_21 = list(filter(lambda x: x % 5 == 0, sol_21))

# 22

sol_22 = pd.Series([random.randint(1, 10) for _ in range(22)])
sol_22 = sol_22.take([0, 2, 4, 6, 10])

# 23

sol_23 = pd.Series([_ for _ in range(1, 11)])
sol_23_1 = pd.Series([1, 3, 5, 7, 10])
sol_23 = [pd.Index(sol_23).get_loc(i) for i in sol_23_1]

# 24

sol_24 = pd.Series(['php', 'python', 'java', 'c#',])
sol_24 = pd.Series(
    map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper(), sol_24))

# 25

sol_25 = pd.Series(['php', 'python', 'java', 'c#',]).map(lambda x: len(x))

# 26

sol_26 = pd.Series([1, 3, 5, 8, 10, 11, 15]).diff().to_list()
sol_26_1 = pd.Series(sol_26).diff().to_list()
sol_26_2 = pd.Series([1, 3, 5, 8, 10, 11, 15]).diff().diff().to_list()

# 27

sol_27 = pd.Series(['01 Jan 2015', '10-02-2016', '20180307',
                   '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
sol_27_1 = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06',
                     '2016-04-12', '2019-04-06T11:20']).apply(pd.to_datetime)

# 28

sol_28 = pd.Series(['01 Jan 2015', '10-02-2016', '20180307',
                   '2014/05/06', '2016-04-12', '2019-04-06T11:20'])


def partition(series):
    series = series.apply(pd.to_datetime)
    dictionary = dict(days=series.dt.day.to_list(),
                      day_of_year=series.dt.day_of_year.to_list(),
                      week_number=series.dt.weekofyear.to_list(),
                      day_of_week=series.dt.day_of_week.to_list()
                      )

    return dictionary

# 29


sol_29 = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018',
                   'May 2019']).apply(pd.to_datetime) + pd.DateOffset(10)

# 30

sol_30 = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
sol_30 = sol_30.apply(lambda item: sum(
    1 for ch in item.lower() if ch in ['a', 'o', 'i', 'e', 'u'])).to_list()


# 31

sol_31 = pd.Series([_ for _ in range(1, 11)])
sol_31_1 = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])

euc_dist = np.sqrt(sum(np.abs(sol_31_1 - sol_31) ** 2))

# 32

sol_32 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])

difference = np.diff(np.sign(np.diff(sol_32)))
sol_32 = np.where(difference == -2)[0] + 1

# 33

sol_33 = pd.Series('abc def abcdef icd')
replacer = Counter(list(str(sol_33[0]).replace(" ", ""))).most_common()[-1][0]
sol_33 = pd.Series(str(sol_33[0]).replace(" ", replacer))

sol_33_1 = pd.Series(list('abc def abcdef icd')
                     ).value_counts().dropna().index[-1]
sol_33_2 = sol_33[0].replace(" ", sol_33_1)

# 34


# 35

sol_35 = pd.date_range(start='1-1-2020', end='31-12-2020', freq='W')

# 36

list_of_char = list('ABCDEFGHIKLMNOPRST')
array_numbers = [_ for _ in range(len(list_of_char))]
composed_to_dict = dict(zip(list_of_char, array_numbers))
series = pd.Series(composed_to_dict)
sol_36 = series.to_frame().reset_index()

# 37

sol_37_1 = pd.Series(['a', 'b', 'c', 'd', 'e', 'f'])
sol_37_2 = pd.Series([_ for _ in range(6)])
sol_37 = pd.concat([sol_37_1, sol_37_2], axis=1)


# 38

sol_38 = pd.Series([random.randint for _ in range(10)])
sol_38_1 = sol_38.copy()
check = sol_38 == sol_38

# 39

sol_39 = pd.Series([random.randint(0, 3) for _ in range(10)])
sol_39_min = sol_39.idxmin()
sol_39_max = sol_39.idxmax()

# 40

sol_40 = pd.DataFrame([[68.0,  78.0,  84,  86], [75.0,  75.0,  94,  97], [86.0, np.nan, 89, 96], [80.0,  80.0,  86,  72],
                      [np.nan,  86.0,  86, 83]], columns=['W', 'X', 'Y', 'Z'])
sol_40_1 = pd.Series(sol_40['W'])
result = [~sol_40.isin(sol_40_1)]
result2 = sol_40.ne(sol_40_1, axis=0)






