class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_concat = []
        nums_concat.extend(nums)
        nums_concat.extend(nums)
        print(nums_concat)
        
        return nums_concat