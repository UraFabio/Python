import pandas as pd

tabela = pd.read_csv("INOVA/actors.csv")
contagem = tabela["#1 Movie"].value_counts()
print(contagem)