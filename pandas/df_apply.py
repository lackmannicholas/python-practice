import pandas as pd
csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
df = pd.read_csv(csv_url, index_col=0)
df.head()

def good_wine(value):
    if value > 94:
        return True
    return False

df['good'] = df['rating'].apply(good_wine)
print(df.query('rating > 94').head())