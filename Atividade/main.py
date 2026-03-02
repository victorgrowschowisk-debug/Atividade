from Enfermeiro import Enfermeiro
from Administrativo import Administrativo
from Medico import Medico
from Funcionario import Funcionario
from FuncionarioSaude import FuncionarioSaude
from Hospital import Hospital


def main():
    print("SISTEMA DE FUNCIONÁRIOS HOSPITALARES")
    
    

    hospital = Hospital("HOP")

    hospital.adicionar_funcionario(Enfermeiro("Maria",4000,1209,"UTI"))
    hospital.adicionar_funcionario(Medico("Fernanda",20000,4108,"FISIO"))
    hospital.adicionar_funcionario(Medico("Joao",15000,3809,"CARDIO"))
    hospital.adicionar_funcionario(Administrativo("Paty",2840,"ALMOX"))
    hospital.adicionar_funcionario(Enfermeiro("Marta",4000,4567,"Internacao"))
    print("--")
    hospital.listar_funcionarios()
    print("--")
    print(hospital.folha_pagamento())
    print("--")
    print(hospital.maior_salario())
    # hospital.maior_salario
    
    lista = hospital.get_lista()
    for item in lista:
        if (item.nome == "Marta"):
            print (item.setor)







main()