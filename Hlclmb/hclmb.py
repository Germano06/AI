graph = {}
heu = {}
visited = []
queue = []
local = []


def childadd():  # adds all child nodes to the graph
    for x in parent:
        print("Enter the children of ", x, " node: ")
        child = list(input().split())
        graph[x] = child


def cmpr(x):  # compares the heu values and returns the node with min or max val
    z = x[0]
    for i in range(len(x)):
        if ((ch == 1) & (heu[z] > heu[x[i]])) | ((ch == 2) & (heu[z] < heu[x[i]])):
            z = x[i]
    return z


def locl(p, c):
    # for i in local:
    #     if i in graph[p]:
    #         return
    local.append(c)
    print("Local", t, "reached at", c)


def hcl(node):  # hill climbing function
    visited.append(node)
    queue.append(node)
    if node == ele:
        return node
    for y in graph[node]:
        if graph[node]:
            r = cmpr(graph[node])
            if ((ch == 1) & (heu[node] < heu[r])) | ((ch == 2) & (heu[node] > heu[r])):
                locl(node, r)
            if heu[node] == heu[r]:
                print("Plateau reached at", node, "and", r)
            node = hcl(r)
    return node


print("Enter the parent nodes (root node as the 1st node): ")
parent = list(input().split())
root = parent[0]

print("Enter the heuristic values of parent nodes resp: ")
h = list(input().split())
for i in range(len(parent)):
    heu[parent[i]] = int(h[i])

print("Enter the leaf nodes: ")
leaf = list(input().split())

print("Enter the heuristic values of leaf nodes resp: ")
h = list(input().split())
for i in range(len(leaf)):
    heu[leaf[i]] = int(h[i])

childadd()
for x in leaf:
    graph[x] = []

ch = int(input("\n1-> Descend\n2-> Ascend\nEnter your choice: "))

if ch == 1:
    t = "minima"
if ch == 2:
    t = "maxima"

ele, val = root, heu[root]
for x in heu:
    if ((ch == 1) & (heu[x] < val)) | ((ch == 2) & (heu[x] > val)):
        val, ele = heu[x], x

print("Following is the Hill-Climbing Search")
print("Traversal path:")
g = hcl(root)
print(visited)
print("Global", t, "reached at", g, "node")
