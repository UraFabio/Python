q1 = int(input("Telefonou para a vítima? 1 para sim, 2 para não:\n"))
q2 = int(input("Esteve no local do crime? 1 para sim, 2 para não:\n"))
q3 = int(input("Mora perto da vítima? 1 para sim, 2 para não:\n"))
q4 = int(input("Devia para a vítima? 1 para sim, 2 para não:\n"))
q5 = int(input("Já trabalhou com a vítima? 1 para sim, 2 para não:\n"))
L = [q1, q2, q3, q4, q5]
if L.count(1) == 1:
    print("A pessoa é inocente!")
elif L.count(1) == 2:
    print("A pessoa é suspeita!")
elif L.count(1) > 2 and L.count(1) < 5:
    print("A pessoa é Cúmplice!")
elif L.count(1) == 5:
    print("A pessoa é a assassina!")
