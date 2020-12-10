with open("input1.txt") as fp:
    ins = [int(f.strip()) for f in fp.readlines()]
    sa = set(ins)
    for a in sa:
        for b in sa:
            if b == a or b+a > 2020:
                continue
            c = 2020 - a - b
            if c in sa:
                print(f"found {a, b, c} multiplied are {a*b*c}")
                break
