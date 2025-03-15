import pandas as pd
import matplotlib.pyplot as plt

# Dados do primeiro DataFrame (pessoas)
dados = {
    "Nome": ["Arthur", "Maria", "Mateus", "Carlos", "Bruna"],
    "Idade": [28, 22, 18, 35, 11], 
    "Cidade": ["Cotia", "Caracas", "São Paulo", "Osasco", "Vargem"]
}

# Dados do segundo DataFrame (carros)
dados2 = {
    "Nome": [
        "Volkswagen Gol",
        "Volkswagen Parati",
        "Volkswagen Santana",
        "Fiat Uno Fire",
        "Fiat Palio",
        "Fiat Siena",
        "Fiat Fiorino",
        "Fiat Tempra",
        "Chevrolet Corsa",
        "Ford Ka"
    ],
    "Data de Lançamento": [
        "1991-03-15",  # Exemplo de data
        "1990-05-20",
        "1992-08-10",
        "1992-07-01",
        "1996-04-12",
        "1997-09-15",
        "1995-06-08",
        "1990-11-03",
        "1994-03-22",
        "1996-10-30"
    ],
    "Modelo": [
        "Hatchback",
        "Station Wagon",
        "Sedan",
        "Hatchback",
        "Hatchback",
        "Sedan",
        "Van",
        "Sedan",
        "Compacto",
        "Hatchback"
    ],
    "Fabricante": [
        "Volkswagen",
        "Volkswagen",
        "Volkswagen",
        "Fiat",
        "Fiat",
        "Fiat",
        "Fiat",
        "Fiat",
        "Chevrolet",
        "Ford"
    ]
}

# Cria os DataFrames a partir dos dicionários
df = pd.DataFrame(dados)
print("DataFrame de pessoas:")
print(df)
print("\n")

df2 = pd.DataFrame(dados2)
print("DataFrame de carros:")
print(df2)

# Salva o df2 em um arquivo CSV e o lê novamente, apenas para exemplificar
df2.to_csv("pandas_carros.csv", index=False)
df2_csv = pd.read_csv("pandas_carros.csv")

print("\nDataFrame lido do CSV:")
print(df2_csv)
print("\n")

# Filtra os carros da marca Fiat
df_filtrado = df2[df2["Fabricante"] == "Fiat"]
print("Carros da marca 'Fiat':")
print(df_filtrado)
print("\n")

# Gerador de Gráfico de Colunas:
# Vamos criar um gráfico que exibe a quantidade de carros por fabricante (do DataFrame df2)

# Contagem de carros por fabricante
contagem_fabricantes = df2["Fabricante"].value_counts()

# Configurando e plotando o gráfico de barras (colunas)
plt.figure(figsize=(8, 8))
plt.bar(contagem_fabricantes.index, contagem_fabricantes.values, 
        color=['skyblue', 'salmon', 'lightgreen', 'violet'])
plt.title("Contagem de Carros por Fabricante")
plt.xlabel("Fabricante")
plt.ylabel("Quantidade de Carros")
plt.tight_layout()  # Ajusta o layout para melhor visualização
plt.show()
