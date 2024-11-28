import pandas as pd

#1)

financials = pd.read_csv('financials.csv')
languages = pd.read_csv('languages.csv')
movies = pd.read_csv('movies.csv')
new_movies = pd.read_csv('new_movies.csv')

# print(financials.head(3))
# print(languages.size)
# print(movies.shape[1])

#2)

df_new_movies = pd.concat([movies, new_movies], ignore_index=True)
print(df_new_movies.tail(5))

#3)

df_mouvies = pd.merge(movies, languages, on='language_id', how='inner')
print(df_mouvies)

#4)
movies = pd.merge(movies, financials, on='movie_id', how='left')
# print(movies.tail(5))

#5) 
movies.to_csv('final_complete.csv', columns=['movie_id', 'title', 'lang_name', 'budget', 'revenue', 'currency'], index=False)