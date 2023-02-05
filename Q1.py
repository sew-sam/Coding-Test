import pandas as pd

df = pd.read_csv("Merge.csv", parse_dates = ['Datetime'])
df_new = df.loc[(df['Datetime'].dt.strftime('%H:%M:%S') >= '07:00:00') & (df['Datetime'].dt.strftime('%H:%M:%S') <= '17:00:00')]

df_index = df_new.set_index(['Datetime', 'Resolution'], inplace = True)

df_new = df_new.groupby(level=1).resample('2H', offset = '1H', level = 0).mean()
df_new.ffill(axis = 0)

print(df_new)