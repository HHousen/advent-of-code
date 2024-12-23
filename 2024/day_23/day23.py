from collections import defaultdict
from itertools import combinations
import networkx as nx

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()


connections = defaultdict(set)
for connection in puzzle_input:
    source, dst = connection.split("-")
    connections[source].add(dst)
    connections[dst].add(source)

threes = set()
for source in connections:
    if source[0] == "t":
        for n1, n2 in combinations(connections[source], 2):
            if n2 in connections[n1]:
                threes.add(frozenset((source, n1, n2)))

part1_solution = len(threes)

# Part 1 Solution: 1156
print("Part 1 Solution:", part1_solution)

graph = nx.Graph()
for connection in puzzle_input:
    node1, node2 = connection.split("-")
    graph.add_edge(node1, node2)

largest_clique = max(nx.find_cliques(graph), key=len)
part2_solution = ",".join(sorted(largest_clique))  # password

# Part 2 Solution: bx,cx,dr,dx,is,jg,km,kt,li,lt,nh,uf,um
print("Part 2 Solution:", part2_solution)
