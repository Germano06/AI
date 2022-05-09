graph = {}
heu = {}
visited = []
queue = []
local = []


def srt(lis):
    for i in range(len(lis)-1):
        min = heu[lis[i]]
        l = i
        for j in range(i+1, len(lis)):
            y = heu[lis[j]]
            if ((ch == 1) & (min > y)) | ((ch == 2) & (min < y)):
                min, l = y, j
        lis[i], lis[l] = lis[l], lis[i]
    return lis


def childadd():  # adds all child nodes to the graph
    for x in parent:
        print("Enter the children of ", x, " node: ")
        child = srt(list(input().split()))
        graph[x] = child


def locl(c):
    # for i in local:
    #     for j in graph:
    #         if (i in graph[j]) & (c in graph[j]):
    #             return
    if c not in local:
        local.append(c)
        print("Local", t, "reached at", c)


def hcl(node):  # hill climbing function
    visited.append(node)
    queue.append(node)
    if node == ele:
        print("\nTraversal path:", visited)
        print("Actual path:", queue)
        print("\nGlobal", t, "reached at", ele, "node")
        exit(0)
    for y in graph[node]:
        if ((ch == 1) & (heu[node] < heu[y])) | ((ch == 2) & (heu[node] > heu[y])):
            locl(node)
        if heu[node] == heu[y]:
            print("Plateau reached at", node, "and", y)
        hcl(y)
        queue.pop()
        if(node != visited[-1]):
            visited.append(node)


ch = int(input("\n1-> Descend\n2-> Ascend\nEnter your choice: "))
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

if ch == 1:
    t = "minima"
if ch == 2:
    t = "maxima"

ele, val = root, heu[root]
for x in heu:
    if ((ch == 1) & (heu[x] < val)) | ((ch == 2) & (heu[x] > val)):
        val, ele = heu[x], x

print("\nFollowing is the Hill-Climbing Search\n")
hcl(root)
