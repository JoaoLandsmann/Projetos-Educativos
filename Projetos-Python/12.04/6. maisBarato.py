#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

#obtendo input do usuário
valor_produtos = input("Digite o valor de três produtos separados por espaço ").split(" ")

#convertendo para float
valor_produtos = [float(valor) for valor in valor_produtos]

#verificando qual o menor valor
valor_min = min(valor_produtos)

#imprimindo o resultado 
print(f"O produto que você deve comprar custa: R${valor_min:,.2f}")