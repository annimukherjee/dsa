# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    
    s_2 = ""
    for i in range(len(s)):
        
        if 'A'<=(s[i])<='Z':
            s_2 += s[i].lower()
        elif 'a'<=(s[i])<='z':
            s_2 += s[i].upper()
        else:
            s_2 += s[i]
        
    
    return s_2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)