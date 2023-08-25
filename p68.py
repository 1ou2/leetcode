class Solution:
    def __init__(self) -> None:
        pass

    def fullJustify(self, words, maxWidth):
        lines = []
        line = []
        currentlen = 0
        for word in words:
            if len(line) == 0:
                # only one word in the line
                if len(word) >= maxWidth -1:
                    lines.append([word])
                    line = []
                else:
                    line = [word]
            else:
                wl = len(word)
                linelen = 0
                for w in line:
                    # +1 because there is a space after each word
                    linelen = linelen + len(w) + 1 
                # add this word to the current line as it fits maxWidth
                if linelen + wl <= maxWidth:
                    line.append(word)
                else:
                    lines.append(line)
                    line = [word]
        if line:
            lines.append(line)

        justifiedlines = []
        for i,l in enumerate(lines):
            # last line
            if i + 1 == len(lines):
                justifiedlines.append(self.justifyLine(l,maxWidth,True))
            else:
                justifiedlines.append(self.justifyLine(l,maxWidth,False))
        return justifiedlines

    def justifyLine(self,words,maxWidth,islastline=False):
        wl=0
        if len(words) == 1:
            return words[0].ljust(maxWidth)

        # last line is always left justified
        if islastline:
            line = ""
            for w in words[:-1]:
                line = line + w + " "
            line = line + words[-1]
            return line.ljust(maxWidth)
        
        # check length of all words
        for word in words:
            wl = wl+len(word)
        # number of spaces between words
        spacesize = (maxWidth - wl) // (len(words)-1)
        # but spaces are not evenly distributed
        # one extraspace added for the first spaces
        extraspaces = (maxWidth - wl) % (len(words)-1)
        line = ""
        for i,w in enumerate(words[:-1]):
            line = line + w + " "*spacesize
            if i < extraspaces:
                line = line + " "
        line = line + words[-1]
        return line

if __name__ == "__main__":
    sol = Solution()
    res = sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16)
    print(res)

    res = sol.fullJustify(["What","must","be","acknowledgment","shall","be"], maxWidth = 16)
    print(res)

    res = sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20)
    print(res)