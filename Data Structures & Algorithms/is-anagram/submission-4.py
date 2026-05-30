class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # have to be the same size
        if len(s) != len(t):
            return False

        # keep count of how many of each letter in each string
        # make a hashmap
        S = {}
        T = {}
        for i in range(len(s)):
            T[t[i]] = 1 + T.get(t[i],0)
            S[s[i]] = 1 + S.get(s[i],0)
        
        if T == S:
            return True
        return False