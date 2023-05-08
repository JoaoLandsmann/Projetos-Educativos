#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

#criando a variável tentativas
tentativas = 0

#setando um limite de tentativas para login
for i in range(5):
    #obtendo input do usuário
    nome = input("Digite o nome do usuário: ").upper()
    senha = input("Digite a senha do usuário: ").upper()

    #validando se o nome é igual a senha
    if nome == senha:
        print("Ocorreu um erro, por favor tente novamente.")
        tentativas += 1
    else:
        print("Login válido. Segue adiante meu guri!")
        break
    
    #caso o usuário exceda o limite de tentativas
    if tentativas == 5:
        print("Número máximo de tentativas excedido. Tente novamente mais tarde.")
        break

