class aluno:
    """
Essa classe cria um "aluno", que é uma pessoa com nome e idade.

Para criar um registro de novo aluno, use
variavel = Aluno(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): # Com n e i eu adiciono parâmetros para identifica-los, e o "= "", = 0" diz que atributo pode estar vazio.
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Aluno(a) e tem {self.idade} anos de idade."

# Declaração de objetos
a1 = aluno("Gustavo", 25)
a1.aniversario()
a2 = aluno("Augusto", 28)
a2.aniversario()
a3 = aluno()
print(a1.mensagem())
print(a2.mensagem())
print(a3.mensagem())
print(a1.__doc__) # Dunder doc (Usado para procurar uma documentação sobre a classe em questão.)