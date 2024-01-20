# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 100
#     -100 <= grid[i][j] <= 100

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid) - 1
        n = len(grid[0]) - 1

        i = 0
        j = m
        neg = 0

        while j!=-1:
            print(j,i)
            if grid[j][i] < 0:
                j-=1
                neg += n - i + 1
            else:
                if i==n:
                    break
                i+=1
            print(neg)
        return neg

        # starty = 0 
        # endy = m

        # while starty<=endy:
        #     midy = starty + (endy-starty)//2
        #     if grid[midy]<0:
        #         if midy>0:
        #             if grid[midy-1]>=0:
        #                 j = midy-1
        #         else:
        #             j = -1
                