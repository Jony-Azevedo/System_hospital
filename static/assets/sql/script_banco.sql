DROP DATABASE IF EXISTS at_pb;
CREATE DATABASE IF NOT EXISTS at_pb;
USE at_pb;
-- Criar Tabelas
CREATE TABLE Paciente (
    id_paciente INT PRIMARY KEY,
    nome VARCHAR(50),
    data_nascimento DATE,
    endereco VARCHAR(100)
);

CREATE TABLE Medico (
    id_medico INT PRIMARY KEY,
    nome VARCHAR(50),
    especialidade VARCHAR(50)
);

CREATE TABLE Consulta (
    id_consulta INT PRIMARY KEY,
    id_paciente INT,
    id_medico INT,
    data_consulta DATE,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_medico) REFERENCES Medico(id_medico)
);

CREATE TABLE Quarto (
    id_quarto INT PRIMARY KEY,
    numero_quarto INT
);

-- Tabela Compartilhamento_Quarto
CREATE TABLE Compartilhamento_Quarto (
    id_compartilhamento INT PRIMARY KEY,
    id_quarto INT,
    FOREIGN KEY (id_quarto) REFERENCES Quarto(id_quarto)
);


-- Tabela Paciente_Compartilhamento
CREATE TABLE Paciente_Compartilhamento (
    id_paciente INT,
    id_compartilhamento INT,
    PRIMARY KEY (id_paciente, id_compartilhamento),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_compartilhamento) REFERENCES Compartilhamento_Quarto(id_compartilhamento)
);
-- Inserir Dados

-- Tabela Paciente
INSERT INTO Paciente (id_paciente, nome, data_nascimento, endereco)
VALUES
    (1, 'Maria', '1990-05-15', 'Rua A, 123'),
    (2, 'João', '1985-08-20', 'Av. B, 456');

-- Tabela Medico
INSERT INTO Medico (id_medico, nome, especialidade)
VALUES
    (101, 'Dr. Silva', 'Cardiologia'),
    (102, 'Dra. Santos', 'Ortopedia');

-- Tabela Consulta
INSERT INTO Consulta (id_consulta, id_paciente, id_medico, data_consulta)
VALUES
    (201, 1, 101, '2023-08-01'),
    (202, 2, 102, '2023-08-02');

-- Tabela Quarto
INSERT INTO Quarto (id_quarto, numero_quarto)
VALUES
    (301, 101),
    (302, 102);

-- Tabela Compartilhamento_Quarto
INSERT INTO Compartilhamento_Quarto (id_compartilhamento, id_quarto)
VALUES
    (401, 301),
    (402, 302);

-- Tabela Paciente_Compartilhamento
INSERT INTO Paciente_Compartilhamento (id_paciente, id_compartilhamento)
VALUES
    (1, 401),
    (2, 401),
    (2, 402);
    
USE at_pb;
SHOW TABLES;
SELECT * FROM compartilhamento_quarto;
SELECT * FROM paciente_compartilhamento;