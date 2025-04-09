class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n2 = 0

        for i in range(len(digits)-1 , -1, -1):
            # print(digits[i])
            n2 = n2 + digits[i]*(10**(len(digits)-(i+1)))
        
        n2 +=1
        

        new_l = []
        while n2 > 0:
            print(n2%10)
            new_l.append(n2%10)
            n2 = n2 // 10
        
        return (new_l[::-1])
