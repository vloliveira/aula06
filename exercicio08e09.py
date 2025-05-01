
nomes = [" "," "]
senhas = [0,0]

for i in range (len(nomes)):
    nomes[i] = input("Digite um nome: ")
    senhas[i] = int(input("Digite a senha: "))

"""for x in range(len(nomes)):
    print(f"{x} - Nome: {nomes[x]}, Senha: {senhas[x]}")
"""
#Alteração do for anterior (Exercício 09)

login = input("Digite seu nome: ")
senha = int(input("Digite sua senha: "))

mensagemErro = " "
for i in range(len(nomes)):
    if login == nomes[i]:
        if senha == senhas[i]:
            mensagem = f"{login}, login efetuado com sucesso!"
            break
        else:
            mensagem = "Senha incorreta!"
            break
    else:
        mensagem = "Login incorreto!"
print(mensagem)