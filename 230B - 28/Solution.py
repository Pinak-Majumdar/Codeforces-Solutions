def check(x):
    y=int(x**0.5)
    if y*y!= x:return False
    if y<2:return False
    for i in range(2,int(y**0.5)+1):
        if y%i==0:return False
    return True
n=int(input())
l=list(map(int,input().split()))

for i in l:
    print("YES" if check(i) else "NO")