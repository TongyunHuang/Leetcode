from collections import deque
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        Idea
        - Traverse the grid
            - When you find a '1', perform dfs from that node and mark all cell the same number
            - Use hashmap to record area of each component
        - Traverse again
            - find all the block that connect two different components
        """
        # find all the connected components
        area_dic = {}
        component_cnt = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # bfs starting from cell (i,j)
                    area = 1
                    queue = deque([(i,j)])
                    grid[i][j] = component_cnt
                    while len(queue) > 0:
                        (x,y) = queue.popleft()
                        for neigh in {(x,y-1),(x,y+1),(x-1,y),(x+1,y)}:
                            
                            if neigh[0] in range(0,len(grid)) and neigh[1] in range(0, len(grid[0])) and grid[neigh[0]][neigh[1]] == 1:
                                queue.append(neigh)
                                area += 1
                                grid[neigh[0]][neigh[1]] = component_cnt
                    # add area to hashmap and increment component count
                    area_dic[component_cnt] = area
                    component_cnt += 1
        # print(area_dic)
        if len(area_dic) == 0: return 1
        newAreas = []
        # find pairs of components that can connected by one cell
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    components = []
                    newArea = 1
                    for neigh in {(i,j-1),(i,j+1),(i-1,j),(i+1,j)}:
                        if neigh[0] in range(0,len(grid)) and neigh[1] in range(0, len(grid[0])) \
                        and grid[neigh[0]][neigh[1]] not in components and grid[neigh[0]][neigh[1]]>1 :
                            components.append(grid[neigh[0]][neigh[1]])
                    
                    for k in components:
                        newArea += area_dic[k]
                    if newArea != 1:
                        newAreas.append(newArea)
                    
        # print(newAreas) 
        if len(newAreas) == 0:
            return max(area_dic.values())
        return max(newAreas)
                    
                    
                