def two_num(a, b, t):
    for i in range(1, t+1):
        if not i % 2 == 0:
            a = a*2
        else:
            b = b*2
    return (max(a,b)//min(a,b))

for _ in range(int(input())):
    a,b,n = map(int,input().split())
    print(two_num(a, b, n))
