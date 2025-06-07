class Solution:
    def checkRecord(self, s: str) -> bool:
        
        d = {'P':0, 'A':0, 'L': 0}
        late_consec = 0
        for i in s:
            # print(i)
            if i =='A':
                late_consec = 0
                d['A']+=1
            if d['A'] >= 2:
                return False
            if i == 'P':
                late_consec = 0
            
            if i == 'L':
                late_consec+=1
                d['L'] +=1
                if late_consec>=3:
                    return False
        # print(d)
        return True
                
                


