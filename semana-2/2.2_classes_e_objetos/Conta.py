class Conta:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0.0

    def depositar(self, valor):
        self._saldo += valor

    def obter_saldo(self):
        return self._saldo

conta1 = Conta(1111)
print('Conta 1: ', conta1.obter_saldo())

conta2 = Conta(2222)
conta2.depositar(500.0)

print('Conta 2: ', conta2.obter_saldo())
