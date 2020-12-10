with open("input1.txt") as fp:
    ins = [int(f.strip()) for f in fp.readlines()]
    s = set(ins)
    for it in s:
        comp = 2020 - it
        if comp in s:
            print(f"found {it} with comp {comp}, multiplied are {it*comp}")
            break
