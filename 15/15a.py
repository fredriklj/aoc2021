import numpy as np
from math import inf, isinf
from heapq import heappush, heappop
from typing import Any, Mapping, Tuple, List

Node = Any
Edges = Mapping[Node, float]
Graph = Mapping[Node, Edges]

#f = "input1.txt"
f = "input2.txt"

i = []
blowup = 4

def dijkstra(graph: Graph, start: Node, goal: Node) -> Tuple[float, List]:

    shortest_distance = {}
    predecessor = {}
    heap = []

    heappush(heap, (0, start, None))

    while heap:
        distance, node, previous = heappop(heap)
        if node in shortest_distance:
            continue

        shortest_distance[node] = distance
        predecessor[node] = previous

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = predecessor[node]
            return distance, path[::-1]
        else:
            for successor, dist in graph[node].items():
                heappush(heap, (distance + dist, successor, node))
    else:
        return inf, []



for line in open(f).readlines():
     i.append(list(line.strip()))

i = [[int(a) for a in n] for n in i]
a = np.array(i)

xm, ym = np.shape(a)

for n in range(0,blowup):
    a = np.concatenate((a, (a[-ym::,-xm::]+1) % 10), axis=1)
    a[a == 0] = 1

for n in range(0,blowup):
    a = np.concatenate((a, (a[-ym::,-xm*10::]+1) % 10), axis=0)
    a[a == 0] = 1

np.set_printoptions(threshold=np.inf, linewidth=300)

xm, ym = np.shape(a)
nodes = np.arange(xm*ym)
b = nodes.reshape((xm,ym))
graph = { n : {} for n in nodes}

for x in range(0, xm):
    for y in range(0, ym):
        if x < xm-1:
            graph[b[x,y]][b[x+1,y]] = a[x+1,y]
        if y < ym-1:
            graph[b[x,y]][b[x,y+1]] = a[x,y+1]
        if x > 0:
            graph[b[x,y]][b[x-1,y]] = a[x-1,y]
        if y > 0:
            graph[b[x,y]][b[x,y-1]] = a[x,y-1]

distance, path = dijkstra(graph, nodes[0], nodes[-1])
print(distance)



