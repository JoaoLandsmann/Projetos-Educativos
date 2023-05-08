#programa para transformar graus Fahrenheit para Celsius

print("Vamos converter graus Fahrenheit para Celsius!")

while True:
    #obtendo input do usuário
    fahrenheit = float(input("Insira a temperatura em graus Fahrenheit "))

    #realizando a operação e imprimindo em tela
    celsius = 5 * ((fahrenheit - 32) / 9)
    celsius_round = round(celsius, 2)
    print(f"A temperatura {fahrenheit}F convertida para Celsius é igual a {celsius_round}°C")

    #perguntando se o usuário quer fazer outra conversão
    escolha = input("Você deseja realizar outra conversão? y/n ").upper()

    #verificando a resposta
    if escolha == "Y":
        print("Beleza, vamos nessa!")
    else: 
        print("Beleza, até a próxima!")
        break