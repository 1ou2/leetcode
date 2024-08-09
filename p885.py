try:
    from typing import List
except:
    pass

class Solution:
    def __init__(self) -> None:
        self.spiral = []
        self.visited = []
        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]
        self.currentDirection = 0
        

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        self.rows = rows
        self.cols = cols
       
        self.current = [rStart,cStart]
        self.spiral.append(self.current)
        while len(self.spiral) <rows*cols:
            # get the next cell where we should go
            [row,col] = self.getNextCell()
            # cell already visited,
            # we need to move in the same direction
            # place the direction
            if [row,col] in self.spiral:
                self.moveForward()
            else:
                # we found the new cell
                if self.is_valid([row,col]):
                    self.spiral.append([row,col])
                    
                self.current = [row,col]
                self.changeDirection()
            

        return self.spiral




    def getNextCell(self):
        row = self.current[0] + self.directions[self.currentDirection][0]
        col = self.current[1] + self.directions[self.currentDirection][1]

        return [row,col]

    def moveForward(self):
        self.currentDirection -=1
        if self.currentDirection == -1:
            self.currentDirection = 3


    def changeDirection(self):
        self.currentDirection +=1
        if self.currentDirection == 4:
            self.currentDirection = 0
    
    # check if a cell is in a valid range
    def is_valid(self,cell):
        if cell[0] < 0 or cell[0] >= self.rows:
            return False
        if cell[1] < 0 or cell[1] >= self.cols:
            return False
        return True



import unittest

class TestSolution(unittest.TestCase):
    def test_case1(self):
        rows,cols,rStart,cStart = 1, 4, 0, 0
        s = Solution()
        
        self.assertEqual(s.spiralMatrixIII(rows, cols, rStart, cStart),[[0,0],[0,1],[0,2],[0,3]])

    def test_case2(self):
        
        rows,cols,rStart,cStart = 5,6,1,4
        s = Solution()
        
        self.assertEqual(s.spiralMatrixIII(rows, cols, rStart, cStart),[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]])

    

if __name__ == "__main__":
    unittest.main()