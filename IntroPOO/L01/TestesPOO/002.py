#class Pessoa:
#   nome = "joao"
#   idade = 30
    
#pessoa1 = Pessoa()
#pessoa1.nome = "Kaio"
#print(pessoa1.nome)

class Pessoa:
    #def falar(self, mensagem):
    #   print(f"{self.nome} diz: {mensagem}")
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


#pessoa1 = Pessoa()
#pessoa1.nome = "João"
#pessoa1.falar("Olá")
        
pessoa1 = Pessoa("João", 30)
print(pessoa1.nome)
print(pessoa1.idade)


