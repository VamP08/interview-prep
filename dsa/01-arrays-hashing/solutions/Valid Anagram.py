class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs = {}
        for i in range(len(s)):
            if s[i] in hs:
                hs[s[i]] += 1
            else:
                hs[s[i]] = 1

            if t[i] in hs:
                hs[t[i]] -= 1
            else:
                hs[t[i]] = -1
        if set(hs.values())=={0}:
            return True
        else:
            return False
        
