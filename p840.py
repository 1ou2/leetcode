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
            for row in rslice:
                g = []
                r = []
                for cslice in colslice:
                    for col in cslice:
                        r.append(grid[row][col])
                g.append(r)
                if self.isMagic(g):
                    nbmagic+=1  
        return nbmagic
        
    def isMagic(self, grid):
        for r in grid:
            if sum(r) != 15:
                return False
        
        diag = 0
        for i in range(3):
            diag += grid[i][i]

        if diag != 15:
            return False
        
        colsum = 0
        for i in range(3):
            colsum = 0
            for j in range(3):
                colsum += grid[i][j]
            if colsum !=15:
                return False

    



import unittest

class TestSolution(unittest.TestCase):
    def test_case1(self):
        grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
        s = Solution()
        
        self.assertEqual(s.numMagicSquaresInside(grid),1)

    def test_case2(self):
        grid = [[4,3,8,4]]
        s = Solution()
        
        self.assertEqual(s.numMagicSquaresInside(grid),0)

    def test_case3(self):
        grid = [[4,3,8],[9,5,1],[2,7,6]]
        s = Solution()
        
        self.assertEqual(s.numMagicSquaresInside(grid),1)
    
    def test_case4(self):
        grid = [[4,3,8],[9,5,3],[2,7,6]]
        s = Solution()
        
        self.assertEqual(s.numMagicSquaresInside(grid),0)
if __name__ == "__main__":
    unittest.main()
