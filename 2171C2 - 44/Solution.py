def score(l):
    s = 0
    for i in l:
        s ^= i
    return s
 
for _ in range(int(input())):
    n = int(input())
    aji = list(map(int,input().split()))
    mai = list(map(int,input().split()))
    scoreaji = score(aji)
    scoremai = score(mai)
    for i in range(n):
        newaji = scoreaji ^ aji[i] ^ mai[i]
        newmai = scoremai ^ mai[i] ^ aji[i]
        if i % 2 == 0:
            if aji[i] != mai[i]:
                if newaji > newmai:
                    aji[i], mai[i] = mai[i], aji[i]
                    scoreaji, scoremai = newaji, newmai
        else:
            if aji[i] != mai[i]: 
                if newmai > newaji:
                    aji[i], mai[i] = mai[i], aji[i]
                    scoreaji, scoremai = newaji, newmai
    if scoreaji > scoremai:
        print("Ajisai")
    elif scoremai > scoreaji:
        print("Mai")
    else:
        print("Tie")