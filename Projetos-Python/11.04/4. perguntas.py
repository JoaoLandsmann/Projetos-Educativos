#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

#criando os vetores vazios
perguntas = [
    "Telefonou para a vítima?",         
    "Esteve no local do crime?",        
    "Mora perto da vítima?",           
    "Devia para a vítima?",             
    "Já trabalhou com a vítima?"         
]
respostas = []

for pergunta in perguntas:
    #fazendo a pergunta
    resposta = input(pergunta + " (yes ou no): ").lower()

    #checando se a resposta é sim e armazenando no vetor
    if resposta == "yes" or resposta == "y":
        respostas.append(True)
    else:
        respostas.append(False)

#contando as respostas positivas
respostas_positivas = respostas.count(True)

#exibindo resultados de acordo com o número de respostas positivas
if respostas_positivas == 2:
    print(f"A pessoa entrevistada é suspeita")
elif 3<= respostas_positivas <= 4:
    print(f"A pessoa entrevistada é cúmplice")
elif respostas_positivas == 5:
    print(f"A pessoa entrevistada é assassina")
else:
    print(f"A pessoa entrevistada é inocente")
