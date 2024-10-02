import pandas as pd
csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
df = pd.read_csv(csv_url, index_col=0)

# The most common operation is with .head() 
df.head(15)

# Now lets get a description of the data
df.describe()

# You can also get metadata about the dataset with .info()
df.info()

df = pd.read_csv("pandas/world-championship-qualifier.csv")
print(df)

df = pd.read_json("pandas/world-championship-qualifier.json")
print(df)