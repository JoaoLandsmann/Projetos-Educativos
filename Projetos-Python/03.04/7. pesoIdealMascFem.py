#verificando o peso ideal de acordo com a altura (homem e mulher)

print("Vamos verificar seu peso ideal de acordo com sua altura!")

#obtendo input do usuário
altura = float(input("Qual sua altura em metros? "))
genero = input("Qual seu gênero? masculino/feminino ").upper()

#realizando a operação e imprimindo em tela para o usuário
peso_ideal_H = round(((72.7 * altura) - 58), 2)
peso_ideal_M = round(((62.1 * altura) - 44.7), 2)

#verificando se é masculino ou feminino e imprimindo o peso ideal de acordo
if genero == "MASCULINO":
    print(f"O seu peso ideal, baseado na sua altura é de {peso_ideal_H}Kg!")
else:
    print(f"O seu peso ideal, baseado na sua altura é de {peso_ideal_M}Kg!")
