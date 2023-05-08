#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

while True:
    #obtendo input do usuário
    num = input("Digite um número: ")

    #função para caso haja casas decimais
    if '.' in num:
        partes = num.split('.')
        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            print(f"O número inserido ({num}) é decimal.")

    #verificando se é inteiro
    elif num.isdigit():
        print(f"O número inserido ({num}) é inteiro.")
    else:
        print(f"O valor inserido é inválido! Tente novamente.")

    #checando se o usuário deseja inserir outro número
    escolha = input("Deseja verificar outro número? (s/n): ")
    if escolha.lower() == "n" or escolha.lower() == "nao":
        print(f"Beleza! tchau.")
        break


# FORMA ALTERNATIVA (MAIS SIMPLES)

#num = float(input("Digite um número: "))
#
#if num % 1 == 0:
#   print(f"O número inserido ({num}) é inteiro")
#else:
#   print(f"O número inserido ({num}) é decimal")