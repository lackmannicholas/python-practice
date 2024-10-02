import pandas as pd
import matplotlib.pyplot as plt

csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
df = pd.read_csv(csv_url, index_col=0)
df.drop('grape', axis=1, inplace=True)
df = df.dropna()
df.head()

df['rating'] = df['rating'].apply(lambda x: int(x))

# plot rating by variety
df.plot.scatter(x="rating", y="variety", alpha=0.5)
plt.show()