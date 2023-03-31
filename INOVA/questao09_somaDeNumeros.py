def soma(numeros):
    a = numeros.split(",")
    soma = 0
    for i in a:
        soma += float(i) 
    return soma


texto = "1,3,4,6,10,76"
print(soma(texto))
