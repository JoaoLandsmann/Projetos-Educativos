#programa para calcular o salário total de um mês trabalhado

#obtendo input do usuário
ganho_por_hora = float(input("Insira o valor do quanto você ganha por hora trabalhada "))
horas_trabalhadas = float(input("Insira o número de horas trabalhadas no referente mês "))

#realizando a operação e imprimindo em tela
salario_mes = ganho_por_hora * horas_trabalhadas
salario_mes_round = round(salario_mes, 2)
print(f"O salário total do mês trabalhado é de R${salario_mes_round}")

