import copy

f = "input4.txt"
graph = {}


def getpaths(graph, start, end, path=[]):
    ngraph = copy.deepcopy(graph)

    if len(path) > 0:
        if start.islower() and start in path:
            for src in ngraph:
                for dst in ngraph[src]:
                    if dst == start:
                        ngraph[src].remove(start)
        count = {}
        for s in path:
            if s.islower():
                count[s] = path.count(s)
        o = sorted(count.values(), reverse=True)
        if len(o) > 1:
            if o[1] > 1:
                return []

    path = path + [start]

    if start == end:
        return [path]
    if start not in ngraph.keys():
        return []

    paths = []

    for node in ngraph[start]:
        newpaths = getpaths(ngraph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)

    return paths


for line in open(f).readlines():
    a, b = line.strip().split("-")
    if a not in graph.keys():
        graph[a] = []
    if b != "start":
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
