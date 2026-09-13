# Heranca significa que uma classe pode receber caracteristicas e comportamentos de outra classe.

# super() --> permite que a classe filha aproveite o codigo da classe pai

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria


    def mostrar(self):
        print(f'Nome: {self.nome}, Preco: {self.preco}€')



class ProdutoFisico(Produto):
    def __init__(self, nome, preco, categoria, peso):
        # rodar o init do pai, depois o do filho 
        super().__init__(nome, preco, categoria)
        # init do filho
        self.peso = peso


    # sem super() sobiscrivi completamente o metodo do pai
    # sobrescrita do metodo pai
    # def mostrar(self):
    #     return print(f'Nome: {self.nome}, Preco: {self.preco}, Peso: {self.peso}')

    # com super() aproveita o comportamento do pai e acresenta/modifica alguma coisa
    def mostrar(self):
        super().mostrar() # executa o codigo do pai, depois executa o do filho
        print(f'Peso: {self.peso}')



pf = ProdutoFisico('Iphone', 12000, 'Smarphone', 0.5)
pf.mostrar()
