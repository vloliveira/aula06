A = [0,0,0,0,0,0,0,0,0,0]
M = [0,0,0,0,0,0,0,0,0,0]

for i in range (len(A)):
    A[i] = int(input("Digite um número: "))

x = int(input("Digite mais um número: "))

for y in range (len(M)):
    M[y] = A[y] * x

print(M)

