class Solution:
    def __init__(self) -> None:
        pass
    def repeatedSubstringPattern(self, s: str) -> bool:
        total_len = len(s)
        for size in range(1,int(total_len/2)+1):
            pattern = s[0:size]
            psize = len(pattern)
            times = total_len / psize
            if not times.is_integer():
                continue
            else:
                times = int(times)

            generated_str = pattern * times
            print(generated_str)
            if generated_str == s:
                print("Found pattern, ",times)
                return True
        print("not found")
        return False

if __name__ == "__main__":
    sol = Solution()
    sol.repeatedSubstringPattern("abab")