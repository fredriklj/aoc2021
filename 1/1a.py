import pandas as pd

# input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
input = []
f = "input.txt"

for line in open(f).readlines():
    input.append(int(line.strip()))

series = pd.Series(input)
df = pd.DataFrame(series, columns=["input"])
df["shifted"] = df["input"].shift()
df.loc[df.input > df.shifted, "difference"] = "increased"
print(df.difference.value_counts()["increased"])
