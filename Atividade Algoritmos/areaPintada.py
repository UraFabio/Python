a = float(input("Qual será o tamanho da área pintada?(em m²):\n>>"))
litros = a/3
latas = litros//18
if (litros%18) != 0:
    latas +=1
print(f"Serão necessárias {latas:2.0f} latas, somando um total de R${80*latas}")