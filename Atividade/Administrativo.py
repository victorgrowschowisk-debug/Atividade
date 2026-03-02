from Funcionario import Funcionario


class Administrativo (Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome,salario,0)
        self.departamento = departamento

    def calcular_bonus(self):
        return self.salario * 0.1

    def descricao_funcao(self):
        return ("Admistrativo, ", self.departamento)