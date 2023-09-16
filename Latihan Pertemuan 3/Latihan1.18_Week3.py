import pandas as pd

data = {
    'satu': [1,1,1,1,1],
    'dua': [2,2,2,2,2],
    'tiga': [3,3,3,3,3],
}

df = pd.DataFrame(data, index = ['a','b','c','d','e'])
df.head()

print(df)