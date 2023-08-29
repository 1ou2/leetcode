class Solution:
    def __init__(self) -> None:
        pass

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #print(s1,s2,s3)
        #res = ""
        alternate = []
        for i,c in enumerate(s3):
            # found a match in s1
            if len(s1) and c == s1[0]:
                # s2 also matches
                if len(s2) and c == s2[0]:
                    if i < len(s3) -2:
                        #alter = s2[0]
                        alternate.append((s1,s2[1:],s3[i+1:])) 
                
                #res = res + c
                s1 = s1[1:]
            else:
                # only s2 matches
                if len(s2) and c == s2[0]:
                    #res = res + c
                    s2 = s2[1:]
                # no match
                else:
                    for branch in alternate:
                        result = self.isInterleave(*branch)
                        if result:
                            return result
                    return False
        # make sure all characters were used
        if not s1 and not s2:
            return True
        else:
            return False

class Solution2D:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[m][n]

class Solution1D:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        if m < n:
            return self.isInterleave(s2, s1, s3)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[n]
    
if __name__ == "__main__":
    sol = Solution2D()
    res = sol.isInterleave(s1 = "a", s2 = "b", s3 = "a")
    print("Result = ", res)
    res = sol.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")
    print("Result = ", res)
    res = sol.isInterleave(s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")
    print("Result = ", res)