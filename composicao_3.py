class Motor:
    def ligar(self):
        print('Motor Ligado')



class Carro:
    def __init__(self):
        # instancia a classe Motor()
        self.motor = Motor()


    def ligar(self):
        # executa a funcao de de ligar do Motor()
        self.motor.ligar()
        print('Carro Ligado')



carro = Carro()
carro.ligar()
