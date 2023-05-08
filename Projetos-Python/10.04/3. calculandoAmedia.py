#programa que lê 4 notas e calcula a média

#criando vetor vazio
notas = []

#obtendo input do usuário
for i in range(4):
    nota = float(input(f"Digite a {i+1}° nota: "))
    notas.append(nota)

#calculando a media
media = sum(notas) / len(notas)

#imprimindo resultado em tela
print(f"Suas notas foram: {notas}, e sua média foi de {media:.2f}")