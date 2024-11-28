import pandas as pd

#1)
df = pd.read_csv('movies_data.csv')

row_df = df.shape[0]
col_df = df.shape[1]


#2)
g = df.groupby('industry')
for key, data in g:
    if key == 'Bollywood':
         print(data)
         print(data.size)

#3)
def distribution(rating: float) -> str:
    if 1 < rating < 3.9:
        return 'Poor'
    elif 4 < rating < 7.9:
        return 'Average'
    elif 8 < rating < 10:
        return 'Good'
    else:
        return 'Others'

df['category_rating'] = df['imdb_rating'].apply(distribution)

k = df.groupby('category_rating')

for key, data in k:
    print('key: ', key)

