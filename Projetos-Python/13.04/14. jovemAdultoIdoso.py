#Faça um programa que peça para n pessoas a sua idade, 
#ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

while True:
    #obtendo input do usuário
    idades = input("Digite a idade de todas as pessoas da turma separadas por espaço: ").split(" ")

    #convertendo as strings em int
    idades = [int(num) for num in idades]

    #criando variavel para somar todas as idades
    soma = 0

    #somando todas as idades
    for num in idades:
        soma += num

    #calculando a média e arredondando para 
    media = round(soma / len(idades))
    
    if media in range(0, 26):
        print(f"A média das idades é aproximadamente {media:.2f} anos, portanto a turma é jovem.")
        break
    elif media in range(26, 60):
        print(f"A média das idades é aproximadamente {media:.2f} anos, portanto a turma é adulta.")
        break
    elif media in range(60, 150):
        print(f"A média das idades é aproximadamente {media:.2f} anos, portanto a turma é idosa.")
        break
    else:
        print("Idade inválida! Certifique-se de que TODAS as idades estão na faixa de 0 a 150 anos.")