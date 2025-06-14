class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = list(s)
        for j in t:
            if j in s_list:
                s_list.remove(j)
                continue
            else:
                return j
            