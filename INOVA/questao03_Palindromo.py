palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in palavras:
    invertido = palavra[::-1]
    if invertido == palavra:
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")