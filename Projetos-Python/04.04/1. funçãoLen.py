#programa para informar o conteúdo das strings, seu comprimento e se são iguais ou diferentes no conteúdo

#obtendo input do usuário
frase1 = input("Insira a primeira frase a ser comparada ").upper()
frase2 = input("Insira a segunda frase a ser comparada ").upper()

#verificando o comprimento das frases
frase1_comprimento = len(frase1)
frase2_comprimento = len(frase2)

#imprimindo em tela
print(f"O conteúdo da primeira frase é '{frase1}', e o da segunda frase é '{frase2}'")
print(f"O comprimento da primeira frase é de {frase1_comprimento} caracteres, e o da segunda frase é de {frase2_comprimento} caracteres")

#verificando se o conteúdo é igual
if frase1 == frase2:
    print(f"O conteúdo das frases é igual!")
else:
    print(f"O conteúdo das frases é diferente!")