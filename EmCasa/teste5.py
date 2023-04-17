vi = float(input("Valor inicial:\nR$"))
am = float(input("Aporte mensal:\nR$"))
tx = float(input("Taxa de juros mensais em %:\n"))
p = int(input("Período em anos:\n"))
m = 2
f = vi
while m <= p*12:
    m += 1
    i = 0
    r = (f+am)*tx/100
    f += r
    i += r
print(f"\nTotal investido:\nR${vi+(am*(p*12)):0.2f}\n")
print(f"Total ganho com os juros:\nR${f-i:0.2f}\n")
print(f"Total:\nR${f:0.2f}")
    

