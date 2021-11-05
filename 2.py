for _ in range(int(input())):
    basic = float(input())
    if basic<1500:
        HRA = 0.1*basic
        DA = 0.9*basic
    else:
        HRA = 500
        DA = 0.98*basic
    print("\t", basic+HRA+DA)