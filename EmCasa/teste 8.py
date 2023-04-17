nikolas_tesla = {"data de nascimentos":1856,
"data de morte":1943,
"religião": "cristão ortodoxo", 
"altura":1.88, 
"nacionalidade":"sérvio",}

print(nikolas_tesla)

print(nikolas_tesla["nacionalidade"])

nikolas_tesla["nome do pai"] = "Milutin Tesla"
nikolas_tesla["nome da mãe"] = "Duka Tesla"
nikolas_tesla["nacionalidade"] = "norte americano"

del nikolas_tesla["altura"]

print(nikolas_tesla)

print(list(nikolas_tesla.keys()))
print(list(nikolas_tesla.values()))
print(list(nikolas_tesla.items()))



