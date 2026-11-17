from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_padrao:float = 0.400
    preco_kg:float = 82.40

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Este é {self.titulo} com {self.quant} pessoas participando."

    def calc_quant_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calc_custo_total(self) -> float:
        return self.calc_quant_carne() * self.preco_kg

    def calc_custo_indv(self) -> float:
        return self.calc_custo_total() / self.participantes
        
    def analisar(self):
        conteudo = f"Analisando [yellow]{self.titulo}[/] com [yellow]{self.participantes} convidados[/]"
        conteudo += f"\nCada participante comerá [blue]{Churrasco.consumo_padrao}Kg[/] e cada Kg custa [green]R${Churrasco.preco_kg:,.2f}[/]"
        conteudo += f"\nRecomendo comprar [blue]{self.calc_quant_carne():.3f}Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calc_custo_total():,.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calc_custo_indv():,.2f}[/] para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco("Churras dos Brodi", 15)
c1.analisar()

# Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e
# mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.