class Solution:
    def __init__(self) -> None:
        pass
    def twoSum1(self, nums, target: int):
        nums.sort()
        rnums = reversed(nums)
        
        for i,a in enumerate(nums):
            
            for j,b in enumerate(rnums):
                if b > 0 and a >= target:
                    break
                elif b < 0 and a <= target:
                    break
                if i == len(nums)-j:
                    break
                if a+b == target:
                    print("found",a,b,i,j)
                    return[i,len(nums)-j-1]

    def twoSum(self, nums, target: int):
        h = {}
        # create hashmap in order to get the right index
        for i,a in enumerate(nums):
            if h.get(a):
                h[a].append(i)
            else:
                h[a] = list()
                h[a].append(i)
        nums.sort()
        rnums = [x for x in reversed(nums)]
        
        for i,a in enumerate(nums):
            
            for j,b in enumerate(rnums):
                if b > 0 and a >= target:
                    continue
                elif b < 0 and a <= target:
                    break
                if i == len(nums)-j:
                    break
                if a+b == target:
                    print("found",a,b,i,j)
                    if len(h[a]) == 1:
                        return[h[a][0], h[b][0]]
                    else:
                        return[h[a][0],h[a][1]]

if __name__ == "__main__":
    sol = Solution()
    res = sol.twoSum(nums = [0,4,0,3], target = 0)
    print(res)
    res = sol.twoSum(nums = [3,2,3], target = 6)
    print(res)
    res = sol.twoSum(nums = [2,7,11,15], target = 9)
    print(res)
    res = sol.twoSum(nums = [3,2,4], target = 6)
    print(res)
    res = sol.twoSum(nums = [3,3], target = 6)
    print(res)