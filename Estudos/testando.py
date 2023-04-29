n = int(input())

lista = list(range(n))
for i in range(n):
    lista[i] = i + 1

print(''.join(lista))