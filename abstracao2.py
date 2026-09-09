from abc import ABC, abstractmethod


class FormaPagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass


class Cartao(FormaPagamento):
    def pagar(self, valor):
        print(f'Pagando com Cartao. valor pago {valor}€')



class Paypal(FormaPagamento):
    def pagar(self, valor):
        print(f'Pagando com Paypal, valor pago {valor}€')



formas_pagamento = [
    Cartao(),
    Paypal()
]

for pagamento in formas_pagamento:
    pagamento.pagar(500)