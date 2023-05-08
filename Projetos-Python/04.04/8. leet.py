#tradutor de dialeto leet

#dicionario
dicionario_leet = {
"A" : "4",
"B" : "8",
"C" : "(",
"D" : "|)",
"E" : "3",
"F" : "ph",
"G" : "6",
"H" : "#",
"I" : "1",
"J" : "j",
"K" : "|<",
"L" : "£",
"M" : "|V|",
"N" : "/V",
"O" : "0",
"P" : "|>",
"Q" : "Q",
"R" : "|2",
"S" : "5",
"T" : "7",
"U" : "|_|",
"V" : "√",
"W" : "//",
"X" : "><",
"Y" : "`/",
"Z" : "2",
}

#function para realizar a substituição
def leet_tradução(texto):
    texto_leet = ''
    for letra in texto:
        if letra.upper() in dicionario_leet:
            texto_leet += dicionario_leet[letra.upper()]
        else:
            texto_leet += letra
    return texto_leet

#obtendo input do usuário
texto = input("Insira um texto para realizarmos a conversão para o dialeto Leet")
texto_leet = leet_tradução(texto)

#imprimindo resultado em tela
print(texto_leet)