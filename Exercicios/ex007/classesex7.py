from rich import print, inspect
from abc import ABC, abstractmethod # Abstract Base Classes

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass
    

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O Aluno [blue]{self.nome}[/] acabou de efetuar a [green]matrícula.[/]")

    def estudar(self):
        print(f"{self.nome} está estudando {self.curso} na turma {self.turma}.")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def inic_aula(self):
        print(f"O professor [blue]{self.nome}[/] começou a [green]aula[/].")

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade} no {self.nivel}.")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionário [blue]{self.nome}[/] bateu o [green]ponto[/].")

    def estudar(self):
        print(f"{self.nome} se especializou para a área de {self.cargo} no setor {self.setor}.")