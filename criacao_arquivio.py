import csv

#criar um arquivo txt, w = write

with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome, Idade, Cidade\n")
    arquivo.write("Alberto, 92, chique-chique\n")
    arquivo.write("Arthur, 28, arraial\n")
    arquivo.write("Matheus, 28, Cotia\n")
    
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("conteuo do arquivo:")
    print(arquivo.read())
    
#criando arquivo csv

dados = [
    
    ["nome", "Idade"],
    ["joao", "20"],
    ["Maria", "30"],
    ["jose", "80"],
    ["Lana", "40"],
]    
    
with open ("dados.csv", "w", newline="", encoding="utf-8")as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)
    
with open ("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo)
    print("\n Conteudo do arquivo CSV")
    for linha in leitor:
        print(linha)
        
