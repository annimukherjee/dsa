class Solution:
    def addDigits(self, num: int) -> int:
        
        def add_all_digist_of_a_num(n):
            sum_=0
            while n!=0:
                digit = n%10
                sum_ = digit + sum_
                n//=10

            return sum_
        
        while num//10 !=0:
            num = add_all_digist_of_a_num(num)
        
        return num

        
        
