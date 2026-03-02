# Atividade SISTEMA DE FUNCIONÁRIOS HOSPITALARES 
DEV python Teste


PARTE 1 – Classe Abstrata: Funcionario 
Criar uma classe abstrata chamada Funcionario. 
Atributos obrigatórios: 
• nome 
• registro 
• salario 
• ativo (inicia como True) 
Métodos abstratos obrigatórios: 
• calcular_bonus() 
• descricao_funcao() 
Métodos concretos: 
• aumentar_salario(percentual) 
• desativar() 
• salario_total() (salário + bônus) 
• exibir_dados() 
Observação: 
A classe Funcionario não pode ser instanciada diretamente. 


PARTE 2 – Classe Intermediária: FuncionarioSaude 
Criar uma classe chamada FuncionarioSaude que herda de Funcionario. 
Novo atributo: 
• registro_conselho 
Novo método concreto: 
• validar_registro() 
Importante: 
Essa classe não deve implementar os métodos abstratos. 
Ela continua sendo abstrata. 


PARTE 3 – Classe Medico 
Herda de FuncionarioSaude. 
Atributos adicionais: 
• especialidade 
Regras: 
• Bônus de 20% sobre o salário 
• Implementar calcular_bonus() 
• Implementar descricao_funcao() 


PARTE 4 – Classe Enfermeiro 
Herda de FuncionarioSaude. 
Atributo adicional: 
• setor 
Regras: 
• Bônus de 15% sobre o salário 
• Implementar calcular_bonus() 
• Implementar descricao_funcao() 


PARTE 5 – Classe Administrativo 
Herda diretamente de Funcionario. 
Atributo adicional: 
• departamento 
Regras: 
• Bônus de 10% sobre o salário 
• Implementar calcular_bonus() 
• Implementar descricao_funcao() 


PARTE 6 – Classe Hospital 
Criar uma classe Hospital. 
Atributo: 
• lista_funcionarios (lista) 
Métodos: 
• adicionar_funcionario(funcionario) 
• listar_funcionarios() 
• folha_pagamento() (soma dos salários totais) 
Observação: 
Hospital não herda de Funcionario. 
Ela apenas armazena objetos (composição). 


DESAFIOS EXTRAS 
• Impedir salário negativo 
• Impedir bônus para funcionário inativo 
• Criar método no Hospital que retorne o funcionário com maior salário total 
