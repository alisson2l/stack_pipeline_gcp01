class Teste:
    def __init__(self, nome, cidade, telefone):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone

class TesteFilho(Teste):
    def speak(self, lingua):
        return lingua

a = Teste('Alisson','Rio','9999999')
b = Teste('Blison','Santa','88888')
c = Teste('Ze','Santana','55555')
d = Teste('Rai','Salvador','222222')

print(a.nome)
print(a.cidade)
print(a.telefone)
print(b.nome)
print(b.cidade)
print(b.telefone)


class Computador:
    def __init__(self, marca, memoria, placavideo):
        self.marca =  marca
        self.memoria = memoria
        self.placavideo = placavideo

    def Ligar(self):
        print('ligar')

    def Desligar(self):
        print('desligar')

    def Exibir(self):
        print(self.marca, self.memoria, self.placavideo)

computador1 = Computador('dell','8gb','gforce')

computador1.Ligar()
computador1.Exibir()
