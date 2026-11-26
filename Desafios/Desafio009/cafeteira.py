from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print(f"--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print(f"--- Bebida Pronta ---\n")

    def ferver_agua(self):
        print(f"1. Fervendo água a 100 graus Celsius.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        print(f"2. Passando a água pressurizada pelo pó de café.")

    def servir(self):
        print(f"3. Servindo na xícara pequena de expresso.")

class Cha(BebidaQuente):

    def misturar(self):
        print(f"2. Mergulhando o sachê na água.")

    def servir(self):
        print(f"3. Servindo na xícara grande com uma rodela de limão.")

class Leite(BebidaQuente):

    def misturar(self):
        print(f"2. Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print(f"3. Servindo no copo grande com um pau de canela.")