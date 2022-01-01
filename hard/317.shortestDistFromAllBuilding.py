from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        use dfs to find shortest paths from every building to every empty space
        decrement empty space by 1 for every bfs starting from a building
        only search throught these decremented empty space in the next round
        """
        
        def bfs(source, grid, dist_mx, empty_val):
            step = 0
            # traverse the grid
            m, n = len(grid), len(grid[0])
            queue = deque([source])
            new_val = empty_val
            while len(queue) > 0:
                step += 1
                level_cnt = len(queue)
                for i in range(level_cnt):
                    (x,y) = queue.popleft()
                    # add neibor vertices(up, down, left, right) with empty_val
                    # add dist to dist_mx if applicable
                    if y-1>=0 and grid[x][y-1] == empty_val:
                        queue.append((x,y-1))
                        grid[x][y-1] = empty_val-1
                        new_val = empty_val -1
                        dist_mx[x][y-1] += step
                    if y+1<n and grid[x][y+1] == empty_val:
                        queue.append((x,y+1))
                        grid[x][y+1] = empty_val-1
                        new_val = empty_val -1
                        dist_mx[x][y+1] += step
                    if x-1>=0 and grid[x-1][y] == empty_val:
                        queue.append((x-1,y))
                        grid[x-1][y] = empty_val-1
                        new_val = empty_val -1
                        dist_mx[x-1][y] += step
                    if x+1<m and grid[x+1][y] == empty_val:
                        queue.append((x+1,y))
                        grid[x+1][y] = empty_val-1
                        new_val = empty_val -1
                        dist_mx[x+1][y] += step
                    #print(dist_mx)
            return new_val
            
        
        # main function
        # get all building
        buildings = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append((i,j))
        
        # bfs to fill up dist_mx
        dist_mx = [[0 for j in range(n)] for i in range(m)]
        
        empty_val = 0
        for i in range(len(buildings)):
            source = buildings[i]
            #empty_val = -i
            new_val = bfs(source, grid, dist_mx, empty_val)
            if new_val == empty_val: # space reachable by i-1 cannot be reach by i, sol DNE
                return -1
            else: empty_val = new_val
        # print(grid)
        # print(dist_mx)
        # find the min
        minVal = -1
        for i in range(m):
            for j in range(n):
                #print(grid[i][j],minVal ,dist_mx[i][j])
                if grid[i][j] == empty_val and (dist_mx[i][j] < minVal or minVal < 0) :
                    minVal = dist_mx[i][j]
        return minVal

                    
                    
            
            