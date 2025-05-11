import pandas as pd
df=pd.read_csv("top-1000-trending-youtube-videos.csv")
#df.to_csv("output.csv",index=False)
#print(df)
'''#print(df.head())
print(df.describe())
print(df.shape)
'''

df_filled=df.copy()
df_filled['Likes']=df_filled['Likes'].fillna("0")
#df_filled['Category']=df_filled['Category'].fillna(0)
print("\n data frame after filling missing value\n",df_filled['Likes'])

df_filled['Category']=df_filled['Category'].fillna("0")
print("\n data frame after filling missing value\n",df_filled['Category'])


df_dropped=df.dropna()
print("\n data frame after dropping rows with missing values\n",df_dropped)

df_no_duplicates=df.drop_duplicates(keep='first')
print("\n data frame after removing duplicates (keep first)\n",df_no_duplicates)

df.to_csv("output.csv",index=False)
print(df)
print(df['Likes'].describe())
print(df.info())

 