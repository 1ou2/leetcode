import unittest

class Solution:
    def numberToWords(self, num: int) -> str:
        s = str(num)
        words = ""
        if num == 0:
            return "Zero"
        if num >= 1000000000000:
            # get trillions
            trillions = s[0:-12]
            remaining = int(s[len(trillions):])
            words = words + self.numberToWords(int(trillions)) + " Trillion" 
            if remaining:
                words = words + " " + self.numberToWords(remaining)
            
        elif num >= 1000000000:
            # get billions
            billions = s[0:-9]
            remaining = int(s[len(billions):])
            words = words + self.numberToWords(int(billions)) + " Billion"
            if remaining:
                words = words + " " + self.numberToWords(remaining)
        elif num >= 1000000:
            # get millions
            millions = s[0:-6]
            remaining = int(s[len(millions):])
            words = words + self.numberToWords(int(millions)) + " Million" 
            if remaining:
                words = words + " " + self.numberToWords(remaining)
        elif num >= 1000:
            # get thousands
            thousands = s[0:-3]
            remaining = int(s[len(thousands):])
            words = words + self.numberToWords(int(thousands)) + " Thousand" 
            if remaining:
                words = words + " " + self.numberToWords(remaining)
        elif num >= 100:
            hundreds = s[0:-2]
            remaining = int(s[len(hundreds):])
            words = words + self.numberToWords(int(hundreds)) + " Hundred"
            if remaining:
                words = words + " " + self.numberToWords(remaining)
        elif num >=20:
            
            remaining = int(s[1])
            words = words + self.tens(int(s[0]))
            if remaining:
                words = words + " " + self.numberToWords(remaining)
        else:
            words = words + self.units(num)
        return words
    
    def tens(self,digit: int) -> str:
        t = {1:"Ten",2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
        return t[digit]
    
    def units(self,digit: int) -> str:
        u = {0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        return u[digit]
    
      

class TestSolution(unittest.TestCase):
    def test_case1(self):
        num = 123
        s = Solution()
        self.assertEqual(s.numberToWords(num),"One Hundred Twenty Three")

    def test_case2(self):
        num = 12345
        s = Solution()
        self.assertEqual(s.numberToWords(num),"Twelve Thousand Three Hundred Forty Five")


    def test_case3(self):
        num = 1234567
        s = Solution()
        self.assertEqual(s.numberToWords(num),"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")

    def test_case4(self):
        num = 0
        s = Solution()
        self.assertEqual(s.numberToWords(num),"Zero")


if __name__ == "__main__":
    unittest.main()
    s = Solution()
    print(s.numberToWords(1100000000040))