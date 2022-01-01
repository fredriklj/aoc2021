fn = "input.txt"

bmap = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

count = 0


def parse(**kwargs):
    buf = kwargs.get("buf", "")
    parent = kwargs.get("parent", 0)
    level = 0

    global count
    global child

    while len(buf) > 0:

        # header
        pver, buf = int(buf[:3], 2), buf[3:]
        count += pver
        ptype, buf = int(buf[:3], 2), buf[3:]

        if ptype == 4:  # literal
            val = ""
            while buf[0] != "0":
                payload, buf = buf[:5], buf[5:]
                val += payload[1:]

            payload, buf = buf[:5], buf[5:]
            val += payload[1:]
            decval = int(val, 2)
            print("End of literal packet with value: %s" % (decval))
            return buf, decval

        else:  # operator
            if len(buf) >= 1:
                ltype, buf = buf[:1], buf[1:]

        if ltype == "0":
            oplen, buf = int(buf[:15], 2), buf[15:]
            print("Operator packet with l-type %s and oplen %s" % (ltype, oplen))
            level = 4
        elif ltype == "1":
            oppkt, buf = int(buf[:11], 2), buf[11:]
            print("Operator packet with l-type %s and %s packets" % (ltype, oppkt))
            level = 4

        leafs = []
        if ltype == "0":  # operator length type bits
            opbuf, buf = buf[:oplen], buf[oplen:]
            while len(opbuf) > 0:
                print("Subpacket recursion on %s bits" % (oplen))
                (opbuf, res) = parse(buf=opbuf)
                leafs.append(res)
            level = 0
        elif ltype == "1":  # operator length type packets
            for i in range(0, oppkt):
                if len(buf) > 0:
                    print("Subpacket recursion on %s packets" % (oppkt))
                    (buf, res) = parse(buf=buf)
                    leafs.append(res)

        if ptype == 0:
            res = sum(leafs)
        elif ptype == 1:
            res = 0
            for i in leafs:
                res *= i
        elif ptype == 2:
            res = min(leafs)
        elif ptype == 3:
            res = max(leafs)
        elif ptype == 5:
            if leafs[0] > leafs[1]:
                res = 1
            else:
                res = 0
        elif ptype == 6:
            if leafs[0] < leafs[1]:
                res = 1
            else:
                res = 0
        elif ptype == 7:
            if leafs[0] == leafs[1]:
                res = 1
            else:
                res = 0
        return buf, res

    if len(buf.rstrip("0")) == 0:
        buf = ""
        res = ""

    return buf, res


with open(fn, "rb") as f:
    buf = ""
    while True:
        indata = f.read(1).decode("utf-8")
        if indata not in bmap.keys():
            break
        buf += bmap[indata]

    buf, res = parse(buf=buf, parent=0)
    print(count, res)
