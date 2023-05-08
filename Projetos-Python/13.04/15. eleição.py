#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

#criando um vetor vazio
votos = []

#obtendo número total de eleitores
num_eleitores = int(input("Digite o número total de eleitores: "))

for i in range(num_eleitores):
    #obtendo input do usuário e armazenando no vetor votos
    voto = input(f"Digite o voto do {i+1}° eleitor: (1, 2 ou 3) ")
    votos.append(voto)

#contando a quantidade de votos para cada candidato
candidato1 = votos.count("1")
candidato2 = votos.count("2")
candidato3 = votos.count("3")

#imprimindo o resultado em tela
print(f"O total de votos para o 1° candidato é {candidato1}")
print(f"O total de votos para o 2° candidato é {candidato2}")
print(f"O total de votos para o 3° candidato é {candidato3}")