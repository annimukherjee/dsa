s = input().split(" ")

n = int(s[0])
k  = int(s[1])

a = list(map(int, input().split(" ")))

if n==k:
    k-=1

count = 0
for i in a:
    # print(i)
    # print(f"{i}, {a[k]}")
    if i >= a[k] and i > 0:
        count+=1

print(count)

