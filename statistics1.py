import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/user/Desktop/pandasapp/excels/height.xlsx')
sn.histplot(df.height, kde=True)
plt.show()
mean = df.height.mean()
std_deviation = df.height.std()
print(std_deviation)
print(mean - 3*std_deviation)
print(mean + 3*std_deviation)
df_cleared = df[(df.height > 2.8) & (df.height < 77.6842)]
print(df_cleared.height.sort_values())

# Z-score

df['z_score'] = (df.height - mean) / std_deviation
df_cleared = df[((df.z_score) > -3) | (df.z_score < 3)]
print(df_cleared)