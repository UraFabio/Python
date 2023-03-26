def semElementosDuplicados(lista):
    novaLista = list(set(lista))
    return novaLista

Lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print(semElementosDuplicados(Lista))