


n = int(input(">>"))

binario = list(str(bin(n)))

a = binario.pop(2)
binario.append(a)
binario = "".join(binario)

print(int(binario, 2))