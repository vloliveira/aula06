a = []
b = []
somas= []

n = int(input("Digite um número: "))

for i in range(n):
    a.append(i)
    b.append(i)
    somas.append(a[i] + b[i])

print(somas)