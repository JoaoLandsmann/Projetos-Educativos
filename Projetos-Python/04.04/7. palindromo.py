#checando se um texto é um palíndromo

#obtendo input do usuário
texto_user = input("Digite um texto (sem acentos) ").upper()
texto = texto_user.replace(" ", "")
check_palindromo = texto[::-1]

#checando se é um palíndromo
if texto == check_palindromo:
    print(f"O texto {texto} é um palíndromo!")
else:
    print(f"O texto {texto} não é um palíndromo")