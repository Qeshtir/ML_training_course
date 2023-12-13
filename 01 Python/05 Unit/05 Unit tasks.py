# task 1
import pandas as pd
df5 = pd.read_csv('.\\01 Python\\05 Unit\\data.csv')
list(df5["dateAdded"].head(3))

# task 2
df5.dtypes

# task 3-4
df5.describe()

# task 5
df_na = df5.copy()
df_na.dropna(inplace=True)

# task 6
sub_df = df5[df5['city'] == 'California'].copy()
list(sub_df.reset_index()["index"])

# task 7
sub_df = df5[(df5['city'] == 'California') & (df5['name'] == 'Taco Bell')].copy()
list(sub_df.reset_index()["index"])

# task 8
data = df5.copy()
result = data[
    (
            (data['city'] == 'New York') | (data['name'] == 'Taco Bell')
    )
    &
    ~(
            (data['menus.name'].isin(['Volcano Taco'])) | (data['menus.name'].isin(['Fresco Soft Taco']))
    )
].copy()

# task 9
data = df5.copy()
result = data[~(data.isna())]


# task 11
list(df5.groupby('city').agg({'id': "count"}).sort_values(by=["id"], ascending=False).head(5).reset_index()['city'])

# task 12
data = df5.copy()
result = data[data['name'] == 'Taco Bell'].groupby('city').agg({'id': "count"}).sort_values(by=["id"], ascending=False).head(5).reset_index()

result = data[data['name'] == 'Taco Bell']['city'].value_counts().head(5)

# task 13
df_dt = df5.copy()
df_dt['dateAdded'] = pd.to_datetime(df_dt['dateAdded'])
list(df_dt[df_dt['dateAdded'].dt.month == 10].head(5).reset_index()['index'])

# task 14
data = df5.copy()
df_dt = data.drop_duplicates('id', keep='first').copy()
df_dt['dateAdded'] = pd.to_datetime(df_dt['dateAdded'])
result = df_dt.groupby(
    df_dt['dateAdded'].dt.month  # для каждого месяца
).agg({
    'id': 'count'
})

# task 15
data = df5.copy()
df_dt = data.copy()
df_dt['dateAdded'] = pd.to_datetime(df_dt['dateAdded'])
df_dt['dateUpdated'] = pd.to_datetime(df_dt['dateUpdated'])
df_dt['update_delta'] = df_dt['dateUpdated'] - df_dt['dateAdded']
df_dt['update_delta'] = df_dt['update_delta'].dt.days

result = df_dt.groupby('city', as_index=False).agg({'update_delta': 'mean', 'latitude':'max'})
zep_group = df_dt[df_dt['city'] == 'Zephyrhills'].groupby('city', as_index=False).agg({'update_delta': 'mean'})
zep_mean = zep_group.iloc[0]['update_delta']

# task 16
df5[df5['categories'].str.contains('Pizza')]

# task 17
data = df5.copy()
df_dt = data.copy()
df_dt['dateAdded'] = pd.to_datetime(df_dt['dateAdded'])
df_dt['dateUpdated'] = pd.to_datetime(df_dt['dateUpdated'])
df_dt['update_delta'] = df_dt['dateUpdated'] - df_dt['dateAdded']
df_dt['update_delta'] = df_dt['update_delta'].dt.days
df_dt['update_delta'].mean()
df_dt['update_delta'].median()

# task 18
pre_result = df5[df5['categories'].str.split(pat = ',').apply(len) > 20][['province','longitude']]
result = pre_result.groupby('province', as_index=False).agg({'longitude': 'min'})
result[['longitude']] = result[['longitude']].round(3)
result.to_csv('result.csv', sep=';', index=False)