L = []
print("Digite 5 elementos:")
for i in range(5):
    x = input(">>")
    L.append(x)
V = L[:]
del V[2]
del V[0]
del V[2]
print(L)
print(V)