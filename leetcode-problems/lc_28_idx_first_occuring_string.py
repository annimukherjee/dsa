class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        success = 0
        first_idx = 0

        for i in range(0, len(haystack) - len(needle) + 1):
            c = 0

            for j in range(len(needle)):
                if needle[j] == haystack[i + j]:
                    c += 1
                    if c == len(needle):
                        first_idx = (i + j) - len(needle) + 1
                        success = 1
                        break

            if success == 1:
                return first_idx
                break

        return -1
