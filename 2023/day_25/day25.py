import math
import networkx as nx

with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

graph = nx.Graph()

for line in puzzle_input:
    source, destinations = line.split(": ")
    for destination in destinations.split():
        graph.add_edge(source, destination)

cuts = nx.minimum_edge_cut(graph)
graph.remove_edges_from(cuts)

part1_solution = math.prod(
    len(component) for component in nx.connected_components(graph)
)

# Solution: 592171
print(f"Solution: {part1_solution}")
