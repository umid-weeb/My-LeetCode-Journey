from collections import deque, defaultdict
EMPTY = 0
FRESH = 1
ROTTON= 2
class Solution:
    def orangesRotting(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        queue = deque()
        countF = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==ROTTON:
                    queue.append((i, j))

                elif matrix[i][j]==FRESH:
                    countF +=1

        if countF ==0:
            return 0
        minuts = 0
        while queue and countF>0:
            minuts+=1
            for _ in range(len(queue)):

                i, j = queue.popleft()

                for ni, nj in [(i+1,j), (i,j+1),(i-1,j), (i,j-1),]:
                    if (0<=ni<n and 0<= nj<m and matrix[ni][nj]==FRESH):
                        matrix[ni][nj] = ROTTON
                        countF -=1
                        queue.append((ni, nj))
        return minuts if countF ==0 else -1
