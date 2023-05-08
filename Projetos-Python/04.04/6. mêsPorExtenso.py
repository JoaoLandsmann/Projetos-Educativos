#escrevendo a data de nascimento com o mês por extenso

#importando a biblioteca
import datetime

#obtendo input do usuário
dia = int(input("Qual o dia do seu nascimento? (em números)"))
mes = int(input("Qual o mês do seu nascimento? (em números)")) 
ano = int(input("Qual o ano do seu nascimento? (em números)"))

#utilizando a função da biblioteca
data = datetime.datetime(ano, mes, dia)

#imprimindo em tela o resultado
print("Você nasceu dia", data.day, "do mês de", data.strftime("%B"), "do ano de", data.year)


