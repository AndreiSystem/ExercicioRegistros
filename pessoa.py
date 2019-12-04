id = 0
class Pessoa:
    
    def __init__(self, name, last_name, cpf):
        id_lista = []
        global id
        self.name = name
        self.last_name = last_name
        self.cpf = cpf
        id += 1
        self.id = id
        id_lista.append(id)


        

    def get_name(self):
        return self.name
    
    def get_last_name(self):
        return self.last_name

    def get_cpf(self):
        return self.cpf


