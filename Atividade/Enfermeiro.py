from FuncionarioSaude import FuncionarioSaude


class Enfermeiro (FuncionarioSaude):
    def __init__(self, nome,salario, registro_conselho, setor):
        super().__init__(nome,salario,registro_conselho)
        self.setor = setor
    
    def calcular_bonus(self):
        return self.salario * 0.15
    
    def descricao_funcao(self):
        return ("Enfermeiro,", self.setor)