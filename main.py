class Produto:

    # Atributos de Classe
    total_produtos = 0


    def __init__(self, nome, preco, categoria, estoque):
        # Atributos de instancia
        self.nome = nome
        self._preco = preco
        self.categoria = categoria
        self._estoque = estoque

        # aumentando 1 toda vez que criamos um objeto
        Produto.total_produtos = Produto.total_produtos + 1


    @classmethod
    def mostrar_total(cls):
        print(f'Total de produtos: {cls.total_produtos}')

    
    # pegar o dados pasados, tratar eles e criar um novo objeto
    @classmethod
    def criar_do_texto(cls, texto):
        nome, preco, categoria, estoque = texto.split(',')

        # como se fosse: produto = Produto(nome, preco, categoria, estoque)
        return cls(
            nome,
            float(preco),
            categoria,
            int(estoque)
        )

    
    @staticmethod
    def calcular_desconto(preco: int | float, percentual: int):
        return preco * (percentual / 100)

    # pega/le o valor
    @property
    def preco(self):
        return self._preco

    # altera/define o valor
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError('O valor nao pode ser negativo.')

        self._preco = valor


    # ler estoque/pegar valor do estoque
    @property
    def estoque(self):
        return self._estoque

    # alterar ou definir estoque
    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError('Valor nao pode ser negativo.')

        self._estoque = valor


    def vender(self):
        if self.estoque <= 0:
            raise ValueError('Produto sem estoque')

        self.estoque -= 1
        print('Produto sem estoque')


    def repor_estoque(self, quantidade: int):
        if quantidade < 0:
            raise ValueError('Quantidade nao pode ser negativo.')
        
        self.estoque = self.estoque + quantidade


p1 = Produto('Iphone', 1200, 'Smartphone', 1)

percento = Produto('Iphone', 1500, 'Smartphone', 10).calcular_desconto(1000, 50)
print(percento)

# p2 = Produto('Camisas', 50, 'Roupa', 2)

# Produto.mostrar_total()



# api = 'Iphone,30000,Smartphone,50'

# p3 = Produto.criar_do_texto(api)
# print(p3.nome)
# print(p3.estoque)
