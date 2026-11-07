class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq_of_s = {}
        freq_of_t = {}

        for i in range(len(s)):
            freq_of_s[s[i]] = freq_of_s.get(s[i],0) + 1
            freq_of_t[t[i]] = freq_of_t.get(t[i],0) + 1

        for key, value in freq_of_s.items():
            t_freq = freq_of_t.get(key)
            if t_freq !=value:
                return False

        return True
        