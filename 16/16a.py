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
    seq = kwargs.get("seq", 0)
    level = kwargs.get("level", 0)
    depth = kwargs.get("depth", 0)

    global count

    while len(buf) > 0:

        if level == 0:  # packet version

            if len(buf) >= 8:
                pver, buf = int(buf[:3], 2), buf[3:]
                count += pver
                level = 1
                seq += 1
                print(
                    "Seq: %s, Depth %s, Version: %s, Buf: %s" % (seq, depth, pver, buf)
                )

        if level == 1:  # packet type
            if len(buf) >= 3:
                ptype, buf = int(buf[:3], 2), buf[3:]
                level = 2
                print("Seq: %s, Depth %s, Type: %s, Buf: %s" % (seq, depth, ptype, buf))

        if level == 2:
            if ptype == 4:  # literal
                while len(buf) >= 5 and buf[0] != "0":
                    val, buf = buf[:5], buf[5:]
                    print(
                        "Seq: %s, Depth %s, Payload: %s, Buf: %s"
                        % (seq, depth, val, buf)
                    )

                if len(buf) >= 5 and buf[0] == "0":
                    val, buf = buf[:5], buf[5:]
                    print(
                        "Seq: %s, Depth %s, Payload: %s, Buf: %s"
                        % (seq, depth, val, buf)
                    )
                    print(
                        "Seq: %s, Depth %s, End of literal packet, Buf: %s"
                        % (seq, depth, buf)
                    )
                    return buf

            else:  # operator
                if len(buf) >= 1:
                    ltype, buf = buf[:1], buf[1:]
                    print(
                        "Seq: %s, Depth %s, L-type: %s, Buf: %s"
                        % (seq, depth, ltype, buf)
                    )
                    level = 3

        if level == 3:  # operator length
            if ltype == "0" and len(buf) >= 15:
                oplen, buf = int(buf[:15], 2), buf[15:]
                print(
                    "Seq: %s, Depth %s, Oplen: %s, Buf: %s" % (seq, depth, oplen, buf)
                )
                level = 4
            elif ltype == "1" and len(buf) >= 11:
                oppkt, buf = int(buf[:11], 2), buf[11:]
                print(
                    "Seq: %s, Depth %s, Oppkts: %s, Buf: %s" % (seq, depth, oppkt, buf)
                )
                level = 4

        if level == 4 and ltype == "0":  # operator length type bits
            if len(buf) >= oplen:
                opval, buf = buf[:oplen], buf[oplen:]
                print(
                    "Seq: %s, Depth %s, Bitlen subpacket: %s, Buf: %s"
                    % (seq, depth, opval, buf)
                )
                buf = parse(buf=opval + buf, seq=seq, level=0, depth=depth + 1)
                while len(buf) >= 8:
                    print("Seq: %s, Depth %s, Subpacket: %s" % (seq, depth, buf))
                    buf = parse(buf=buf, seq=seq, level=0, depth=depth + 1)
                level = 0

        if level == 4 and ltype == "1":  # operator length type packets
            for i in range(0, oppkt):
                if len(buf) >= 8:
                    print("Seq: %s, Depth %s, Oplen subpacket: %s" % (seq, depth, buf))
                    buf = parse(buf=buf, seq=seq, level=0, depth=depth + 1)

        if len(buf.rstrip("0")) == 0:
            buf = ""

    return buf


with open(fn, "rb") as f:
    buf = ""
    while True:
        indata = f.read(1).decode("utf-8")
        if indata not in bmap.keys():
            break
        buf += bmap[indata]

    parse(buf=buf)
    print(count)
