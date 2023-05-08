#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

#obtendo as notas do usuário
notas = input("Digite a primeira e a segunda nota separadas por espaço ").split(" ")

#convertendo para float
notas = [float(num) for num in notas]

#calculando a media
media = sum(notas) / 2

#verificando a média e imprimindo o resultado 
if media == 10:
    print(f"Aprovado com Distinção")
elif media >= 7:
    print(f"Aprovado")
else:
    print("Reprovado")