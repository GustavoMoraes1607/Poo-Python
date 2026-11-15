from rich import print
class funcionario:
    empresa = "Curso em vídeo"
    """
    Uma classe que representa um funcionário, contendo nome, setor e cargo.
    """
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f"Funcionário: {self.nome}, Setor: {self.setor}, Cargo: {self.cargo}, Empresa: {self.emopresa}"

    def apresentacao(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {self.empresa}."

c1 = funcionario("Camila", "Administração", "Diretora")
print(c1.apresentacao())
c2 = funcionario("Gustavo", "TI", "Programador")
print(c2.apresentacao())

#Crie a classe Funcionario, onde podemos cadastrar o nome, setor e cargo.
#Crie também um método que permita o funcionário se apresentar.