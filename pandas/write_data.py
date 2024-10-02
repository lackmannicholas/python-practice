import pandas as pd

df = pd.read_csv("pandas/world-championship-qualifier.csv")

# export a dataset to HTML
df.to_html("pandas/dataset.html")

print(df)