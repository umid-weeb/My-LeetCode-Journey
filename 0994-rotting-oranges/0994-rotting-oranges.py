from collections import deque, defaultdict
EMPTY = 0
FRESH = 1
ROTTON= 2
class Solution:

    def orangesRotting(self, matrix: list[list[int]]) -> int:
        quueue = deque()
        n , m = len(matrix), len(matrix[0])
        maxtime = 0
  
        def bfs(matrix):

            nonlocal maxtime

            for i in range(n):
                for j in range(m):
                    if matrix[i][j]==ROTTON:
                        matrix[i][j] = FRESH
                        quueue.appendleft((i, j, 0))

            while quueue:
                i,j,time = quueue.pop()
                if matrix[i][j]!=FRESH:
                    continue

 
                maxtime = max(time, maxtime)
                matrix[i][j] = ROTTON
    
    #  matrix[i][j] =FRESH

                neighbors=[
                    (i+1,j),(i,j+1),
                    (i-1,j),(i,j-1),
                ]
                for ni, nj in neighbors:
                    if not (0<=ni<n and 0<=nj<m):
                        continue

                    if matrix[ni][nj]==FRESH:
                        quueue.appendleft((ni, nj, time+1))

        bfs(matrix)
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==FRESH:
                    return -1
        return maxtime



  