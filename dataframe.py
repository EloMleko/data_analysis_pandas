import pandas as pd
import numpy as np
import random

# 1

df1 = pd.DataFrame({'X': [78, 85, 96, 80, 86], 'Y': [
                   84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]})

# 2

df2 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
df2_1 = df2.copy()
# 3

df3 = df2.info()

# 4

df4 = df2.head(3)

# 5

df5 = df2[['name', 'score']]

# 6

df6 = df2[['name', 'score']].iloc[[1, 3, 5, 6]]

# 7

df7 = df2[df2['attempts'] > 2]

# 8

print('Number of Rows: ', df2.shape[0], '\nNumber of Columns: ', df2.shape[1])

# 9

df9 = df2[df2['score'].isna()]

# 10

df10 = df2[(df2['score'] >= 15) & (df2['score'] <= 20)]
df10_1 = df2[df2['score'].between(15, 20)]

# 11

df11 = df2[(df2['attempts'] < 2) & (df2['score'] > 15)]

# 12

df2.loc['d', 'score'] = 11.5

# 13

df13 = df2['attempts'].sum()

# 14

df14 = df2['score'].mean()

# 15

df2.loc['k'] = ['Suresh', 15.5, 1, 'yes']
df2 = df2.drop('k')

# 16

df16 = df2.sort_values(by=['name', 'score'], ascending=[False, True])

# 17

df17 = df2['qualify'].replace(['yes', 'no'], [True, False])
df17_1 = df2['qualify'].map({'yes': True, 'no': False})

# 18

df2['name'][(df2['name'] == 'James')] = 'Suresh'
df2['name'] = df2['name'].replace('James', 'Suresh')

# 19

df19 = df2.drop(['attempts'], axis=1)
# alternatively: df2.pop('attempts')

# 20

df2['color'] = [random.choice(['Red', 'Blue', 'Green'])
                for _ in range(df2.shape[0])]
df2.pop('color')
print(df2)

# 21

df21 = pd.DataFrame([{'name': 'Anastasia', 'score': 12.5}, {
                    'name': 'Dima', 'score': 9}, {'name': 'Katherine', 'score': 16.5}])

for _, row in df21.iterrows():
    print(row['name'], row['score'])

# 22

df22 = list(df2.columns)

# 23

df23 = pd.DataFrame([[1, 4, 7], [2, 5, 8], [3, 6, 9]],
                    columns=['col1', 'col2', 'col3'])
df23.columns = ['Column1', 'Column2', 'Column3']

# 24

df24 = pd.DataFrame([[1, 4, 7], [4, 5, 8], [3, 6, 9], [4, 7, 0], [
                    5, 8, 1]], columns=['col1', 'col2', 'col3'])
df24_2 = df24[df24['col1'] == 4]
df24_1 = df24.loc[df24['col1'] == 4]

# 25

df25 = df24.copy()
df25 = df25.reindex(columns=['col3', 'col2', 'col1'])

# 26

df26 = df24.copy()
df26.loc['5'] = [10, 11, 12]

# 27

df27 = df24.copy()
df27.to_csv('Tab.csv', sep='\t')
df27_1 = pd.read_csv('Tab.csv')

# 28

df28 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                     'city': ['California', 'Los Angeles', 'California', 'California',
                              'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})

df28_1 = df28.groupby(['city']).count().reset_index()
df28_2 = df28.groupby(['city']).size().reset_index(name='number of people')

# 29

df29 = df24.copy()
df29 = df29.loc[df29['col3'] != 8]
df29 = df29.drop(df29.loc[df29['col3'] == 8].index)

# 30

# 31

df31 = df24.copy()
idx = 2
df31 = df31.iloc[[idx]]

# 32 

df32 = df2.copy()
df32 = df32.fillna(0)

# 33

df33 = df2.copy()
df33.reset_index(drop=True, inplace=True)

# 34 

df34 = df33.copy()
#df34._set_value(8, 'score', 10.2)
df34.loc[8, 'score'] = 10.2

# 35 

df35 = df33.copy()
df35 = df35.isnull().values.sum()

# 36 

df36 = df33.copy()
df36 = df36.drop([2, 4])

# 37

df37 = df33.copy()
df37 = df33.drop([0,1]).reset_index()

# 38 

df38 = df33.copy()
ratio = round(df38.shape[0] * 0.7)
df38= df38.loc[:ratio]

# -- 70% -- 30%
df38_1 = df33.copy().sample(frac=0.7, replace=False)
df38_2 = df33.copy().drop(df38_1.index)

# 39 

series39 = pd.Series([100, 200, 'python', 300.12, 400])
series39_1 = pd.Series([10, 20, 'php', 30.12, 40])
df39 = pd.DataFrame([series39, series39_1]).T

# 40

df40 = df33.copy().sample(frac=1)

# 41

df41 = pd.DataFrame(['3/11/2000', '3/12/2000', '3/13/2000']).apply(pd.to_datetime)

# 42

df42 = df23.copy()
df42 = df42.rename(columns={'Column1' : 'col1'})

# 43

df43 = df23.copy()['Column2'].tolist()

# 44

df44 = pd.DataFrame(np.zeros(shape=(15, 3)), columns=['Column1', 'Column2', 'Column3'],
                    index=['Index' + str(i) for i in range(1, 16)])

# 45 

df45 = pd.DataFrame([[1, 4, 7], [2, 5, 8], [3, 6, 12], [4, 9, 1], [7, 5, 11]], 
                    columns=['col1', 'col2', 'col3']).idxmax(axis=0).to_dict()

# 46

df46 = pd.DataFrame([[1, 4, 7], [2, 5, 8], [3, 6, 12], [4, 9, 1], [7, 5, 11]], 
                    columns=['col1', 'col2', 'col3'])

column_names = ['col1', 'col4']
for item in column_names:
    if item in df46.columns:
        print(f'{item} is not present in DataFrame.')
    else:
        print(f'{item} is present in DataFrame.')

# 47

df47 = df46.copy()
df47 = df47.iloc[[0, 3]]

# 48

df48 = df2.copy().dtypes.to_dict()

# 49

df49 = pd.DataFrame([])
data = pd.DataFrame({'col1': [0, 1, 2], 'col2' : [0,1,2]})
df49 = df49.append(data, ignore_index = True)

# 50

df50 = df2.copy().sort_values(by=['attempts', 'name'])
print(df50)

# 51 

df51 = df2.copy()
df51.score = df51.score.fillna(0).astype(int)

# 52 

df52 = pd.DataFrame([1000.000000, 2000.000000, 3000.000000, -4000.000000, np.inf, -np.inf]
                    ).replace([-np.inf, np.inf], np.nan)

# 53

""" df53 = pd.DataFrame({'col2' : [4, 5, 6, 9, 5], 'col3' : [7, 8, 12, 1, 11]})
df53_1 = pd.DataFrame({'col1' : [1, 2, 3, 4, 7]})
df53_2 = pd.concat([df53_1, df53], axis=1) """

df53 = pd.DataFrame({'col2' : [4, 5, 6, 9, 5], 'col3' : [7, 8, 12, 1, 11]})
data = [1, 2, 3, 4, 7]
df53.insert(0, 'col1', data)

# 54

list_of_lists = [[2,4], [1,3]]
df54 = pd.DataFrame(list_of_lists, columns=['col1', 'col2'])

# 55

df55 = pd.DataFrame({'col1' : ['C1', 'C1', 'C2', 'C2', 'C3', 'C3', 'C2',], 
                     'col2' : [1, 2, 3, 3, 4, 6, 5]}) \
                     .groupby(['col1'])['col2'].apply(list)

# 56

df56 = df46.copy()
df56 = df56.columns.get_loc('col2')

# 57

df57 = df46.copy().columns.value_counts().sum()
df57_1 = len(df46.columns)
df57_2 = df46.shape[1]

# 58

df58 = df46.copy()
df58 = df58.drop(['col3'], axis=1)
df58_1 = df58.loc[:, df58.columns != 'col3']

# 59

df59 = df46.copy()
n_row = 3
df59 = df59.iloc[:n_row]
df59_1 = df59.head(n_row)

# 60

df60 = df46.copy()
df60 = df60.tail(n_row)
df60_1 = df60.iloc[-n_row:]






