class aluno:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Aluno(a) e tem {self.idade} anos de idade."

# Declaração de objetos
a1 = aluno()
a1.nome = "Gustavo"
a1.idade = 25
a1.aniversario()
a2 = aluno()
a2.nome = "Augusto"
a2.idade = 28
a2.aniversario()
print(a1.mensagem())
print(a2.mensagem())
    