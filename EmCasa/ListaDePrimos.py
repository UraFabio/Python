def eh_primo(n):
    if n == 1:
        return False
    else:
        a = 2
        while True:
            if n % a == 0:
                if n != a:
                    return False
                else:
                    return True
            else:
                a += 1

primos = []  
a = int(input("Com quantos termos deseja criar um lista de numeros primos?:\n>>"))
x = 2
while True:
    if eh_primo(x):
        primos.append(x)
        if len(primos) == a:
            break
        else:
            x +=1
    else:
        x +=1
print(primos)