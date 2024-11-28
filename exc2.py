import pandas as pd
import numpy as np

df = pd.read_csv('fruits_data2.csv', names=['apple', 'banana', 'grapes', 'mango', 'watermelon'])

#1)
#number of rows
row_df = df.shape[0]
#number of columns
columns_df = df.shape[1]

#2)
new_df = df.fillna(-1)
print(new_df)

#3)
new_df = df.fillna({
    'apple': df.apple.mean(),
    'banana': df.banana.mean(),
    'grapes': df.grapes.median(),
    'mango': df.mango.median(),
    'watermelon': df.watermelon
})

#4)
new_df = df.fillna(method='ffill')
print(new_df)

#5)
new_df = df.dropna(how='any')
print(new_df)