from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favgame = list()

    def __str__(self):
        return f"{self.nome} tem o nick {self.nick} e os seus jogos favoritos são: {self.favgame}."

    def add_fav(self, game):
        self.favgame.append(game)
        self.favgame = sorted(self.favgame, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [white on blue] {self.nome} [/]"
        conteudo += f"\nJogos favoritos:"
        for num, game in enumerate(self.favgame):
            conteudo += f"\n:video_game: [blue]{game}[/]"
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)

g1 = Gamer("Gustavo Rocha", "Gusz")
g1.add_fav("Terraria")
g1.add_fav("Don't Starve")
g1.add_fav("Rust")
g1.ficha()

g2 = Gamer("Tales Mundo","Carbi")
g2.add_fav("Rain World")
g2.add_fav("Celeste")
g2.add_fav("Outer Wilds")
g2.ficha()

# Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# Crie também um método que permita mostrar a ficha desse gamer.