from Funcionario import Funcionario


class FuncionarioSaude(Funcionario):
    def __init__(self, nome, salario, registro_conselho):
        super().__init__(nome, salario, 0)
        self.registro_conselho = registro_conselho
    
    def validar_registro(self):
        if self.registro_conselho > 0:
            return True
        return False
    
    def calcular_bonus(self):
        pass

    def descricao_funcao(self):
        pass