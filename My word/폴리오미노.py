X = list(input().split("."))


Xlist = []
PoliList = []
for i in X:
    if "X" in i:
        Xlist.append(i)

for i in Xlist:
    if len(i) % 4 == 0:
        PoliList.append("AAAA")
    if len(i) % 2 == 0:
        PoliList.append("BB")
    if len(i) % 4 == 2:
        PoliList.append("AAAA") * (len(i) // 4)
        PoliList.append("BB")
    else:
        PoliList.append("-1")

print("".join(PoliList)) if "-1" not in PoliList else print(-1)


X = input()

X = X.replace("XXXX", "AAAA")
X = X.replace("XX", "BB")

if "X" in X:
    print(-1)
else:
    print(X)