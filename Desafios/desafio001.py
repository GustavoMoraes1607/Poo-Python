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
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor {self.setor} da empresa {self.empresa}."

c1 = funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())
c2 = funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())
