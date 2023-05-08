#calculando a multa

print("Vamos calcular se houve multa em relação ao peso de peixes trazidos")

#obtendo input do usuário
peso = float(input("Entre o peso em Kg"))

#realizando operação e calculando o valor da multa
excesso = peso - 50
valor_multa = 4
total_a_pagar = round((excesso * valor_multa), 2)

#verificando se ele trouxe a mais do que o permitido
if peso > 50:
    print("O peso excedeu o limite! Vamos calcular sua multa...")
    print(f"O valor total da multa é de R${total_a_pagar}, pois o peso {peso}Kg excede o limite imposto!")
else:
    print("O peso não atingiu o limite, tudo certo!") 