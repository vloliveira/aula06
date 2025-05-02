nomes = [" "]*5

for i in range(5):
    nomes[i] = (input("Digite um nome: "))

print(*nomes, sep = ", ")

for x in range(4,-1,-1):
    print( nomes[x], end = ", ")