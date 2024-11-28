import pandas as pd


df = pd.read_excel('movies_list.xlsx', header=1, names=['movies', 'budget', 'year', 'age', 'language', 'havayi', 'year_classify'])

def check(x):
    if x < 2000:
        return 'before 2000'
    else:
        return 'from 2000'

df['year_classify'] = df['year'].apply(check)

#df = df.drop(df.columns[[0]], axis=1)
#df.to_excel('movies_list.xlsx')

#index change to year
df.set_index('year', inplace=True)


print(df)