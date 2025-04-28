nomes = ["", "", "", "", ""]
for i in range(len(nomes)):
    nomes[i] = input("Digite o nome: ")

nome = input("Digite um nome para encontrar na lista: ")

for i in range(len(nomes)):
    if nome == nomes[i]:
        print(f"{nome} está na posição {i}")