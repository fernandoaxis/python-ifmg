class Conta:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0.0

    def depositar(self, valor):
        self._saldo += valor

    def obter_saldo(self):
        return self._saldo

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False

conta1 = Conta(1111)
print('Conta 1: ', conta1.obter_saldo())

conta2 = Conta(2222)
conta2.depositar(2000.0)
conta2.sacar(1000)

print('Conta 2: ', conta2.obter_saldo())

conta2.transferir(conta1, 500)

saldo_conta1 = conta1.obter_saldo()
saldo_conta2 = conta2.obter_saldo()

print('Saldo após a transferencia: ')
print('Conta1: ', saldo_conta1 )
print('Conta2: ', saldo_conta2 )
