with open("INOVA/numbers.txt", "r") as n:
    numeros = [int(x) for x in n.readlines()]
    numeros_pares = sorted(list(filter(lambda x: (x%2)==0, numeros)))
    soma = sum(numeros_pares[-1:-6:-1])
    print(f"Cinco maiores valores pares: {numeros_pares[-1:-6:-1]}")
    print(f"Soma dos cinco maiores valores pares = {soma}")