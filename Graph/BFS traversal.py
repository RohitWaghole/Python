
def bfs(i):
    queue = []
    queue.append(i)
    visited[i] = 1
    while queue:
        
        node = queue.pop(0)
        result.append(node)
        
        for t in adj[node]:
            if visited[t]==0:
                queue.append(t)
                visited[t] = 1
        

edges = [[1,2],[2,3],[2,4],[4,5],[3,5],[6,7]]

adj = [[] for i in range(len(edges)+2)]

for u,v in edges:
    
    adj[u].append(v)
    adj[v].append(u)
    
result = []
visited = [0]*len(edges)+2)

for i in range(1,len(visited)):
    if visited[i]==0:
        bfs(i)
        
print(result)
