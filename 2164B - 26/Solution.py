for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    p = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if (l[j]%l[i])%2==0:
                print(l[i],l[j])
                p = 1
                break
        if p:
            break
    if not p:
        print(-1)