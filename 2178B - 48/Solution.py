for _ in range(int(input())):
    s=input().strip()
    n=len(s)
    total_u=s.count('u')
    kept=0
    last_kept=-2
    for i in range(1,n-1):
        if s[i]=='u' and i-last_kept>=2:
            kept+=1
            last_kept=i
    print(total_u-kept)