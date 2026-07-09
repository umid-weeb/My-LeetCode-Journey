class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
    
        n = len(isConnected)

        count = 0
        visited = set()

        def dfs(isConnected, i, visited):
            if i in visited: return
            visited.add(i)

            for j , connected in enumerate(isConnected[i]):
                if connected:
                    dfs(isConnected, j, visited)

        for i in range(n):
            if i not in visited:
                dfs(isConnected,i , visited)
                count +=1
        return count
        

        