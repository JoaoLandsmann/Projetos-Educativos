#verificando o peso ideal de acordo com a altura

print("Vamos verificar seu peso ideal de acordo com sua altura!")

#obtendo input do usuário
altura = float(input("Qual sua altura em metros?"))

#realizando a operação e imprimindo em tela para o usuário
peso_ideal = (72.7 * altura) - 58
peso_ideal_round = round(peso_ideal, 2)
print(f"O seu peso ideal, baseado na sua altura é de {peso_ideal_round}Kg!")