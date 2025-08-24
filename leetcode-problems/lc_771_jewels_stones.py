class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total_jewels = 0

        for j in jewels:
            for st in range (len(stones)):
                if stones[st] == j:
                    total_jewels+=1
        

        return (total_jewels)