import pandas as pd

# input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
input = []
f = "input.txt"

for line in open(f).readlines():
    input.append(int(line.strip()))


series = pd.Series(input)
df = pd.DataFrame(series, columns=["input"])
df["s1"] = df["input"].shift()
df["s2"] = df["s1"].shift()
df["t"] = df["input"] + df["s1"] + df["s2"]
df["ts"] = df["t"].shift()
df.loc[df.t > df.ts, "difference"] = "increased"
print(df.difference.value_counts()["increased"])
