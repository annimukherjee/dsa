class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_chars = []
        for i in t:
            t_chars.append(i)
        
        for i in s:
            if i in t_chars:
                t_chars.remove(i)
            else:
                return False

        if len(t_chars) == 0:
            return True
        else:
            return False