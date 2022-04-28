graph = {}
visited = []
queue = []


def childadd():
    for x in parent:
        print("Enter the children of ", x, " node: ")
        child = list(input().split())
        graph[x] = child


def bfs(node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        if m in goal:
            print("\nGoal node", m, "found")
            exit(0)
        for y in graph[m]:
            if y not in visited:
                visited.append(y)
                queue.append(y)


print("Enter the parent nodes (root node as the 1st node): ")
parent = list(input().split())
root = parent[0]
print("Enter the leaf nodes: ")
leaf = list(input().split())
childadd()
for x in leaf:
    graph[x] = []

print("Enter the goal nodes: ")
goal = list(input().split())
if root in goal:
    print("Root node is the goal node")
else:
    print("Following is the Breadth-First Search")
    bfs(root)
    print("\nGoal node not found")

# Reference graph
# graph = {
#  'A' : ['B','C'],
#  'B' : ['D', 'E'],
#  'C' : ['D','G'],
#  'D' : ['C','F'],
#  'E' : [],
#  'F' : ['H'],
#  'G' : ['F'],
#  'H' : []
# }
