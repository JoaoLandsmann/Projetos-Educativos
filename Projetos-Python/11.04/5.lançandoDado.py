#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor 
#de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

#importando biblioteca random
import random

#criando vetores 
contadores = [1, 2, 3, 4, 5, 6]
resultados = []
num_cada_valor = []
indice = 1

for i in range(100):
    #lançando o dado numa faixa de números 1 a 6
    dado = random.randrange(1, 6 + 1)

    #armazenando os resultados
    resultados.append(dado)

for j in range(6):
    #checando quantas vezes caiu cada valor do dado
    num = resultados.count(indice)
    num_cada_valor.append(num)
    indice += 1

    #imprimindo resultado de cada valor
    print(f"Há {num_cada_valor[j]} número(s) ({j+1})")


    

