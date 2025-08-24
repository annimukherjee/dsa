# https://codeforces.com/problemset/problem/231/A

n=int(input())
attempt=0

for i in range(n):
    s = input().split()
    c = s.count('1')
    # print(c)
    
    if c>=2:
        attempt+=1
    
print(attempt)