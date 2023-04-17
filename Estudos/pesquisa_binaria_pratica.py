lista = list(range(1, 1001))
print("\n\nPense em um número entre 1 e 1000, eu tentarei adivinhar.\n")

baixo = 0
alto = len(lista) - 1
meio = int((baixo+alto)/2)
tentativas = 0
while True:
    tentativas += 1
    chute = lista[meio]
    print(f"O seu número é igual, maior, ou menor que {chute}?\n")
    print("[1] Igual\n[2] Maior\n[3] Menor\n")
    r = int(input(">>"))
    if r == 1:
        print(f"Eba, acertei!! O seu número é: {chute}!!")
        print(f"Tentativas: {tentativas}")
        break
    elif r == 2:
        baixo = meio + 1
        meio = int((baixo + alto)/2)
    else:
        alto = meio - 1
        meio = int((baixo + alto)/2)

