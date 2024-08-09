try:
    from typing import List
except:
    pass

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        nbmagic = 0
        rows = len(grid)
        if rows < 3:
            return 0
        if grid[0]:
            cols = len(grid[0])
        else:
            cols = 0
        if cols < 3:
            return 0

        rowslice,colslice = [],[]
        
        for i in range(rows):
            if i + 2 < rows:
                rowslice.append([i,i+1,i+2])
        
        for i in range(cols):
            if i + 2 < cols:
                colslice.append([i,i+1,i+2])

        for rslice in rowslice:
            for cslice in colslice:
                g = []
                for r in rslice:
                    row = []
                    for c in cslice:
                        row.append(grid[r][c])
                    g.append(row)
                
                if self.isMagic(g):
                    nbmagic+=1
        
        return nbmagic
        
    def isMagic(self, grid):
        numbers = set()
        for r in grid:
            numbers.update(r)

        if numbers != set(range(1,10)):
            return False
        
        total = sum(grid[0])
        for r in grid:
            if sum(r) != total:
                return False
        
        diag = 0
        for i in range(3):
            diag += grid[i][i]

        if diag != total:
            return False
        
        diag2 = grid[0][2] + grid[1][1] + grid[2][0]
        if diag2 != total:
            return False

        
        colsum = 0
        for i in range(3):
            colsum = 0
            for j in range(3):
                colsum += grid[j][i]
            if colsum !=total:
                return False

        return True



import unittest

class TestSolution(unittest.TestCase):
    def test_case09(self):
        grid = [[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]]
        s = Solution()
        self.assertEqual(s.numMagicSquaresInside(grid),1)
    
    def test_case10(self):
        grid = [[5,5,5],[5,5,5],[5,5,5]]
        s = Solution()
        self.assertEqual(s.numMagicSquaresInside(grid),0)

    def test_case11(self):
        grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
        s = Solution()
        
        self.assertEqual(s.numMagicSquaresInside(grid),1)

    def test_case12(self):
        grid = [[2,7,6],[1,5,9],[4,3,8]]
        s = Solution()
        
        self.assertEqual(s.numMagicSquaresInside(grid),0)

    def test_case13(self):
        grid = [[4,3,8],[9,5,1],[2,7,6]]
        s = Solution()
        
        self.assertEqual(s.numMagicSquaresInside(grid),1)
    
    def test_case14(self):
        grid = [[4,3,8],[9,5,3],[2,7,6]]
        s = Solution()
        
        self.assertEqual(s.numMagicSquaresInside(grid),0)
if __name__ == "__main__":
    unittest.main()
