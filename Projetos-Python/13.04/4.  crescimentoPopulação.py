#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

#criando os dicionários
pais_A = {
          "populacao": 80000,
          "crescimento": 0.03
          }
pais_B = {
          "populacao": 200000,
          "crescimento": 0.015
          }

# criando variável anos
anos = 0

for anos in range(1000):
    # calculando o aumento da população anual
    pais_A["populacao"] += pais_A["populacao"] * pais_A["crescimento"]
    pais_B["populacao"] += pais_B["populacao"] * pais_B["crescimento"]

    # verificando se a população do país A é maior que a do B
    if pais_A["populacao"] >= pais_B["populacao"]:
        break

# contabilizando mais um ano fora do loop
anos += 1

# imprimindo o resultado
print(f"Levou {anos} anos para que o país A ultrapassasse o país B em população.")