graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        s=queue.pop(0)
        print(s,end='')

        for adjacent in graph[s]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(adjacent)

bfs(visited,graph,'A')
