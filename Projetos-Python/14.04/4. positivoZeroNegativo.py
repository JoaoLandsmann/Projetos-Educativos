#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo

#obtendo input do usuário
numero = int(input("Digite um número real: "))
verificacao = str.isnumeric(numero)

def retorna_valor(num):
    if verificacao == True and num > 0:
        return "P"
    elif verificacao == True and num<= 0:
        return "N"
    else:
        return "Loucurada"
    
resultado = retorna_valor(numero)
print(resultado)