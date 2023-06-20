# In the village there are some houses and some stores that are represented in a 2-D Matrix. Houses are represented by ‘H’ and stores are represented by ‘S’. The task is to find the minimum moves to reach the store from all the houses.

# Input -

# H H H S H H H
# S H H H H S H
# H H H H H H H

# Output -

# 1 2 1 0 1 1 2
# 0 1 2 1 1 0 1
# 1 2 3 2 2 1 2

# Constraints - N,M = 10^3

import numpy as np

mat = open('test_mbfs.txt', 'r').readlines()
grid =[]
for line in mat:
    grid.append(line.split())

grid = np.array(grid)
grid = np.where(grid=='S',0,grid.shape[0] + grid.shape[1])
print(grid)

class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getNbrs(self,grid):
        nbrs = []
        offsets = [(0,1), (0,-1), (1,0), (-1,0)]
        for offset in offsets:
            new_x = self.x + offset[0]
            new_y = self.y + offset[1]

            if 0<=new_x<grid.shape[0] and 0<=new_y<grid.shape[1]:
                nbrs.append(Cell(new_x,new_y))
        return nbrs

visited = {}
frontier = []
coords = np.where(grid==0)
for cell in np.array(coords).T:
    shop = Cell(cell[0],cell[1])
    frontier.append(shop)
    visited[(shop.x,shop.y)] = 0


while len(visited.keys())<grid.shape[0]*grid.shape[1]:
    curr_cell = frontier.pop(0)
    nbrs = curr_cell.getNbrs(grid)
    for nbr in nbrs:
        if (nbr.x,nbr.y) in visited:
            # print('visited')
            pass
        else:
            visited[(nbr.x,nbr.y)] = visited[(curr_cell.x,curr_cell.y)] + 1
            frontier.append(nbr)

# print(len(visited.keys()))

for key in visited.keys():
    grid[key[0],key[1]] = visited[key]

print(grid)
        
# for x in grid:
#     for y in 
# if cell value = 0:
#     add cell to frontier
#    add each to visited

# for each cell in frontier:
#     remove the Cell
#     find its neighbors
#     if nbr in visited
#         skip
#     else    
#         give nbrs cost = cost + 1
#         add nbr to visited
#         append nbr to frontier
