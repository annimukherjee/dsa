class Solution:
    def countDigits(self, num: int) -> int:
        
        num_copy = num
        digits = []
        while num!=0:
            digits.append(num%10)
            num //=10
        
        count = 0
        seen = []
        for i in digits:
            # if i in seen:
            #     continue
            # else:
            #     seen.append(i)

            if num_copy % i == 0:
                count+=1

        # print(digits)
        return count