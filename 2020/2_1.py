from collections import Counter

count = 0
with open("input2.txt") as fp:
    ls = [l.strip() for l in fp.readlines()]
    for l in ls:
        toks = l.split(" ")
        minv, maxv = map(int, toks[0].split("-"))
        c = Counter(toks[2])
        if c[toks[1][0]] >= minv and c[toks[1][0]] <= maxv:
            count += 1
print(count)
