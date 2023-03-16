tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f"{tabuada}x{numero} = {tabuada*numero}")
        if numero == 10:
            print("-----------------")
        numero += 1
    tabuada += 1