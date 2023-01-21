class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False

        hashmapS, hashmapT = {}, {}

        for i in range(len(s)):
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)

        for j in hashmapS:
            if hashmapS[j] != hashmapT.get(j, 0):
                return False
        return True

