class Solution:
    def isFascinating(self, n: int) -> bool:
        n_str = str(n)
        n_str_twice = str(n*2)
        n_str_thrice = str(n*3)

        concat_num = n_str + n_str_twice + n_str_thrice

        for i in range(0, 10):
            if i==0:
                if str(i) in concat_num:
                    return False
            else:
                if str(i) not in concat_num or int(concat_num.count(str(i)) > 1):
                    return False
                
            
        return True