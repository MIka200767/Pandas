import pandas as pd


#change costum column names
fl = pd.read_excel('movies_list.xlsx', header=1, names=["movies", "ratings", "year", "budget", "language"])

print(fl['rating'].value_counts())

print(fl[['title', 'rating', 'language']])

df = fl[fl.rating<8]

#creating new column
fl["revenue"]= fl["date"].apply(lambda x: 2023 - x)

#creating dictionary
fl.set_index('title', inplace=True)
print(fl.loc['Joker'])

#get row by index
print(fl.iloc[3:6:2])

fl["age"] = 2024 - fl['year'] 
fl.to_excel('movies_list.xlsx')

# drop cloumns
fl = fl.drop(fl.columns[[0,1]], axis=1)


print(fl)