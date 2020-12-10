from utils import read_input

lines = list(map(int, read_input("input9.txt")))
# print(lines[:5])
size = 25


def is_valid(n, buffer):
    buffer = sorted(buffer)

    i = 0
    j = len(buffer) - 1

    while True:
        if i == j:
            return False
        t = buffer[i] + buffer[j]
        if t > n:
            j -= 1
        elif t < n:
            i += 1
        else:
            return True


for i in range(size, len(lines)):
    if not is_valid(lines[i], lines[i - size : i]):
        print(lines[i], "is not valid!")


w = 104054607
i = 0
j = 1
while True:
    buffer = lines[i : j + 1]
    t = sum(buffer)
    if t < w:
        j += 1
    elif t > w:
        i += 1
    else:
        print("Found!", i, j, max(buffer) + min(buffer))
        break
