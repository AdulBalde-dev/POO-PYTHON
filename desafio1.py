class Produto:

    total_produtos = 0

    def __init__(self, nome, preco, categoria, estoque):
        self.nome = nome
        self._preco = preco
        self.categoria = categoria
        self._estoque = estoque
        
        Produto.total_produtos += 1

    @classmethod
    def mostrar_total(cls):
        return cls.total_produtos


    @classmethod
    def criar_do_texto(cls, texto):
        nome, preco, categoria, estoque = texto.split(',')
        return cls(
            nome,
            preco, 
            categoria, 
            estoque,
        )


    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError('O estoque nao pode ser negativo')

        self._estoque = valor

    @staticmethod
    def calcular_desconto(preco, percentual):
        return preco * (percentual / 100)

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError('O preo nao pode ser negativo')

        self._preco = valor


    def vender(self):
        if self._estoque <= 0:
            raise ValueError('Produto sem estoque.')

        self.estoque -= 1

    def repor_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError('A quantidade deve ser maior que zero.')

        self.estoque += quantidade

    def mostrar(self):
        print(f'Produto: {self.nome}, Preco: {self.preco}')


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, categoria, estoque, peso):
        super().__init__(nome, preco, categoria, estoque)
        self.peso = peso

    def mostrar(self):
        super().mostrar()
        print(f'Peso: {self.peso}kg')

class ProdutoDigital(Produto):
    def __init__(self, nome, preco, categoria, estoque, tamanho_mb):
        super().__init__(nome, preco, categoria, estoque)
        self.tamanho_mb = tamanho_mb

    def mostrar(self):
        super().mostrar()
        print(f'Tamanho em Mb: {self.tamanho_mb}Mb')


produtos = [ProdutoFisico('Iphone', 1500, 'Smartphone', 10, 1.5),
             ProdutoDigital('Macbook', 1500, 'Laptop', 10, 200)
            ]
for produto in produtos:
    produto.mostrar()