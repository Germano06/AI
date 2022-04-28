from sqlalchemy import false


graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],
    'B': ['F', 'G'],
    'C': ['H'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'H': ['I', 'J'],
    'I': ['K', 'L', 'M'],
    'J': [],
    'K': [],
    'L': [],
    'M': []
}
heu = {
    'S': 100,
    'A': 2,
    'B': 6,
    'C': 5,
    'D': 10,
    'E': 8,
    'F': 13,
    'G': 14,
    'H': 7,
    'I': 5,
    'J': 6,
    'K': 1,
    'L': 0,
    'M': 1
}
parent = ['S', 'A', 'B', 'C', 'H', 'I']
leaf = ['D', 'E', 'F', 'G', 'J', 'K', 'L', 'M']
visited = []
queue = []
q = []


def qsort():
    for i in range(len(q)-1):
        min = heu[q[i]]
        l = i
        for j in range(i+1, len(q)):
            y = heu[q[j]]
            if min > y:
                min, l = y, j
        q[i], q[l] = q[l], q[i]


def acPath(v):
    queue.append(v)
    if v in goal:
        print(queue)
        print("Goal node found")
        exit(0)
    for x in graph[v]:
        if x in visited:
            acPath(x)
            queue.pop()


def bbfs(node):
    q.append(node)
    while q:
        qsort()
        m = q.pop(0)
        visited.append(m)
        if m in goal:
            print(visited)
            print("The actual path: ")
            acPath(root)
        for x in graph[m]:
            if x not in visited:
                q.append(x)


root = parent[0]
print("Enter the goal nodes: ")
goal = list(input().split())
if root in goal:
    print("Root node is the goal node")
else:
    print("Following is the BEST-First Search")
    print("The traversal path:")
    bbfs(root)
    print(visited)
    print("\nGoal node not found")
