import pandas as pd
csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
df = pd.read_csv(csv_url, index_col=0)
df.head()

wine_notes = df["notes"]
print(wine_notes.head())

named_ratings = df[["name", "rating"]]
print(named_ratings.head())

# filter rows based on a condition
top_named_ratings = named_ratings[df["rating"] > 96]
print(top_named_ratings.head())

print(df.query("rating > 93").head(10))

# add more combined queries
print(df.query("rating > 94 & region == 'Ribera del Duero, Spain'").head(10))

# chain queries to use the Python engine to operate on strings
top_wines = df.query("rating > 95")
# na=False is needed because we have some NaN region descriptions!
paso_robles = top_wines.query("region.str.contains('Robles', na=False)", engine='python')
print(paso_robles.head())