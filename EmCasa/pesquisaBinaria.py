def pesquisaBinaria(item):
    lista = []
    for i in range(1001):
        lista.append(i)    
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto)/2
        tentativa = lista(meio)
        if tentativa == item:
            return meio
        elif tentativa > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None



item = int(input("Digite um número entre 0 e 1000:\n>>"))

print(pesquisaBinaria(item))
