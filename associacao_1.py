# class Cliente:
#     def __init__(self, nome):
#         self.nome = nome


#     def comprar(self, produto: Produto):
#         print(f'{self.nome} comprou {produto.nome}')

# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco


# cliente = Cliente('Adul')
# iphone = Produto('Iphone', 12000)

# cliente.comprar(iphone)


class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Gerente:
    def __init__(self, nome):
        self.nome = nome


    def supervisionar(self, funcionario: Funcionario):
        print(f'{self.nome} está supervisionando {funcionario.nome}')


func = Funcionario('Adul')

gerente = Gerente('Herr Kuhnert')
gerente.supervisionar(func)

