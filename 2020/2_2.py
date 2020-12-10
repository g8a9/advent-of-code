from collections import Counter

count = 0
with open("input2.txt") as fp:
    ls = [l.strip() for l in fp.readlines()]
    for l in ls:
        toks = l.split(" ")
        minv, maxv = map(int, toks[0].split("-"))
        if (toks[2][minv-1] == toks[1][0]) != (toks[2][maxv-1] == toks[1][0]):
            count += 1
print(count)
