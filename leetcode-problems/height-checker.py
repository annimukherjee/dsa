class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        print(expected)
        counter = 0
        for i, j in zip(heights, expected):
            if i != j:
                counter += 1

        return counter
