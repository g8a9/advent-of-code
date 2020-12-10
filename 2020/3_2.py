from utils import read_input

lines = read_input("input3.txt")

trees = 1
ncols = len(lines[0])
for stepr, stepd in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
    j = 0
    ct = 0
    for i in range(stepd, len(lines), stepd):
        j = (j + stepr) % ncols
        if lines[i][j] == "#":
            ct += 1
    trees *= ct
print(trees)
