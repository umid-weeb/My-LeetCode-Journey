from collections import deque, defaultdict
EMPTY = 0
FRESH = 1
ROTTON= 2
class Solution:

    def orangesRotting(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        maxtime = 0
        queue = deque()
        fresh_oranges = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==ROTTON:
                    queue.append((i, j, maxtime))
                elif matrix[i][j]==FRESH:
                    fresh_oranges +=1
        if fresh_oranges ==0:
            return 0
        while queue:
            i, j, time = queue.popleft()

            maxtime = max(time, maxtime)


            neighbors = [
                (i+1,j), (i,j+1),
                (i-1,j), (i,j-1),
            ]

            for ni, nj in neighbors:
                if (0<=ni<n and 0<= nj<m and matrix[ni][nj]==FRESH):

                    matrix[ni][nj] = ROTTON
                    fresh_oranges -=1
                    queue.append((ni, nj, time+1))
        return maxtime if fresh_oranges ==0 else -1
