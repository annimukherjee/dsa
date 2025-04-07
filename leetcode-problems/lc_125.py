class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = s.replace(" " , "")
        s2 = ""
        for x in s:
            if 'a' <= x <= 'z' or  '0' <= x <= '9':
                s2 +=x
        
        s = s2

        # print(s)

        s_rev = s[::-1]
        # print(s_rev)
        # print(s)
        if s == s_rev:
            return True
        else:
            return False