import pandas as pd

# Create data frame 
data = [[1, 2], [3, 4]] 
df = pd.DataFrame(data, columns=['Num1', 'Num2'], index=['R1', 'R2'])
print(df)

# Create series
s = df['Num1']
print(s)

data = [[4,2,1],
        {3,0,1},
        [1,0,0]]

columns = ['apples', 'bananas', 'oranges']
index = ['Monday', 'Tuesday', 'Wednesday']

df = pd.DataFrame(data, index, columns)
print(df)
