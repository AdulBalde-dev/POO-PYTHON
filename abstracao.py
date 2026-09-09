from abc import ABC, abstractmethod

# Essa classe é um modelo/BASE, nao pode instanciar ela.
class Produto(ABC):

    # metodo obrigatorio que toda classe filha deve implementar
    @abstractmethod
    def mostrar(self):
        pass

# se instancia sem implementar vai dar erro.
class ProdutoFisico(Produto):
    def mostrar(self):
        print('Produto Fisico')

class ProdutoDigital(Produto):
    def mostrar(self):
        print('Produto Digital')




produtos = [
    ProdutoFisico(),
    ProdutoDigital()
]

for produto in produtos:
    produto.mostrar()