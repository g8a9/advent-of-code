def read_input(filename):
    with open(filename, "r") as fp:
        return [f.strip() for f in fp.readlines()]
