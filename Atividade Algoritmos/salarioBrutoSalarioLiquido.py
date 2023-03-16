def imposto_de_renda(salario_bruto):
    if salario_bruto <= 900:
        ir = salario_bruto*0
        return ir
    elif salario_bruto > 900 and salario_bruto <= 1500:
        ir = salario_bruto*0.05
        return ir
    elif salario_bruto > 1500 and salario_bruto <= 2500:
        ir = salario_bruto*0.1
        return ir
    elif salario_bruto > 2500:
        ir = salario_bruto*0.2
        return ir

salario = int(input("Quanto você ganha por hora?(Em R$):\n"))
horas = int(input("Quantas horas você trabalha por mês?:\n"))
salario_bruto = salario*horas
ir = imposto_de_renda(salario_bruto)
sindicato = salario_bruto*0.03
fgts = salario_bruto*0.11
salario_liquido = salario_bruto-ir-sindicato
print(f"\nSalário bruto: R${salario_bruto:5.2f}")
print(f"Salário líquido: R${salario_liquido:5.2f}\n")
print(f"Descontos: \nR${ir:5.2f} - Imposto de Renda\nR${sindicato:5.2f} - Sindicato\n")
print(f"FGTS: R${fgts:5.2f}")
