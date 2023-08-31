*SISTEMA DE HOSPITAL*

Nesse sistema, os pacientes são atendidos por médicos em consultas e podem compartilhar quartos. Além disso, os médicos podem pertencer a diferentes especialidades.

*ENTIDADES*

Paciente:
id_paciente (chave primária)
nome
data_nascimento
endereco

Médico:
id_medico (chave primária)
nome
especialidade

Consulta:
id_consulta (chave primária)
id_paciente (chave estrangeira referenciando a tabela Paciente)
id_medico (chave estrangeira referenciando a tabela Medico)
dados_consulta

Quarto:
id_quarto (chave primária)
numero_quarto

Compartilhamento_Quarto:
id_compartilhamento (chave primária)
id_paciente_1 (chave estrangeira referenciando a tabela Paciente)
id_paciente_2 (chave estrangeira referenciando a tabela Paciente)


*RELACIONAMENTOS*
Relacionamento 1 para N entre Paciente e Consulta: Um paciente pode ter várias consultas, mas cada consulta é para um único paciente.

Relacionamento N para 1 entre Consulta e Medico: Cada consulta é realizada por um médico, mas um médico pode realizar várias consultas.

Relacionamento 1 para 1 entre Paciente e Compartilhamento_Quarto: Dois pacientes podem compartilhar um quarto, formando um relacionamento de 1 para 1.

Relacionamento N para N entre Paciente e Compartilhamento_Quarto: Vários pacientes podem compartilhar um quarto, e um paciente pode compartilhar um quarto com vários outros pacientes.

*O modelo relacional das tabelas do Sistema de Hospital*

Tabela Paciente:
   - `Paciente` armazena informações sobre os pacientes atendidos no hospital.
   - A chave primária (`PK`) é `id_paciente`, que identifica unicamente cada paciente.

Tabela Medico:
   - `Medico` contém informações sobre os médicos que atendem no hospital.
   - A chave primária (`PK`) é `id_medico`, que identifica cada médico de forma exclusiva.

Tabela Consulta:
   - `Consulta` registra informações sobre as consultas realizadas entre pacientes e médicos.
   - A chave primária (`PK`) é `id_consulta`, que identifica cada consulta de forma única.
   - A chave estrangeira (`FK`) `id_paciente` refere-se à tabela `Paciente`, vinculando o paciente à consulta.
   - A chave estrangeira (`FK`) `id_medico` refere-se à tabela `Medico`, vinculando o médico à consulta.

Tabela Quarto:
   - `Quarto` armazena informações sobre os quartos do hospital.
   - A chave primária (`PK`) é `id_quarto`, que identifica cada quarto de forma única.

Tabela Compartilhamento_Quarto:
   - `Compartilhamento_Quarto` guarda informações sobre os quartos compartilhados no hospital.
   - A chave primária (`PK`) é `id_compartilhamento`, que identifica cada compartilhamento de quarto de forma única.
   - A chave estrangeira (`FK`) `id_quarto` está relacionada à tabela `Quarto`, conectando o compartilhamento ao quarto.

Tabela Paciente_Compartilhamento:
   - `Paciente_Compartilhamento` estabelece a relação de muitos-para-muitos entre pacientes e compartilhamentos de quarto.
   - A chave primária (`PK`) é composta por `id_paciente` e `id_compartilhamento`, garantindo unicidade.
   - A chave estrangeira (`FK`) `id_paciente` é referenciada à tabela `Paciente`, associando o paciente ao compartilhamento.
   - A chave estrangeira (`FK`) `id_compartilhamento` é referenciada à tabela `Compartilhamento_Quarto`, vinculando o compartilhamento ao paciente.
