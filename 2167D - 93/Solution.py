def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    x = 2
    while gcd(x, g) != 1:
        x += 1
    print(x)