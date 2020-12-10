from utils import read_input
import re
import logging

logging.basicConfig(level=logging.DEBUG)

lines = read_input("input5.txt")

ROWS, COLS = 128, 8


def explore(l_end, h_end, string, index, l_id, h_id):
    if index == (len(string) - 1):
        if string[index] == l_id:
            return l_end
        else:
            return h_end

    half = round((h_end - l_end) / 2) + l_end
    if string[index] == l_id:
        found_id = explore(l_end, half - 1, string, index + 1, l_id, h_id)
    else:
        found_id = explore(half, h_end, string, index + 1, l_id, h_id)

    return found_id


def get_id(string):
    row_id = explore(0, 127, string[:7], 0, "F", "B")
    col_id = explore(0, 7, string[7:], 0, "L", "R")
    logging.debug(f"{string} {row_id} {col_id}")
    return row_id * 8 + col_id


# print(get_id("FBFBBFFRLR"))

ids = [get_id(l) for l in lines]
print("MAX:")
print(max(ids))

import numpy as np

# matrix = np.zeros(128 * 8)
# matrix[ids] = 1
# matrix = matrix.reshape(128, 8)
# for i in matrix:
# print(i)

ids = sorted(ids)


def gauss(n):
    return n * (n + 1) / 2


print(gauss(ids[-1]) - gauss(ids[0] - 1) - sum(ids))