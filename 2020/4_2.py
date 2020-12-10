from utils import read_input
import re
import logging

logging.basicConfig(level=logging.DEBUG)

lines = read_input("input4.txt")

lb = 0
valid = 0


def in_range(value, lt, ht):
    return (value >= lt) and (value <= ht)

def of_len(value, length):
    return len(value) == length

def check_height(value):
    accept = True
    if value.endswith("in"):
        if not in_range(int(value[:-2]), 59, 76):
            accept = False
    elif value.endswith("cm"):
        if not in_range(int(value[:-2]),  150, 193):
            accept = False
    else:
        accept = False
    return accept
    

def check_fields(lines, lb, hb):
    ppi = set(map(lambda it: it.split(":")[0], " ".join(lines[lb:hb]).split(" ")))
    return len(ppi) == 8 or (len(ppi) == 7 and (not "cid" in ppi))


def is_valid(lines, lb, hb):
    if not check_fields(lines, lb, hb):
        return False

    accept = True
    ppi = {it.split(":")[0]: it.split(":")[1] for it in " ".join(lines[lb:hb]).split(" ")}
    
    if not of_len(ppi["byr"], 4) or not in_range(int(ppi["byr"]), 1920, 2002):
        logging.debug("failed byr " + ppi["byr"])
        accept = False

    if not of_len(ppi["iyr"], 4) or not in_range(int(ppi["iyr"]), 2010, 2020):
        logging.debug("failed iyr " + ppi["iyr"])
        accept = False

    if not of_len(ppi["eyr"], 4) or not in_range(int(ppi["eyr"]), 2020, 2030):
        logging.debug("failed eyr " + ppi["eyr"])
        accept = False

    if not check_height(ppi["hgt"]):
        logging.debug("failed height " + ppi["hgt"])
        accept = False

    if not re.search("^#[0-9a-f]{6}$", ppi["hcl"]):
        logging.debug("failed hair color " + ppi["hcl"])
        accept = False

    if not ppi["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        logging.debug("failed ecl " + ppi["ecl"])
        accept = False

    if not re.search("^[0-9]{9}$", ppi["pid"]):
        logging.debug("failed pid " + ppi["pid"])
        accept = False

    return accept    

for hb, l in enumerate(lines):
    if l == "":
        if is_valid(lines, lb, hb):
            valid += 1
        lb = hb + 1

if is_valid(lines, lb, len(lines)):
    valid += 1

print(valid)
