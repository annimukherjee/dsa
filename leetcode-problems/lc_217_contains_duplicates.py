class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        app = set()
        for i in nums:
            if i not in app:
                app.add(i)
            else:
                return True
        
        return False