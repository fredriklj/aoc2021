import copy

f = "input1.txt"
graph = {}


def getpaths(graph, start, end, path=[]):
    ngraph = copy.deepcopy(graph)

    if len(path) > 0:
        ngraph[path[-1:][0]].remove(start)

    path = path + [start]

    if start == end:
        return [path]
    if start not in ngraph.keys():
        return []

    paths = []

    for node in ngraph[start]:
        if node not in path or node.isupper():
            newpaths = getpaths(ngraph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


for line in open(f).readlines():
    a, b = line.strip().split("-")
    if a not in graph.keys():
        graph[a] = []
    graph[a].append(b)

    if b not in graph.keys():
        graph[b] = []
    if a != "start":
        graph[b].append(a)

directions = list(graph["start"])
path = []

for d in directions:
    path += getpaths(graph, d, "end", ["start"])

print(len(path))
