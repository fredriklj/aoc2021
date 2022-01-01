import random


def f1(a, b, c):
    return 26 * a + b + c


def f2(z, w, c, d):
    x = z % 26 + c
    z = int(z / 26)

    print("    z % 26 + c = ",x," and w = ",w)

    if w != x:
        z = z * (25 * x + 1) + (w + d) * x

    return z


while True:
    start = 94992994195998  # right answer

    monad = list(map(int, list(str(start))))

    if 0 not in monad:

        ## Indatavärde 1
        z = monad[0]
        print(1,z)
        z = f1(z, monad[1], 6)
        print(2,z)
        z = f1(z, monad[2], 4)
        print(3,z)
        z = f1(z, monad[3], 2)
        print(4,z)
        z = f1(z, monad[4], 9)
        print(5,z)
        z = f2(z, monad[5], -2, 1)
        # z % 26 = w + 2
        print(6,z)
        z = f1(z, monad[6], 10)
        print(7,z)
        z = f2(z, monad[7], -15, 6)
        # z % 26 = w + 15
        print(8,z)
        z = f2(z, monad[8], -10, 4)
        # z % 26 = w + 10
        print(9,z)
        z = f1(z, monad[9], 6)
        print(10,z)
        z = f2(z, monad[10], -10, 3)
        # z % 26 = w + 10
        print(11,z)
        z = f2(z, monad[11], -4, 9)
        # z % 26 = w + 4
        print(12,z)
        z = f2(z, monad[12], -1, 15)
        # z % 26 = w + 1
        print(13,z)
        z = f2(z, monad[13], -1, 5)
        # z % 26 = w + 1
        print(14,z)

    # print(start)
    # start += 1
    break

