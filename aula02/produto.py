from loja.modelos import Categoria, Produto

cadeira = Produto("Cadeira", categoria=Categoria("Móveis"))
teclado = Produto("HyperX", categoria=Categoria("Eletrônicos"))

print(cadeira.nome, cadeira.categoria.nome)
print(teclado.nome, teclado.categoria.nome)