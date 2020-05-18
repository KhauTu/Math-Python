import pandas as pd

data = pd.read_csv('200.csv')

df = pd.DataFrame(data = data)
d = df.describe(include = 'all')
for title in df.columns:
    print(d[title])