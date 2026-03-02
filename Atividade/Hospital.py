
class Hospital:
    def __init__(self, nome):
        self.nome = nome
        self.lista_funcionarios = []
        # self.lista_funcionarios = lista_funcionarios 

    

    def adicionar_funcionario(self, funcionario): 
        self.lista_funcionarios.append(funcionario)
        print("ADICIONADO")

    def listar_funcionarios(self):
        print("Lista")
        for item in self.lista_funcionarios:
            item.exibir_dados()
        print("Lista")    

    def folha_pagamento(self):
        return sum(item.salario_total() for item in self.lista_funcionarios)
    
    def maior_salario(self):
         for item in self.lista_funcionarios:
            item.salario