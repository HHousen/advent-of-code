from collections import Counter, namedtuple
import heapq
import math


with open("puzzle_input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().splitlines()

Box = namedtuple("Box", ["x", "y", "z"])
boxes = [Box(*map(int, line.split(","))) for line in puzzle_input]

class UnionFind:
    # https://www.geeksforgeeks.org/dsa/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n
        self.num_components = n

    def find(self, i):
        root = self.parents[i]
        if self.parents[root] != root:
            self.parents[i] = self.find(root)
            return self.parents[i]
        return root

    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return
        isize = self.sizes[irep]
        jsize = self.sizes[jrep]

        if isize < jsize:
            self.parents[irep] = jrep
            self.sizes[jrep] += self.sizes[irep]
        else:
            self.parents[jrep] = irep
            self.sizes[irep] += self.sizes[jrep]
        
        self.num_components -= 1


num_boxes = len(boxes)
distances = []
for i in range(num_boxes):
    box_a = boxes[i]
    for j in range(i + 1, num_boxes):
        box_b = boxes[j]
        distance = (box_a.x - box_b.x)**2 + (box_a.y - box_b.y)**2 + (box_a.z - box_b.z)**2
        distances.append((distance, i, j))
heapq.heapify(distances)

dsuf = UnionFind(num_boxes)

for _ in range(1000):
    _, box_a_idx, box_b_idx = heapq.heappop(distances)
    dsuf.union(box_a_idx, box_b_idx)

sizes = Counter()
for i in range(num_boxes):
    sizes[dsuf.find(i)] += 1

part1_solution = math.prod(s[1] for s in sizes.most_common(3))

# Part 1 Solution: 84968
print(f"Part 1 Solution: {part1_solution}")

while True:
    _, box_a_idx, box_b_idx = heapq.heappop(distances)
    dsuf.union(box_a_idx, box_b_idx)
    if dsuf.num_components == 1:
        part2_solution = boxes[box_a_idx].x * boxes[box_b_idx].x
        break

# Part 2 Solution: 8663467782
print(f"Part 2 Solution: {part2_solution}")
