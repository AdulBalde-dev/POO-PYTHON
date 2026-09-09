class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Loja:
    def __init__(self, nome: str):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

tv = Produto('Tv', 1500)
iphone = Produto('Iphone', 2000)
pc = Produto('Lenovo', 2500)

loja = Loja('Media Markt')

loja.adicionar_produto(tv)
loja.adicionar_produto(iphone)
loja.adicionar_produto(pc)

for produto in loja.produtos:
    print(produto.nome)