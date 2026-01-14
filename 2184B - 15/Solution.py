for _ in range(int(input())):
    s, k, m = map(int, input().split())
    f=m//k
    t=m%k
    if f%2==0:
        se=s
    else:
        se=min(s,k)
    print(max(0,se-t))