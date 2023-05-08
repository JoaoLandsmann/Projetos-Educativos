#calculando a área de um quadrado

print("Vamos calcular a área de um quadrado em m²!")

while True:
    #obtendo input do usuário
    lado = float(input("Insira o valor de um lado do quadrado em metros"))

    #realizando a operação
    area_do_quadrado = (lado * lado)
    area_do_quadrado_round = round(area_do_quadrado, 2)
    print(f"A área de um quadrado de {lado} x {lado} é de {area_do_quadrado_round}m²")

    #vendo se o usuário deseja realizar outra operação
    escolha = input("Deseja calcular a área de outro quadrado?")

    #verificando a resposta
    if escolha == "y":
        print("Beleza, vamos nessa!")
    elif escolha == "n":
        print("Beleza, até mais!")
        break