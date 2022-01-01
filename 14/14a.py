f = "input1.txt"
# input = "NN"
input = "NNCB"
# input = "OKSBBKHFBPVNOBKHBPCO"
rounds = 20
m = {}

for line in open(f).readlines():
    a, b = line.strip().split(" -> ")
    m[a] = b

for r in range(0, rounds):
    p = ""
    for i in range(0, len(input) - 1):
        k = input[i] + input[i + 1]
        p += input[i] + m[k]
    p += input[-1]
    input = p
    # print("Iter", p)

output = sorted(input, key=input.count, reverse=True)
print(output.count(output[0]) - output.count(output[-1]))
