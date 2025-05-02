
num = [0]*10

count = 0

for i in range(10):
    num[i] = int(input("Digite um número: "))

novoNum = int(input("Digite mais um número: "))

for x in range(10):
    if novoNum == num[x]:
        count+=1

print(f"O novo número se repete {count} vezes")

