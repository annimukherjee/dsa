# https://codeforces.com/problemset/problem/282/A

c = int(input())
x = 0
for i in range(c):
    s = input()
    if '++' in s:
        x+=1
    if '--' in s:
        x-=1

print(x)
