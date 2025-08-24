class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        result_list = []

        for i in range(len(nums)):
            smaller_than_i = 0
            for j in range(len(nums)):

                if nums[i] > nums[j]:
                    smaller_than_i+=1
            
            result_list.append(smaller_than_i)
            smaller_than_i = 0
        
        return result_list