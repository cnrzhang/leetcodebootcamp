class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        c_freq = defaultdict(int)
        anagrams = []
        if len_p > len_s:
            return anagrams;
        
        for char in p:
            c_freq[char] += 1
        
        for i in range(len_p - 1):
            if s[i] in c_freq:
                c_freq[s[i]] -= 1

        for i in range(-1, len_s - len_p + 1):
            if i > -1 and s[i] in c_freq:
                c_freq[s[i]] += 1
            if i + len_p < len_s and s[i + len_p] in c_freq:
                c_freq[s[i+len_p]] -= 1

            if not any (c_freq.values()):
                anagrams.append(i+1)
        return anagrams

