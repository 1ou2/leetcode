class Solution:
    def __init__(self) -> None:
        pass
   
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        
        while columnNumber > 26:
            remainder = columnNumber % 26
            res =self.getalphabet(remainder) + res
            columnNumber = (columnNumber-1) // 26
    
        res = self.getalphabet(columnNumber) + res
        return res
        

    def getalphabet(self,num):
        alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        return alphabet[num-1]

if __name__ == "__main__":
    sol = Solution()
    for t in [1,28,52,701]:
        res = sol.convertToTitle(t)
        print(res)
    