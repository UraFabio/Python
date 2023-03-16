mb = float(input("Qual o tamanho do arquivo para download?(Em MB)\n"))
v = float(float(input("Qual a velocidade da Internet?(Em Mbps)\n")))
minutos = (mb//v)//60
segundos = mb%v + (mb//v)%60
print(f"O tempo aproximado de download é de {int(minutos)} minutos e {segundos} segundo(s)! ")
