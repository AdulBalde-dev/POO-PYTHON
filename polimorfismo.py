class Produto:
    def mostrar(self):
        print('Metodo genérico')



class ProdutoFisico(Produto):
    def mostrar(self):
        print('Produto Fisico')


class ProdutoDigital(Produto):
    def mostrar(self):
        print('Produto Digital')


# pfisico = ProdutoFisico()
# pfisico.mostrar()

# pdigital = ProdutoDigital()
# pdigital.mostrar()



# usando for
produtos = [
    ProdutoFisico(),
    ProdutoDigital()
]

for produto in produtos:
    produto.mostrar()