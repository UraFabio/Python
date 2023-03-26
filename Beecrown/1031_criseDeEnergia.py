"""def intervalo_minimo(cidades):
    while True:
        a = list(range(1,cidades+1))
        m = 1
        x = []
        x.append(a[0])
        a.pop(0)
        while len(a) != 0:
            while m > len(a):
                m = m - len(a)
            x.append(a[m-1])
            a.pop(m-1)      
            m = m+m
        if x[-1] == 13:
            break
        m += 1
    return m

lista = []
while True:
    n = int(input())
    if n == 0:
        break
    lista.append(n)
for cidades in lista:
    print(intervalo_minimo(cidades))
"""
def intervaloMinimo(lista, numero):
    m = 1
    for a in range(numero-1):
        lista.pop(m-1)
        if lista == [13]:
            return m



lista = []
while True:
    n = int(input())
    if n == 0:
        break
    lista.append(n)
for numeroDeCidades in lista:
    ListaDeCidades = list(range(1,numeroDeCidades+1))
    print(intervaloMinimo(ListaDeCidades, numeroDeCidades))



        

