#programa que diz quantas consoantes foram lidas

#criando vetores vazios
vetor = []
vetor_vogais = ["a", "e", "i", "o", "u"]
vetor_consoantes = []

#obtendo input do usuário e verificando se é consoante
for i in range (10):
    caractere = input("Digite um caractere: ")
    vetor.append(caractere)
    if caractere.isalpha() and caractere.lower() not in vetor_vogais:
        #inserindo no vetor_consoantes
        vetor_consoantes.append(caractere)

#imprimindo o resultado em tela
print("O vetor é: ", vetor)
print(f"Foram lidas {len(vetor_consoantes)} consoantes. As consoantes são: {vetor_consoantes}!")