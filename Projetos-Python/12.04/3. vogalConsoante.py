#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

#criando um vetor com as vogais
vogais = ["a", "e", "i", "o", "u"]

#pegando input do usuário
letra = input("Digite uma letra: ").lower()

#verificando se é vogal ou consoante e imprimindo o resultado
if letra in vogais:
    print(f"A letra digitada ({letra}) é vogal")
else:
    print(f"A letra digitada ({letra}) é consoante")