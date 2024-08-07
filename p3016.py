import unittest

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = dict()
        ordered = dict()
        
        # count number of occurences of each letter
        for letter in word:
            count[letter] = count.get(letter,0) +1
        
        #ordered = {k:v for k,v in reversed(sorted(count.items(), key=lambda item:item[1]))}
        #print(ordered)
        letters_count = list(reversed(sorted(count.values())))
        
        rank = 1
        index = 1
        pushes = 0
        for c in letters_count:
            
            pushes = pushes + c*rank
            #print(f"count {c} - index {index} - rank {rank} - pushes {pushes}")
            index +=1
            if index == 9:
                rank +=1
                index = 1
        
        return pushes

class TestSolution(unittest.TestCase):
    def test_case1(self):
        w = "abc"
        s = Solution()
        
        self.assertEqual(s.minimumPushes(w),3)

    def test_case2(self):
        w = "aabbccddeeffgghhiiiiii"
        s = Solution()
        
        self.assertEqual(s.minimumPushes(w),24)

    def test_case3(self):
        w = "xyzxyzxyzxyz"
        s = Solution()
        
        self.assertEqual(s.minimumPushes(w),12)

if __name__ == "__main__":
    unittest.main()