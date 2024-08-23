import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerators = []
        denominators = []

        # split input string into a list of fractions
        pattern = re.compile("\+?-?\d+/\d+")
        fractions = pattern.findall(expression)

        # split each fractions, and store it in two arrays: numerators/denominators
        for f in fractions:
            numerators.append(int(f.split('/')[0]))
            denominators.append(int(f.split('/')[1]))

        denom =1 
        for x in denominators:
            denom = denom * x

        num = 0
        for n,d in zip(numerators,denominators):
            num = num + int(n * denom / d)

        # result is zero
        if num == 0:
            return "0/1"

        # reduce fraction
        # we know that all numbers are in range 1 .. 10
        primes = [2,3,5,7]
        for p in primes:
            while num % p == 0 and denom % p == 0:
                num = int(num/p)
                denom = int(denom/p)

        # switch signs
        if denom < 0:
            denom = - denom
            num = -num

        return f"{num}/{denom}"

import unittest
class TestSolution(unittest.TestCase):
    def test_case05(self):
        e = "-1/4-4/5-1/4"
        s = Solution()
        self.assertEqual(s.fractionAddition(e),"-13/10")
    
    def test_case06(self):
        e = "-5/1+8/1+1/1"
        s = Solution()
        self.assertEqual(s.fractionAddition(e),"4/1")
    

    def test_case07(self):
        e = "7/3+5/2-3/10"
        s = Solution()
        self.assertEqual(s.fractionAddition(e),"68/15")
    def test_case08(self):
        e = "7/2+2/3-3/4"
        s = Solution()
        self.assertEqual(s.fractionAddition(e),"41/12")

    def test_case09(self):
        e = "5/3+1/3"
        s = Solution()
        
        self.assertEqual(s.fractionAddition(e),"2/1")
    def test_case1(self):
        e = "-1/2+1/2"
        s = Solution()
        
        self.assertEqual(s.fractionAddition(e),"0/1")

    def test_case2(self):
        e = "-1/2+1/2+1/3"
        s = Solution()
        
        self.assertEqual(s.fractionAddition(e),"1/3")

    def test_case3(self):
        e = "1/3-1/2"
        s = Solution()
        
        self.assertEqual(s.fractionAddition(e),"-1/6")

if __name__ == "__main__":
    
    
    unittest.main()