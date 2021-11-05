for _ in range(int(input())):
    X = input()
    Y = input()
    Z = ""
    l = len(X)
    i = 0
    while i<l:
        if X[i] == Y[i]:
            if X[i] == "W": Z += "B"
            else: Z += "W"
        else: Z += "B"
        i += 1
    print("\t", Z)