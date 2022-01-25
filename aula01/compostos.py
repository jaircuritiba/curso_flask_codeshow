# LISTAS
cores = ["verde", "amarelo", "azul", "branco"]
cores.append("preto")
cores.append("vermelho")
print(cores)
# cor no inicio da lista
cores.insert(0, "laranja")
print(cores)

cores.remove("branco")
print(cores)


# TUPLAS (Não permite alterações)
identidade = ("Bruno", "123456-9", 15)
print("Nome: ", identidade[0])
print("RG: ", identidade[1])
print("Idade: ", identidade[2])

# DICIONÁRIOS
pessoa = {"nome": "Carla", 
    "RG": "79764-9", 
    "idade": 18}

pessoa['idade'] = 19


for letra in 'Gabriel':
    if letra == 'a':
        continue
    print(letra)

# list COMPREHENSION
print([letra for letra in 'Gabriel'])

# list COMPREHENSION filter
print([letra for letra in 'Gabriel' if letra != "i"])


# pegar por chave
for chave in pessoa:
    print(chave, ": ", pessoa[chave])

print('---------------------------------')

for chave, valor in pessoa.items():
    print(chave, ": ", valor)