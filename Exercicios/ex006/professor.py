from pessoa import Pessoa
from rich import print

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def inic_aula(self):
        print(f"O professor [blue]{self.nome}[/] começou a [green]aula[/].")