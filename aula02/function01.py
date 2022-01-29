def ola1(nome):
    print(f"Olá,  {nome}")

ola1('Jair')
#ou
ola1(nome = "Deise")

#--------------------
def ola2(nome, maiusculo = False):
    if maiusculo:
        msg = f"Olá, {nome}".upper()
    else:
        msg = f"Olá, {nome}"

    print(msg)

ola2('Francisco')
ola2('Clarice', maiusculo=False)
ola2('Clara', True)

