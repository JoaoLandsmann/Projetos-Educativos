#criando um programa para calcular a média entre 4 notas
print("Vamos calcular a sua média anual com base nas suas notas bimestrais!")

while True:
    #pegando input do usuário
    nota1 = float(input("Entre sua nota do 1° bimestre."))
    nota2 = float(input("Entre sua nota do 2° bimestre."))
    nota3 = float(input("Entre sua nota do 3° bimestre."))
    nota4 = float(input("Entre sua nota do 4° bimestre."))

    #calculando a media
    media_final = (nota1 + nota2 + nota3 + nota4) / 4
    media_round = round(media_final, 2)

    print(f"A sua média final é de {media_round}")

    #vendo se o usuário deseja calcular novamente
    escolha = input("Deseja calcular mais uma vez? y/n")

    #verificando a resposta
    if escolha == "y":
        print("Beleza, insira as suas notas novamente!")
    elif escolha == "n":
        print("Beleza, até a próxima!")
        break

