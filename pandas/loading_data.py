import pandas as pd
csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
df = pd.read_csv(csv_url, index_col=0)

# Now lets get a description of the data
print(df.describe())

# You can also get metadata about the dataset with .info()
print(df.info())

print(df.sort_values(by="rating", ascending=False).head())

df.drop(['grape'], axis=1, inplace=True)
print(df.describe())

df = pd.read_csv("pandas/world-championship-qualifier.csv")
print(df)

df = pd.read_json("pandas/world-championship-qualifier.json")
print(df)