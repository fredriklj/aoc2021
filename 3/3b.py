import pandas as pd

df1 = pd.read_csv("input2.txt", dtype=str)
dm = {"1": "0", "0": "1"}

df1 = df1["input"].apply(lambda x: pd.Series(list(x)))
df1.replace(dm, inplace=True)

df2 = df1

for i in range(0, df1.shape[1]):
    df1 = df1[df1[i] == df1.mode()[i].values[0]]
    if df1.shape[0] == 1:
        break

for i in range(0, df2.shape[1]):
    df2 = df2[df2[i] != df2.mode()[i].values[0]]
    if df2.shape[0] == 1:
        break

df1.replace(dm, inplace=True)
df2.replace(dm, inplace=True)

foo = int(df1.apply("".join, axis=1).values[0], 2)
bar = int(df2.apply("".join, axis=1).values[0], 2)

print(foo * bar)
