import pandas as pd
playstore = pd.read_csv('.\\01_Python\\Unit_05_Pandas\\playstore.csv')

# task 1
data_head = playstore.head(3)
data_tail = playstore.tail(3)

# task 2
n_col = playstore.shape[1]
n_row = playstore.shape[0]

# task 3
df_dt = playstore.drop_duplicates('App', keep='first').copy()
df_dt.describe()

# task 4
rating_missing = playstore[playstore['Rating'].isna() == True].shape[0]

# task 5
ps = playstore[['App', 'Size', 'Genres', 'Current Ver']]
result = pd.concat([ps.head(3), ps.loc[5:7], ps.loc[15:18]])
result.to_csv('mp_result_1.csv')

# task 6
unique_playstore = playstore.drop_duplicates(subset = 'App', keep='first').reset_index(drop = True).copy()

# task 7
playstore.columns = playstore.columns.str.replace(pat = ' ', repl = '_').str.lower()

# via lambda
playstore.rename(columns = lambda x: x.replace(" ", "_").lower())

# task 8
unique_playstore = playstore.drop_duplicates(subset = 'App', keep='first').reset_index(drop = True).copy()
new_dataset = unique_playstore.groupby('Type', as_index=False).agg({'Unnamed: 0': 'count'})
round(new_dataset['Unnamed: 0'][0]/new_dataset['Unnamed: 0'].sum(), 2)

# task 9
playstore = playstore.drop_duplicates(subset = 'App', keep='first').reset_index(drop = True).copy()
playstore = playstore.rename(columns = lambda x: x.replace(" ", "_").lower())
education_playstore = playstore[
(playstore['category'] == 'EDUCATION') & (playstore['reviews'] > 1000)
].reset_index(drop = True)


# task 10
playstore['price'] = playstore['price'].str.replace(pat = '$', repl = '').astype('float')

# task 11
playstore = playstore.drop_duplicates(subset = 'App', keep='first').reset_index(drop = True).copy()
playstore = playstore.rename(columns = lambda x: x.replace(" ", "_").lower())
result = pd.pivot_table(
    playstore,
    index=['category', 'type'],
    values=['price', 'rating', 'reviews'],
    aggfunc='mean'
)
result = result.rename(columns = {"price": "mean_price", "rating": "mean_rating", "reviews": "mean_reviews"})
result[['mean_price', 'mean_reviews']] = round(result[['mean_price', 'mean_reviews']], 2)
result[['mean_rating']] = round(result[['mean_rating']], 1)
# result
result.to_csv('mp_result_2.csv')

# round type
# pivot_dt = pivot_dt.round({'price': 2, 'rating': 1, 'reviews': 2})

