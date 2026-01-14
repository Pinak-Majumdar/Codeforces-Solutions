for _ in range(int(input())):
    n,k=map(int,input().split())
    if k==n:
        print(0)
        continue
    t=0
    while True:
        t+=1
        low=n//(2**t)
        high=(n+(2**t)-1)//(2**t)
        if low==k or high==k:
            print(t)
            break
        elif high<k:
            print(-1)
            break
        elif high==0:
            print(-1)
            break