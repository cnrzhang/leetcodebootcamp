class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        res = []
        i = 0
        min = -2**31
        max = 2**31 - 1
        sign = 1
        if s[0] == "-":
            sign = -1
            i += 1
        while i < len(s) and s[i].isnumeric():
            res.append(s[i])
            i += 1
        if not res:
            return 0
            
        num = int("".join(res)) * sign
        if num < min:
            return min

        if num > max:
            return max
        return num
        