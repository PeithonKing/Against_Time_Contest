for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    ans = 0
    i = k-1
    while i<len(a):
        s = sum(a[i-k:i])
        if s>ans:
            ans = s
        i += 1
    print(ans)