import pandas as pd
import numpy as np
df = pd.read_csv("liquorsales.csv")
cn = df.groupby(['item_description','zip_code']).agg({ 'bottles_sold': 'sum'}).sort_values('bottles_sold',ascending=False).head(1)
df2 = df.groupby(by=["store_name","item_description"], as_index=False)['bottles_sold']\
    .agg('sum')
df2 = df2.rename(columns={'bottles_sold':'count'})
df2['percent'] = ((df2['count'])/df2['count'].sum())*100
df2 = df2.sort_values(by='percent', ascending=False)
print(cn)
print(df2.head(1))




