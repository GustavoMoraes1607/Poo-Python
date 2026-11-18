from rich import print
class Caneta:
    def __init__(self, cor):
        match cor.lower().strip():
            case "azul":
                cor = "[blue]"
            case "vermelho":
                cor = "[red]"
            case "verde":
                cor = "[green]"
            case _:
                cor = "[white]"
        self.cor = cor
        self.tampada = True

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def escrever(self, conteudo):
        if self.tampada:
            print(f":prohibited: A{self.cor} caneta[/] está tampada.")
        if not self.tampada:
            print(f"{self.cor}{conteudo}[/]")


c1 = Caneta("vermelho")
c2 = Caneta("verde")
c3 = Caneta("azul")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá mundo! Vermelho")
c2.escrever("Olá mundo! Verde")
c3.escrever("Olá mundo! Azul")

        
# Crie uma classe Caneta, que simula o funcionamento de uma caneta colorida
# podendo escrever frases na cor relativa.