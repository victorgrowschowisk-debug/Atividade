from abc import ABC, abstractmethod

class Funcionario(ABC):
    
    def __init__(self,nome,salario,registro):
        self.nome = nome
        self.registro = registro
        self.salario = salario
        self.ativo = True  
    

    @abstractmethod
    def calcular_bonus(self):
        pass
    
    @abstractmethod
    def descricao_funcao(self):
        pass
    

    def aumentar_salario(self, percentual):
        aumento =  self.salario * (percentual / 100)
        self.salario = self.salario + aumento
    
    def desativar(self):
        self.ativo = False
    
    def salario_total(self):
        return self.salario + self.calcular_bonus()
    
    def exibir_dados(self):
        print("Nome: ", self.nome)


# • Impedir salário negativo 
# • Impedir bônus para funcionário inativo 
# • Criar método no Hospital que retorne o funcionário com maior salário total 