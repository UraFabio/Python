print(">>Eu calculo quantos % a quantidade de horas inseridas equivalem no dia.")
h = 1
m = 1
def calculo():
    h = float(input(">Insira a quantidade de horas:\n>>"))
    m = float(input(">Insira a quantidade de minutos:\n>>"))
    tempo_inserido = (h*60)+m
    minutos_dia = 24*60
    resultado = tempo_inserido*100/minutos_dia
    print(f"Equivale a {resultado:2.0f}% do dia ou mais exatamente a {resultado:5.2f}%.")
while h!=0 or m!=0:
    calculo()

