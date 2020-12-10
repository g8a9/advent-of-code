from utils import read_input
import networkx as nx

lines = read_input("input7.txt")
G = nx.DiGraph()

for l in lines:
    toks = l.split(" ")
    color = f"{toks[0]} {toks[1]}"
    slots = [s.strip() for s in " ".join(toks[4:]).split(",")]
    if slots[0][0] != "n":  # else empty rule
        for s in slots:
            stoks = s.split(" ")
            G.add_edge(color, f"{stoks[1]} {stoks[2]}", weight=int(stoks[0]))


import matplotlib.pyplot as plt

# nx.draw(G, with_labels=True)
# plt.show()

print(
    sum(
        [
            1
            for node in G.nodes
            if node != "shiny gold"
            and ("shiny gold" in nx.algorithms.dag.descendants(G, node))
        ]
    )
)


def count_neighbors(G, node):  # this must be a DAG!
    return (
        sum(
            e["weight"] + e["weight"] * count_neighbors(G, ne)
            for ne, e in G[node].items()
        )
        if G[node]
        else 0
    )


print(count_neighbors(G, "shiny gold"))