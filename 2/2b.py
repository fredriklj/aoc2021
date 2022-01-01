import pandas as pd

input = []
f = "input.txt"

for line in open(f).readlines():
    a, b = line.strip().split(" ")
    input.append((a, int(b)))


df = pd.DataFrame(input, columns=["dir", "steps"])
df.loc[df.dir == "down", "aim"] = df.steps
df.loc[df.dir == "up", "aim"] = -df.steps
df.loc[df.dir == "forward", "aim"] = 0

df = df.assign(incline=df.aim.cumsum())

df.loc[df.dir == "forward", "depth"] = df.steps * df.incline

fw = df.loc[df.dir == "forward"].sum().steps
td = df.loc[df.dir == "forward"].sum().depth

print(fw * td)
