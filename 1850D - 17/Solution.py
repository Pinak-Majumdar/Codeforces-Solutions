for _ in range(int(input())):
    n,k=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    mx,c=1,1
    for i in range(n-1):
        if l[i+1]-l[i]<=k:c+=1
        else:mx=max(mx,c);c=1
    mx=max(mx,c)
    print(n-mx)