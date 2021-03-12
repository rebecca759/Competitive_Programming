def bfs(visited,graph,node):
    visited = set() #set to keep track of visited nodes

    queue = []
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end = " ")


        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
