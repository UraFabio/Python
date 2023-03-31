import pandas as pd

tabela = pd.read_csv("INOVA/actors.csv", index_col="Actor")

maior_numero_de_filmes = tabela[["Number of Movies"]].sort_values(by = "Number of Movies", ascending=False)
total_de_filmes = tabela["Number of Movies"].max()

maior_numero_de_filmes.reset_index(inplace=True)

print(f"O ator/atriz com o maior número de filmes é: {maior_numero_de_filmes.loc[0, 'Actor']}")
print(f"Com o total de {total_de_filmes} filmes.")