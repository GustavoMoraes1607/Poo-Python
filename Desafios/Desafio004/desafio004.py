from rich import print
import time

class Livro:

    def __init__(self, titulo, totalpag, currpag=1):
        self.titulo = titulo
        self.totalpag = totalpag
        self.currpag = currpag

    def __str__(self):
        return f"{self.titulo} é um livro e contém {self.totalpag} páginas."

    def avancar_pag(self, avancar=0):
        cont = 0
        for pg in range (0, avancar, 1):
            if self.currpag == 1:
               print(f":open_book: [blue]Você acabou de abrir o livro [red]'{self.titulo}'[/] e está na [yellow]página {self.currpag}[/].[/]")
            if not self.fim_do_livro():
                self.currpag += 1
                print(f"Pág{self.currpag} :arrow_forward: ", end =' ')
                time.sleep(0.3)
                cont += 1
        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.currpag}[/][/]")
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'.[/]")
            
    def fim_do_livro(self) -> bool:
        if self.currpag == self.totalpag:
            return True
        else:
            return False
        

l1 = Livro("Entendendo algoritmos", 20)
l1.avancar_pag(20)

# Crie a classe Livro, que vai simular a passagem de páginas de um livro.
# considerando também se o usuário chegou ao fim da leitura.