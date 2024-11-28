import pandas as pd     

df = pd.read_csv('food_db.csv')

row_df = df.shape[0]
col_df = df.shape[1]

new_df = df.replace(['5%', '10%'], '13%')

new_df = df.replace({
    'Excellent': 4,
    'Very Good': 3,
    'Good': 2,
    'Average': 1
})

#new_df = df.replace(["Excellent", 'Very Good', 'Good', 'Average'], [4, 3, 2, 1])

