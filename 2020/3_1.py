from utils import read_input

lines = read_input("input3.txt")

trees = 0
idx = 0
step = 3
ncols = len(lines[0])
for l in lines[1:]:
    idx = (idx + 3) % ncols
    if l[idx] == "#":
        trees += 1
print(trees)
