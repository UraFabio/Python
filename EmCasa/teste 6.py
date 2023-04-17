L = []
V = []
print("Adicione números à lista 'L'(0 para parar):\n")
while True:
    l = int(input(">>"))
    if l == 0:
        break
    L.append(l)
print("Agora adicione números à lista 'V'(0 para parar):\n")
while True:
    v = int(input(">>"))
    if v == 0:
        break
    V.append(v)
print(f"Lista 1: {L}")
print(f"Lista 2: {V}")
M = []
M.append(L[0])
x = 0
while x < len(L):
    y = 0
    while y <= len(M):
        if y == len(M):
            M.append(L[x])
        if L[x] != M[y]:
            y += 1
        elif L[x] == M[y]:
            break
    x += 1
x = 0
while x < len(V):
    y = 0
    while y <= len(M):
        if y == len(M):
            M.append(V[x])
        if V[x] != M[y]:
            y += 1
        elif V[x] == M[y]:
            break
    x += 1
M.sort()
print(f"Lista 3: {M}")