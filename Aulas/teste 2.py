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
M = []
M.append(L[0])
teste = False
x = 0
print(M)
while x < len(L):
    y = 0
    while y <= len(M):
        if y == len(M):
            M.append(L[x])
        elif L[x] != M[y]:
            y += 1
    x += 1
print(M)

         
    