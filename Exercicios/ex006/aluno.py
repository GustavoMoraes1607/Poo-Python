from pessoa import Pessoa
from rich import print

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O Aluno [blue]{self.nome}[/] acabou de efetuar a [green]matrícula.[/]")