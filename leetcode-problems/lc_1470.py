class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        l = []

        for i in range(0, len(nums)//2):
            l.append(nums[i])
            l.append(nums[len(nums)//2 + i])

        return l