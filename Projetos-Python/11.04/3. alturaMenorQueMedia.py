#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

#criando vetores vazios
quantidade_alunos = 0
media_altura = []
alturas = []
idades = []

for i in range(3):
    #obtendo as idades e alturas de cada aluno
    idade = int(input(f"Digite a idade do aluno {i+1} :"))
    altura = float(input(f"Digite a altura do aluno {i+1} :"))

    #adicionando os valores nos respectivos vetores
    idades.append(idade)
    alturas.append(altura)

#calculando a média das alturas
media_altura = sum(alturas) / len(alturas)

for j in range(3):
    #checando se tem alunos dentro dos requisitos
    if alturas[j] < media_altura and idades[j] > 13:
        quantidade_alunos +=1
        j += 1

#printando o resultado em tela
print(f"Há {quantidade_alunos} aluno(s) com mais de 13 anos e altura inferior a média de altura de todos os alunos.")
