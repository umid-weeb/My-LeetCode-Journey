from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        count = 0
        visited = set()
        
    
        def dfs(node):
            for neighbor, connected in enumerate(isConnected[node]):
                if connected and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)


        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count +=1
        return count
                
        




        