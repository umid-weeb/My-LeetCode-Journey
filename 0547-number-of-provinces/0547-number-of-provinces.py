class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        visited = set()
        
        for i in range(n):
            if i not in visited:
                count+=1

                stack=[i]
                visited.add(i)
                while stack:
                    node = stack.pop()
                    for neighbor in range(n):
                        if isConnected[node][neighbor] ==1 and neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
        return count


        