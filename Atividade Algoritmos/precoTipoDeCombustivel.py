c = input("Com qual tipo de combustível deseja abastecer?('A' para álcool e 'G' para gasolina:\n")
litros = int(input("Com quantos litros deseja abastecer?\n"))
if c.upper() == "A":
    if litros <= 20:
        desconto = 0.03*litros
    elif litros > 20:
        desconto = 0.05*litros
    total = litros*1.9-(litros*1.9*desconto)
    print(f"O total a ser pago será de R${total:5.2f}")
    
elif c.upper() == "G":
    if litros <= 20:
        desconto = 0.04*litros
    elif litros > 20:
        desconto = 0.06*litros
    total = litros*2.5-(litros*2.5*desconto)
    print(f"O total a ser pago será de R${total:5.2f}")
