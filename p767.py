class Solution:
    def __init__(self) -> None:
        pass

    def reorganizeString(self, s: str) -> str:
        h = {}
        # Count each letters
        # h[letter] = number of times this letter appears in string
        for c in s:
            if h.get(c):
                h[c] = h[c] +1
            else:
                h[c] = 1

        # ordered list of letters
        letters = []
        # weight of a letter is how many times this letter appears
        weights = []
        # sort letters and associated weight 
        for v,k in sorted( ((v,k) for k,v in h.items()), reverse=True):
            letters.append(k)
            weights.append(v)

        res = ""
        index = 0  
        while len(letters) > 0:
            res = res + letters[index]
            weights[index] = weights[index] - 1
           
            # last letter was consumed, remove this letter from the list
            if weights[index] == 0:
                del letters[index]
                del weights[index]
                index = 0
                # it was the last letter
                if len(letters) == 0:
                    return res
            # we have only this letter left, not possible to reorganize string
            elif len(letters) == 1:
                return ""
            else:
                swapped = False
                w0 = weights[index]
                # check if we need to move this letter downwards
                for i,w in reversed(list(enumerate(weights))):
                    if i > index and w > w0:
                        weights[index],weights[i] = weights[i],weights[index]
                        letters[index],letters[i] = letters[i],letters[index]
                        index = 0
                        swapped = True
                        break
                # no letter swapped, alternate between the two most frequent letters ( index 0 and 1 )
                if not swapped:
                    if index == 1:
                        index = 0
                    else:
                        index = 1

        return res

    


            

if __name__ == "__main__":
    sol = Solution()
    for t in ["aab","aabbbbcccd"]:
        res = sol.reorganizeString(t)
        print(res)