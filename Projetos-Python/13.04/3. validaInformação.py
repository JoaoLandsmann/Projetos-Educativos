#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

#criando uma lista com as informações
info = ["nome", "idade", "salário", "sexo", "estado civil"]

#percorrendo a lista com o loop for
for i in info:
    #obtendo o nome do usuário e imprimindo em tela
    if i == "nome":
        nome = input("Digite o seu nome: ").capitalize()
        if len(nome) > 3:
            print(f"\nSeu nome é {nome}")
        else:
            #mensagem de erro
            print("Nome inválido! O nome deve conter ao menos 4 caracteres.")

    #obtendo a idade do usuário e imprimindo em tela
    elif i == "idade":
        idade = int(input("Digite a sua idade: "))
        if idade in range(0, 151):
            print(f"Você tem {idade} anos de idade")
        else:
            #mensagem de erro
            print("Idade inválida! A idade deve estar na faixa de 0 a 150 anos.")

    #obtendo o salário do usuário e imprimindo em tela
    elif i == "salário":
        salario = float(input("Digite o seu salário: R$"))
        if salario > 0:
            print(f"O seu salário é de: R${salario:.2f}")
        else:
            #mensagem de erro
            print("Salário inválido! O salário deve ser maior do que 0")

    #obtendo o sexo do usuário e imprimindo em tela
    elif i == "sexo":
        sexo = input("Digite o seu sexo: (f/m) ").lower()
        if sexo == "masculino" or sexo == "m":
            print("Sexo masculino.")
        elif sexo == "feminino" or sexo == "f":
            print("Sexo feminino")
        else:
            #mensagem de erro
            print("Sexo inválido! O sexo deve ser masculino ou feminino")

    #obtendo o estado civil do usuário e imprimindo em tela
    elif i == "estado civil":
        estado_civil = input("Digite o seu estado civil: (s/c/v/d) ").lower()
        #verificando qual o estado civil
        if estado_civil == "s":
            print("Seu estado civil é solteiro(a) \n")
        elif estado_civil == "c":
            print("Seu estado civil é casado(a) \n")
        elif estado_civil == "v":
            print("Seu estado civil é viúvo(a) \n")
        elif estado_civil == "d":
            print("Seu estado civil é divorciado(a) \n")
        else:
            #mensagem de erro
            print("Estado civil inválido! O estado civil deve ser (s)olteiro, (c)asado, (v)iuvo ou (d)ivorciado.")