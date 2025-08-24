class Solution:
    def sumOfMultiples(self, n: int) -> int:
        
        sum_ = 0

        for i in range(1,n+1):

            if i%3 == 0 and i%5 == 0 and i%7 == 0:
                sum_+=i
            elif i%3 == 0 and i%5 == 0:
                sum_+=i
            elif i%5 == 0 and i%7 == 0:
                sum_+=i
            elif i%3 == 0:
                sum_+=i
            elif i%5 ==0:
                sum_+=i
            elif i%7 == 0:
                sum_+=i

        return sum_