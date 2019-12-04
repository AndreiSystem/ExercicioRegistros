from pessoa import *

class Cliente(Pessoa):

    def cadastrar(self):
        with open('C:/Users/900213/Desktop/pythonClt2/Exercicio06/classes/banco/clientes.txt', 'a') as arquivo:
            arquivo.write(f'{self.id}; {self.name}; {self.last_name}; {self.cpf} \n')

    def listar(self):
        lista = []

        with open('C:/Users/900213/Desktop/pythonClt2/Exercicio06/classes/banco/clientes.txt', 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip().split(';')
                lista.append({'id': linha[0], 'name': linha[1], 'last-name': linha[2], 'cpf': linha[3]}) 
        
        return lista



