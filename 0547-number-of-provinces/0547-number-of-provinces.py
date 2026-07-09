from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        count = 0
        visited = set()
        
        for i  in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(j)
        def dfs(graph, i, visited):
            if i  in visited: return
            visited.add(i)

            for j in graph[i]:
                if j not in visited:
                    dfs(graph, j, visited)

        for i in range(n):
            if i not in visited:
                dfs(graph, i, visited)
                count +=1
        return count
                
        




        