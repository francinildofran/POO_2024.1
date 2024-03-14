class Conta:
    def __init__(self,nome, numero, saldo):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo


    def deposito(self):
        self.saldo += float(input())

    def saque(self):
        valor = float(input())
        if(self.saldo < valor):
            print("Saldo insuficiente")
        self.saldo -= valor
        print("Valor retirado: R$", valor )
    

usuario1 = Conta(input(), int(input()), float(input()))
usuario1.deposito()
usuario1.saque()
print("Seu saldo atual é: ", usuario1.saldo)