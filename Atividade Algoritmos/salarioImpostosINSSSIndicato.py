s = float(input("Quanto você ganhar por hora?(em R$):\n"))
h = int(input("Quantas horas você trabalha ao mês?\n"))
salario_bruto = s*h

ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto-(ir+inss+sindicato)
print(f"Seu salário bruto ao mês é de R${salario_bruto:5.2f}")
print(f"Valor pago de impostos: R${ir:5.2f}")
print(f"Valor pago ao INSS: R${inss:5.2f}")
print(f"Valor pago ao sindicato:R${sindicato:5.2f}")
print(f"Salário líquido: R${salario_liquido:5.2f}")