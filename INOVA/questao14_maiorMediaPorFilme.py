import pandas as pd

tabela = pd.read_csv("INOVA/actors.csv")
tabela = tabela.sort_values(by = "Average per Movie", ascending=False)

tabela.reset_index(inplace=True)
print(tabela.loc[0, "Actor"])