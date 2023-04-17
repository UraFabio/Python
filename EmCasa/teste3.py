q = "S"
while q.upper() == "S":
    n = int(input("Escolha um número inteiro:\n"))
    t = input("Qual operação deseja realizar? S para soma, M para subtração, X para multiplicação e D para divisão.\n")
    h = 1
    if t.upper() == "S":
        while h <= 10:
            print(f"{h}+{n}={h+n}")
            h += 1
    elif t.upper() == "M":
        while h <= 10:
            print(f"{h}-{n}={h-n}")
            h += 1
    elif t.upper() == "X":
        while h <= 10:
            print(f"{h}x{n}={h*n}")
            h += 1
    elif t.upper() == "D":
        while h <= 10:
            print(f"{h}/{n}={h/n}")
            h += 1
    q = input("Deseja realizar outra operação? S para sim e N para não:\n")
