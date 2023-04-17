aporte_inicial = float(input("Aporte inicial:\n>> R$"))
aportes_mensais = float(input("Aportes mensais\n>> R$"))
aportes_anuais = float(input("Aportes anuais:\n>> R$"))
tipo_de_juros = (input("A taxa de juros será mensal ou anual?\n\n[1] Mensal\n[2] Anual\n\n>>"))
if tipo_de_juros == "1":
    taxa_de_juros = float(input("\nDigite a taxa de juros mensal:\n>>"))
else:
    taxa_de_juros = float(input("\nDigite a taxa de juros anual:\n>>"))
    


