class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Initialize the grid filled with obstacles ('#')
        grid = [['#' for _ in range(n)] for _ in range(m)]
        
        # Mark the top row as free cells ('.' )
        for j in range(n):
            grid[0][j] = '.'
            
        # Mark the rightmost column as free cells ('.')
        for i in range(m):
            grid[i][n - 1] = '.'
            
        # Convert each row list into a string
        return ["".join(row) for row in grid]