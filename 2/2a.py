import pandas as pd

input = [
    ["forward", 5],
    ["down", 5],
    ["forward", 8],
    ["up", 3],
    ["down", 8],
    ["forward", 2],
]

df = pd.DataFrame(input, columns=["dir", "steps"])
fw = df.loc[df.dir == "forward"].sum().steps
up = df.loc[df.dir == "up"].sum().steps
dn = df.loc[df.dir == "down"].sum().steps

print((dn - up) * fw)
