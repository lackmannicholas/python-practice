import pandas as pd
csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
df = pd.read_csv(csv_url, index_col=0)
print(df.head())

# manipulate the variety to be R for red or W for white
df["variety_short"] = df["variety"].replace({"Red Wine": "R", "White Wine": "W"})
print(df.head())

df["region_short"] = df["region"].str.split().str.get(-1)
print(df.query("region_short != 'California'").head())