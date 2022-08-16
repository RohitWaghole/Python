
def dfs(i):
    
    if not visited[i]:
        result.append(i)
        visited[i] = 1
        for t in adj[i]:
            if not visited[t]:
                dfs(t)
    

edges = [[1,2],[2,4],[2,7],[4,6],[7,6],[3,5]]

n = 7

adj = [[] for i in range(n+1)]
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)
    

result = []
visited = [0]*(n+1)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)

print(result)

