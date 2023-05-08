#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                   Até 5 Kg              Acima de 5 Kg

#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

#ara atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

#tabela de preços
precos = {
    "file_duplo": {"ate_5kg": 4.90, "acima_5kg": 5.80},
    "alcatra": {"ate_5kg": 5.90, "acima_5kg": 6.80},
    "picanha": {"ate_5kg": 6.90, "acima_5kg": 7.80}
}

#obtendo informações da compra
tipo_carne = input("Qual o tipo de carne? (file_duplo, alcatra ou picanha): ").lower()
quantidade = float(input("Qual a quantidade (em Kg) de carne que deseja comprar? ").lower())
cartao_tabajara = input("A compra será realizada com o cartão Tabajara? (s/n): ").lower()

#calculando o preço total baseado na quantidade de carne
if quantidade <= 5:
    preco_total = quantidade * precos[tipo_carne]["ate_5kg"]
else:
    preco_total = quantidade * precos[tipo_carne]["acima_5kg"]

#calculando o desconto para pagamento no cartão
if cartao_tabajara.lower() == "s" or cartao_tabajara == "sim":
    desconto = 0.05 * preco_total
else:
    desconto = 0

#imprimindo cupom fiscal com as informações da compra
print("\n======= CUPOM FISCAL =======")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade: {quantidade}Kg")
print(f"Preço total: R${preco_total:,.2f}")

#aplicando o desconto se for pago no cartão
if cartao_tabajara.lower() == "s":
    print("Tipo de pagamento: Cartão Tabajara")
    print(f"Desconto: R${desconto:,.2f}")
else:
    print("Tipo de pagamento: Dinheiro")
    print(f"Desconto: R${desconto:,.2f}")

print(f"Valor a pagar: R$ {preco_total - desconto:,.2f}")
