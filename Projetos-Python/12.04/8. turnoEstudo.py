#Faça um Programa que pergunte em que turno você estuda. 
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

while True:

    #obtendo input do usuário e convertendo em maiúscula
    turno = input("Em que turno você estuda? (M)atutino, (V)espertino ou (N)oturno (M, V ou N) ")
    turno = turno.upper()

    #verificando o que foi inserido e imprimindo a mensagem
    if turno == "M" or turno == "MATUTINO":
        print(f"Bom dia!")
        break
    elif turno == "V" or turno == "VESPERTINO":
        print(f"Boa tarde!")
        break
    elif turno == "N" or turno == "NOTURNO":
        print(f"Boa noite!")
        break
    else:
        print("Valor inválido, tente novamente!")