num = [0,0,0,0,0]

for i in range (len(num)):
    num[i] = int(input("Digite um número: "))

for x in range(len(num)-1,-1,-1):
    print(num[x])