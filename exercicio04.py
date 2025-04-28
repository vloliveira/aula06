notas = [0,0,0,0,0]
soma = 0
acimaMedia = 0

for i in range(len(notas)):
    notas[i] = float(input("Digite a nota do aluno: "))

for x in range(len(notas)):
    soma += notas[x]

media = soma/len(notas)

for y in range(len(notas)):
    if notas[y] > media:
        acimaMedia += 1

print(f"A média da turma é: {media}")
print(f"Tem {acimaMedia} alunos acima da média.")