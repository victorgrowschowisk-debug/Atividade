from Enfermeiro import Enfermeiro
from Administrativo import Administrativo
from Medico import Medico
from Funcionario import Funcionario
from FuncionarioSaude import FuncionarioSaude
from Hospital import Hospital


def main():
    print("SISTEMA DE FUNCIONÁRIOS HOSPITALARES")
    
    Lista = []
    Lista.append (Enfermeiro("Maria",4000,1209,"UTI"))
    Lista.append (Medico("Fernanda",20000,4108,"FISIO"))
    Lista.append (Medico("Joao",15000,3809,"CARDIO"))
    Lista.append (Administrativo("Joao",2840,"ALMOX"))

    hospital = Hospital("HOP")

    hospital.adicionar_funcionario(Enfermeiro("Maria",4000,1209,"UTI"))
    hospital.adicionar_funcionario(Medico("Fernanda",20000,4108,"FISIO"))
    hospital.adicionar_funcionario(Medico("Joao",15000,3809,"CARDIO"))
    hospital.adicionar_funcionario(Administrativo("Paty",2840,"ALMOX"))
    hospital.adicionar_funcionario(Enfermeiro("Marta",4000,4567,"Internacao"))
    print("--")
    hospital.listar_funcionarios
    print("--")
    # hospital.maior_salariofghdfghdfghdfgh dfghdfgh

    #///////////////////////////////////////
    print("\nLista Funcionarios:")
    for item in Lista:
        item.exibir_dados()

    x = Enfermeiro("Maria",4000,1209,"UTI")
    x.exibir_dados()


main()