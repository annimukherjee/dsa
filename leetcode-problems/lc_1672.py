class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        wealth = []
        for i in range(len(accounts)):
            s=0
            for j in range(len(accounts[0])):
                s+= accounts[i][j]
            
            wealth.append(s)
        
        return max(wealth)

