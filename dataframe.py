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
print(df33)