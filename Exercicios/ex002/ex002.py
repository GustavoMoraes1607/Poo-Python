class aluno:
    """
Essa classe cria um "aluno", que é uma pessoa com nome e idade.

Para criar um registro de novo aluno, use
variavel = Aluno(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): # Com n e i eu adiciono parâmetros para identifica-los, e o "= "", = 0" diz que atributo pode estar vazio.
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f"{self.nome} é Aluno(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: Nome = {self.nome} ; Idade = {self.idade}"

# Declaração de objetos
a1 = aluno("Gustavo", 25)
a1.aniversario()
a2 = aluno("Augusto", 28)
a2.aniversario()
print(a1)
print(a2)
print(a1.__doc__) # Dunder doc (Usado para procurar uma documentação sobre a classe em questão.)
print(a1.__dict__) # Dunder dict (Usado para procurar os atributos de uma classe.)
print(a1.__getstate__()) # Dunder getstate (Usado para procurar o estado de uma classe.)
print(a1.__class__) # Dunder class (Usado para procurar a classe de um objeto.)