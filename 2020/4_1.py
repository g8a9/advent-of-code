from utils import read_input

lines = read_input("input4.txt")

lb = 0
valid = 0

def is_valid(lines, lb, hb):
    ppi = set(map(lambda it: it.split(":")[0], " ".join(lines[lb:hb]).split(" ")))
    return len(ppi) == 8 or (len(ppi) == 7 and (not "cid" in ppi))


for hb, l in enumerate(lines):
    if l == "":
        if is_valid(lines, lb, hb):
            valid += 1
        lb = hb + 1

if is_valid(lines, lb, len(lines)):
    valid += 1

print(valid)
