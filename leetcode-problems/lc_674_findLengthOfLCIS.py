# findLengthOfLCIS

# Longest Continuous Increasing Subsequence

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        max_lengths = []
    

        for i in range(len(nums)):
            # print(f"i: {i}")
            length = 1
            flag=0
            # print(f"j from {i+1} to {len(nums)}")
            # print(nums)
            for j in range(i+1, len(nums)):
                prev = nums[j-1]
                # print(f"j:{j}\t\tprev(nums[{j-1}]): {prev}\tcurr: {nums[j]}")
                if nums[j] > prev:
                    length +=1
                    # print(f"in if, length: {length}")
                else:
                    max_lengths.append(length)
                    flag=1
                    # print(f"in else; max_lengths: {max_lengths}")
                    break
            # print("j loop over----")
            if flag==0:
                max_lengths.append(length)
        
        return max(max_lengths)
