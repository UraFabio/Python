def conta_vogais(string):
    vogais = ["a","e","i","o","u"]
    contagem = list(filter(lambda x:x in vogais, string.lower()))
    print(contagem)
    return len(contagem)

frase = input("Digite uma palavra ou frase:\n>>")

print(conta_vogais(frase))