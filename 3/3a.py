import pandas as pd

df = pd.read_csv("input2.txt", dtype=str)
gamma = int(
    df["input"]
    .apply(lambda x: pd.Series(list(x)))
    .mode()
    .apply("".join, axis=1)
    .values[0],
    2,
)
print((4095 - gamma) * gamma)
