def produto(nome, preco):
    print(f"{nome} -> R$ {preco}")

produto("Caderno", 14.80)

############ *args ################

def produto1(nome, preco, *args):
    print(f"{nome} -> R$ {preco} - {args}")

produto1("Cola", 16.50, "1Kg", "PVA")

############ *kwargs ################

def produto2(nome, preco, *args, **kwargs):
    print(f"{nome} -> R$ {preco} - {args} - {kwargs}")

produto2("Lápis", 1.50,  "Grafite 8", "Anatômico", material = "madeira", marca = "Fundepar")