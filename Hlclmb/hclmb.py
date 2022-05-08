graph = {}
heu = {}
visited = []
queue = []


def childadd():  # adds all child nodes in the graph
    for x in parent:
        print("Enter the children of ", x, " node: ")
        child = list(input().split())
        graph[x] = child


def cmpr(x):  # compares the heu values and returns the node with min or max val
    z = x[0]
    for i in range(len(x)):
        if ((ch == 1) & (heu[z] > heu[x[i]])) | ((ch == 2) & (heu[z] > heu[x[i]])):
            z = x[i]
    return z


def hcl(node):  # hill climbing function
    visited.append(node)
    queue.append(node)
    while queue:
        y = queue.pop()
        r = cmpr(graph[y])  # r hold the child node of y having min or max val
        if ((ch == 1) & (heu[y] < heu[r])) | ((ch == 2) & (heu[y] > heu[r])):
            return y
        else:
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

print("Following is the Hill-Climbing Search")
print("Traversal path:")
g = hcl(root)
print(visited)
print("Goal node", g, "found")
