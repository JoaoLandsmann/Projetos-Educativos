#conversor de metro para centímetros
print("Vamos converter metros para centímetros!")

while True:

    #obtendo input do usuário
    metros = float(input("Insira um número em metros"))

    #fazendo a conversão
    centimetros = metros * 100
    centimetros_round = round(centimetros, 2)

    #imprimindo resultado em tela
    print(f"O valor em metros ({metros}), convertido para centímetros é {centimetros_round}cm")

    #vendo se o usuário deseja fazer outra conversão
    escolha = input("Deseja realizar outra conversão? y/n")

    #verificando a resposta
    if escolha == "y":
        print("Beleza, vamos nessa!")
    elif escolha == "n":
        print("Beleza, até mais!")
        break