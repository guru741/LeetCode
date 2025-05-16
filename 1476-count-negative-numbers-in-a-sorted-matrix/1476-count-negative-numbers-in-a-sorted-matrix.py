class Solution(object):
    def countNegatives(self, grid):
        m,n = len(grid),len(grid[0])
        row,col,count = 0,n - 1,0

        while m > row and col >= 0:
            if grid[row][col] < 0:
                count += (m - row)
                col -= 1
            else:
                row += 1
        return count