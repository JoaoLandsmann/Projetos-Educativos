#lendo e imprimindo 5 vetores
lista = []

#obtendo input do usuário e inserindo no vetor lista
palavras = input("Digite 5 palavras separadas por espaço: ").split(" ")
lista.append(palavras)

#imprimindo cada palavra da lista
for palavra in lista:
    print(f"As palavras são: {palavra}")
    