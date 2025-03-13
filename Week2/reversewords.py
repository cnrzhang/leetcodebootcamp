class Solution:
    def reverseWords(self, s: str) -> str:
        output = []
        for p in range(len(s)):
            if s[p] != " ": break

        for q in range(len(s)-1,-1,-1):
            if s[q] != " ": break

        s = s[p : q + 1]

        words = s.split()

        for k in range(len(words) - 1, 0, -1 ):
            output.append(words[k])
        output.append(words[0])

        return ' '.join(output)
        
