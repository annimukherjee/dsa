class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = []
        d={}
        for i in s:
            d[i] = True
        
        for i in s:
            if i in seen:
                d[i] = False
                seen.append(i)
            elif i not in seen:
                seen.append(i)
        
        for i in s:
            if i in seen and d[i]:
                return s.index(i)
        
        return -1
