#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    
  #obtendo input do usuário
  populacao_A = int(input("DIgite o valor populacional do país A: "))
  crescimento_A = float(input("Digite o crescimento populacional do país A em valor decimal: "))
  populacao_B = int(input("DIgite o valor populacional do país B: "))
  crescimento_B = float(input("Digite o crescimento populacional do país B em valor decimal: "))

  if populacao_A <= 0 or populacao_B <= 0:
    print("Erro! A população dos países não podem ser menores do que 0.")
    continue

  #criando os dicionários
  pais_A = {
            "populacao": populacao_A,
            "crescimento": crescimento_A
            }
  pais_B = {
            "populacao": populacao_B,
            "crescimento": crescimento_B
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
  break


