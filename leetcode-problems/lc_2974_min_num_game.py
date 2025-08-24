class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []

        while nums:
            alice_min = min(nums)
            nums.remove(alice_min)
            bob_min = min(nums)
            nums.remove(bob_min)

            arr.append(bob_min)
            arr.append(alice_min)
            

        return arr