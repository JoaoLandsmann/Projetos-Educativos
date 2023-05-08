#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

while True:
  #obtendo input do usuário com a lista desejada
  conjunto_N = input("Digite um conjunto de números de 0 a 1000 separados por espaço: ").split(" ")

  #convertendo essa lista para float e armazenando no vetor conjunto_N
  conjunto_N = [float(num) for num in conjunto_N] 

  #verificando se todos os valores digitados estão entre 0 e 1000
  for valor in conjunto_N:
      if valor < 0 or valor > 1000:
          print("Erro! Todos os valores devem estar na faixa de 0 e 1000.")
      else:
          #verificando o maior, menor e realizando a soma. Imprimindo em tela
          print(f"O maior número dessa lista é: {max(conjunto_N)}")
          print(f"O menor número dessa lista é: {min(conjunto_N)}")
          print(f"A soma dos números dessa lista é: {sum(conjunto_N):.2f}") 
  break


