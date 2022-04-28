graph = {}
visited = []
stack = []


def childadd():
    for x in parent:
        print("Enter the children of ", x, " node: ")
        child = list(input().split())
        graph[x] = child


def dfs(node):
    visited.append(node)
    stack.append(node)
    print(node, end=" ")
    if node in goal:
        print("\nActual path:")
        for i in stack:
            print(i, end=" ")
        print("\nGoal node", node, "found")
        exit(0)
    for y in graph[node]:
        if y not in visited:
            dfs(y)
            stack.pop()
            if(node != visited[-1]):
                print(node, end=" ")


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
    print("Following is the Depth-First Search")
    print("Traversal path:")
    dfs(root)
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
