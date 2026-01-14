for _ in range(int(input())):
    n, l, r = map(int, input().split())
    ar = list(map(int, input().split()))
    ar.sort()
    m = ar[n // 2]
    m = min(r, max(l, m))
    ans = 0
    for i in range(n):
        ans += abs(ar[i] - m)
    print(ans)