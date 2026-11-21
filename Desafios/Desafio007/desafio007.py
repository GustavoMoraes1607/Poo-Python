from rich import print
from rich.panel import Panel

class ControleRemoto:
    canalmax = 10
    canalmin = 1
    volumemax = 10
    volumemin = 1

    def __init__(self, canal=1, volume=4):
        self.canal:int = canal
        self.volume:int = volume
        self.ligado:bool = False

    def on_off(self):
        self.ligado = not self.ligado

    def prox_canal(self):
        if self.ligado:
            if self.canal == ControleRemoto.canalmax:
                self.canal = ControleRemoto.canalmin
            else:
                self.canal += 1

    def canal_ant(self):
        if self.ligado:
            if self.canal == ControleRemoto.canalmin:
                self.canal = ControleRemoto.canalmax
            else:
                self.canal -= 1

    def aum_volume(self):
        if self.ligado:
            if self.volume != ControleRemoto.volumemax:
                self.volume += 1

    def dim_volume(self):
        if self.ligado:
            if self.volume != ControleRemoto.volumemin:
                self.volume -= 1
    
    def status_tv(self):
        conteudo = ""
        if not self.ligado:
            conteudo = f":TV: [red]A TV está desligada[/] :prohibited:"
        else:
            conteudo = f"[yellow]CANAL: [/]"
            for canal in range(ControleRemoto.canalmin, ControleRemoto.canalmax + 1):
                if canal == self.canal:
                    conteudo += f"[purple on yellow] {canal} [/]"
                else: 
                    conteudo += f" {canal} "
            conteudo += f"\n[yellow]VOLUME: [/]"
            for volume in range(ControleRemoto.volumemin, ControleRemoto.volumemax + 1):
                if volume <= self.volume:
                    conteudo += f"[yellow on green]|.[/]"
                else:
                    conteudo += f"[yellow on white]|.[/]"
        paineltv = Panel(conteudo, title="[ TV ]", width=45, height=5)
        print(paineltv)

ct = ControleRemoto()
while True:
    ct.status_tv()
    comando = str(input(f"| < CH >   - VOL + |"))
    match comando:
        case '0':
            break
        case '@':
            ct.on_off()
        case '<':
            ct.canal_ant()
        case '>':
            ct.prox_canal()
        case '-':
            ct.dim_volume()
        case '+':
            ct.aum_volume()
    print("\n" * 10)

# Crie a classe ControleRemoto, onde vamos simular o funcionamento
# de um controle simples (canal, volume e liga/desliga).