with open("input8.txt") as fp:
    lines = [l.strip() for l in fp.readlines()]


def test_sequence(lines):
    acc = 0
    ic = 0
    visited = [0] * len(lines)

    while True:
        if ic == len(lines):
            print("Reached the end. Final acc value:", acc, ic, len(lines))
            return 1, acc

        #  print(ic, lines[ic])
        op, val = lines[ic].split(" ")
        val = int(val)

        if visited[ic] > 0:
            #  print(f"Visiting again {ic}: {lines[ic]}")
            #  print("Last acc:", acc)
            return 0, acc
        else:
            visited[ic] += 1

        if op == "jmp":
            ic += val
            continue

        if op == "acc":
            acc += val

        ic += 1


test_sequence(lines)

for idx in reversed(range(len(lines))):
    ops = lines.copy()
    if ops[idx].startswith("nop"):
        ops[idx] = ops[idx].replace("nop", "jmp")
    if ops[idx].startswith("jmp"):
        ops[idx] = ops[idx].replace("jmp", "nop")
    # print(ops, idx)
    test_sequence(ops)