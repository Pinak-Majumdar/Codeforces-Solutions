for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mp={}
    ans=0
    for i in range(n):
        k=a[i]-(i+1)
        ans+=mp.get(k,0)
        mp[k]=mp.get(k,0)+1
    print(ans)