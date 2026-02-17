n=int(input())
a=list(map(int,input().split()))
l=0
while l+1<n and a[l]<=a[l+1]:l+=1
if l==n-1:print("yes");print(1,1);exit()
r=l
while r+1<n and a[r]>=a[r+1]:r+=1
a[l:r+1]=reversed(a[l:r+1])
if all(a[i]<=a[i+1] for i in range(n-1)):print("yes");print(l+1,r+1)
else:print("no")