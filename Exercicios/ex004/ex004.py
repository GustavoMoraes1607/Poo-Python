from rich import print, inspect
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O Aluno [blue]{self.nome}[/] acabou de efetuar a [green]matrícula.[/]")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def inic_aula(self):
        print(f"O professor [blue]{self.nome}[/] começou a [green]aula[/].")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionário [blue]{self.nome}[/] bateu o [green]ponto[/].")

a1 = Aluno("José", 17, "Informática", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()

inspect(a1, methods=True)

p1 = Professor("Samuel", 37,"Biologia", "Mestrado")
p1.fazer_aniversario()
p1.inic_aula()

inspect(p1, methods=True)

f1 = Funcionario("Claudia", 28, "Secretária", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()

inspect(f1, methods=True)

