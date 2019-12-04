from pessoa import *

class Cliente(Pessoa):

    def cadastrar(self):
        with open('C:/Users/900213/Desktop/pythonClt2/Exercicio06/classes/banco/clientes.txt', 'a') as arquivo:
            arquivo.write(f'{self.id}; {self.name}; {self.last_name}; {self.cpf} \n')






joao = Cliente('joao', 'silva', 1231)
paulo = Cliente('paulo', 'luca', 2343)
juca = Cliente('juca', 'pinto', 1234)

joao.cadastrar()
paulo.cadastrar()
juca.cadastrar()