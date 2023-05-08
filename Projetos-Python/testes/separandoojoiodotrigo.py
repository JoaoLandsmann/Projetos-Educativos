JoioTrigo = ["joio", "joio", "trigo", "joio", "trigo", "joio", "trigo", "joio", "joio", "trigo", 
            "joio", "trigo", "joio", "trigo", "joio", "joio", "trigo", "joio", "trigo", "joio", 
            "trigo", "joio", "joio", "trigo", "joio", "trigo", "joio", "trigo", "joio", "joio", 
            "trigo", "joio", "trigo", "joio", "trigo", "joio", "joio", "trigo", "joio", "trigo", 
            "joio", "trigo", "joio", "joio", "trigo", "joio", "trigo", "joio", "trigo", "joio", 
            "joio", "trigo", "joio", "trigo", "joio", "trigo", "joio", "joio", "trigo", 
            "joio", "trigo", "joio", "trigo", "joio", "joio", "trigo", "joio", "trigo", "joio", 
            "trigo", "joio", "joio", "trigo", "joio", "trigo", "joio", "trigo", "joio", "joio", 
            "trigo", "joio", "trigo", "joio", "trigo", "joio", "joio", "trigo", "joio", "trigo", 
            "joio", "trigo", "joio", "joio", "trigo", "joio", "trigo", "joio", "trigo", "joio", 
            "joio", "trigo", "joio", "trigo", "joio", "trigo", "joio", "joio", "trigo", 
            "joio", "trigo", "joio", "trigo", "joio", "joio", "trigo", "joio", "trigo", "joio", 
            "trigo", "joio", "joio", "trigo", "joio", "trigo", "joio", "trigo", "joio", "joio", 
            "trigo", "joio", "trigo", "joio", "trigo", "joio", "joio", "trigo", "joio", "trigo", 
            "joio", "trigo", "joio", "joio", "trigo", "joio", "trigo", "joio", "trigo"]

joio = []
trigo = []

# separar o joio do trigo

for i in JoioTrigo:
    if i == "joio":
        joio.append(i)
for i in JoioTrigo:
    if i == "trigo":
        trigo.append(i)

print(joio)
print(trigo)