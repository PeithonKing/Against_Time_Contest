for _ in range(int(input())):
    n, k, x, y = [int(x) for x in input().split()]
    c = x
    if n%k:
        print("YES")
    else:
        if x%k == y%k:
            print("YES")
        else:
            print("NO")