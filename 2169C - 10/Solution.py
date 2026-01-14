import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    maxg = 0
    current = 0
    for i in range(n):
        new = 2*(i+1) - a[i]
        current = max(new, current + new)
        maxg = max(maxg, current)
    print(total + maxg)