#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

#criando vetor vazio para os números ímpares
num_impares = []

#criando contador
contador = 0

for i in range(1, 51):
    #verificando se o número é impar
    if contador % 2 != 0:
        num_impares.append(contador)
        
    contador += 1
  
print(num_impares)



## FORMA ALTERNATIVA

# for i in range(2, 50, 2):
#   print (i)