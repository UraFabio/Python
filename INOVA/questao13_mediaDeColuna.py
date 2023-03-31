import pandas as pd
tabela = pd.read_csv("INOVA/actors.csv")
print(tabela["Number of Movies"].mean())