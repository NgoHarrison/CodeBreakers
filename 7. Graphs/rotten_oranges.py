

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        fresh = 0
        queue = collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]== 1:
                    fresh +=1
                elif grid[i][j]==2:
                    queue.append((i,j))
        
        res = 0
        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for hor,vert in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0 <= hor < row and 0 <= vert < col and grid[hor][vert]==1:
                        grid[hor][vert]=2
                        fresh -= 1
                    
                        queue.append((hor,vert))
            res += 1
        
        if fresh == 0:
            return max(0,res-1)
        else:
            return -1
                    
