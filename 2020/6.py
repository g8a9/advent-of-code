from utils import read_input

lines = read_input("input6.txt")

lb = 0
total = 0


def count(lines, lb, hb):
    ppi = set("".join(lines[lb:hb]))
    return len(ppi)


from collections import Counter


def count2(lines, lb, hb):
    num_people = hb - lb
    cn = Counter("".join(lines[lb:hb]))
    # print(num_people, cn)
    candidates = [c for c in cn if cn[c] == num_people]
    # print(candidates)
    return len(candidates)


for hb, l in enumerate(lines):
    if l == "":
        total += count(lines, lb, hb)
        lb = hb + 1

total += count(lines, lb, len(lines))
print(total)

lb = 0
total = 0
for hb, l in enumerate(lines):
    if l == "":
        total += count2(lines, lb, hb)
        lb = hb + 1

total += count2(lines, lb, len(lines))
print(total)