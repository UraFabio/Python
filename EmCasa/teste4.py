d = float(input("Depósito incial:\n"))
t = float(input("Taxa de juros mensal da poupança:\n"))
m = 1
i = d
while m <= 12:
    print(f"Rendimentos do {m}º mês:")
    print(f"R${(d*t)/100:0.2f}")
    q = input("Deseja fazer uma nova aplicação? S para sim e N para não:\n")
    a = 0
    if q.upper() == "S":
        a = float(input("Qual o valor do aporte?:\n"))
    i += a
    m += 1
    d = (d+(d*t)/100)+a
    print(f"Novo valor:\n R${d:0.2f}\n\n")
print(f"Valor investido: R${i:0.2f}\n Rendimentos totais:\n R${d-i:0.2f}")