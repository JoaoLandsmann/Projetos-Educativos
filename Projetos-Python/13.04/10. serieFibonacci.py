#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

#inicializando a série de fibonacci com os dois primeiros números
fibonacci = [0, 1]

#loop while para gerar a série até o número especificado (500)
while fibonacci[-1] + fibonacci[-2] < 500:
    # Adicione o próximo número da série, que é a soma dos dois últimos
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

#exibindo a série de fibonacci gerada, separada por vírgulas
print(f"Série de Fibonacci até 500:")
for i in fibonacci[:-1]:
    print(i, end=", ")

#adicionando o último número da série sem a vírgula no final
print(fibonacci[-1])