from rich import print
from poligono import Quadrado, Circulo

def main():  
    q = Quadrado(12)
    print(f"Um quadrado de lado {q.lado}cm tem perímetro de {q.perimetro()}cm.")
    print(f"Um quadrado de lado {q.lado}cm tem area de {q.area()}cm.")

    c = Circulo(12)
    print(f"Um circulo de raio {c.raio}cm tem perímetro de {c.perimetro():.1f}cm.")
    print(f"Um circulo de raio {c.raio}cm tem area de {c.area():.1f}cm.")

if __name__ == "__main__":
    main()