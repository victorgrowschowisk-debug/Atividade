from FuncionarioSaude import FuncionarioSaude


class Medico(FuncionarioSaude):
    def __init__(self, nome, salario, registro_conselho, especialidade):
        super().__init__(nome, salario, registro_conselho)
        self.especialidade = especialidade
    
    def calcular_bonus(self):
        return self.salario * 0.20
    
    def descricao_funcao(self):
        return ("Medico,", self.especialidade)