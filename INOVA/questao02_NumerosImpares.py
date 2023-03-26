a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

impar = []
for i in a:
    if i%2 != 0:
        impar.append(i)
    else:
        continue

print(impar)