graphs = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
  }

visited=[]
queue=[]

def bfs(graphs,start):
      queue=[start]
      while queue:
            nodes=queue.pop(0)

            if nodes not in visited:
                  visited.append(nodes)
                  adjacent=graphs[nodes]

                  for adjacent in adjacent:
                        queue.append(adjacent)
      return visited
print(bfs(graphs,'A'))
                  
