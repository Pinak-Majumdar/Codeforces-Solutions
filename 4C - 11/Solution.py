d={}
for _ in range(int(input())):
    s=input()
    print("OK" if s not in d else s+str(d[s]))
    d[s]=d.get(s,0)+1