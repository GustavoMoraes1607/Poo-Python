from abc import ABC, abstractmethod
import math

class Poligono(ABC):

    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    def area(self):
        pass

class Quadrado(Poligono):

    def __init__ (self, lado):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2

class Circulo(Poligono):

    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2

# Implemente o seguinte diagrama de classes:

#Class Poligono (Abstract)
#+qnt_lados
#------------------------
#+perimetro() (Abstract)
#+area() (Abstract)

#SubClass Quadrado
#+lado
#------------------------
#+perimetro()
#+area()

#SubClass Circulo
#+raio
#------------------------
#+perimetro()
#+area()