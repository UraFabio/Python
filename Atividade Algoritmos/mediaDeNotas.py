n1 = float(input("Digite sua primeira nota:\n>>"))
n2 = float(input("Digite sua segunda nota:\n>>"))
media = (n1+n2)/2
if media == 10:
    print("Aprovado com Distinção!")
else:
    if media >= 7:
        print("Aprovado!")
    elif media < 7:
        print("Reprovado!")
