def calculadora(n1, n2, op):
    if op == "+":
        return n1+n2
    elif op == "-":
        return n1-n2
    elif op == "*":
        return n1*n2
    elif op == "/":
        return n1/n2
tela = input("Digite a operação que deseja realizar(sem espaçamentos):\n>")
n1 = float(tela[0])
n2 = float(tela[2])
op = tela[1]
resultado = calculadora(n1 , n2, op)
print(resultado)

