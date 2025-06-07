# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()
    first =arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i] == first:
            continue
        else:
            print(arr[i])
            break
