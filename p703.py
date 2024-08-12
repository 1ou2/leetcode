try:
    from typing import List
except:
    pass

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k-1
        self.nums = list(reversed(sorted(nums)))

    def add(self, val: int) -> int:
        for i,v in enumerate(self.nums):
            if val > v:
                self.nums = self.nums[:i] + [val] + self.nums[i:]
                return self.nums[self.k]
        self.nums.append(val)
        return self.nums[self.k]

import unittest

class TestKthLargest(unittest.TestCase):
    def test_case09(self):
        k = 3
        nums = [4, 5, 8, 2]
        adds = [3, 5, 10, 9, 4]
        kth = KthLargest(k,nums)
        print(kth.nums)
        for v in adds:
            out = kth.add(v)
            print(kth.nums)
            print(out)

        self.assertTrue(len(kth.nums)>=1)

if __name__ == "__main__":

    unittest.main()
