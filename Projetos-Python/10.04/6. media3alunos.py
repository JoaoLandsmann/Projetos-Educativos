#calculando a media de 3 alunos 

#criando vetores vazios
alunos = []
notas = []
medias = []
medias_acima7 = []

#criando indice e contador
indice = 0
contador = 1

#obtendo inputdo usuário
for i in range(0, 3):
    print("Insira a nota do aluno ", i + 1)
    for j in range(0, 4):
        nota = int(input(f"Nota do {contador}° bimestre: "))
        notas.append(nota)
        contador += 1
        if contador == 5:
            contador = 1
            
    #inserindo as notas no respectivo vetor
    alunos.append(notas)
    notas = []

#calculando a média dos alunos
for k in range(0, 3):
    media = sum(alunos[indice]) / len(alunos[indice])

    #verificando quantos alunos tem media acima de 7
    if media >= 7:
        medias.append(media)
        medias_acima7.append(media)
        indice += 1
    else:
        medias.append(media)
        indice += 1

#imprimindo resultado em tela
print(f"As notas dos alunos foram, respectivamente, {alunos}")
print(f"As médias dos alunos foram, respectivamente, {medias}")

#imprimindo quantos alunos tem media acima de 7
if len(medias_acima7) > 0:
    print(f"Há {len(medias_acima7)} aluno(s) com nota acima de 7")
else:
    print(f"Não há nenhum aluno com nota acima de 7")

