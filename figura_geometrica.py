# pylint: disable=R0903

"""Este módulo define figuras geométricas básicas y calcula sus áreas."""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta que define una figura geométrica."""

    @abstractmethod
    def calcular_area(self):
        """Calcula el área de la figura geométrica."""
        raise NotImplementedError("Este método debe ser implementado por una subclase.")


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura


class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2


class Circulo(FiguraGeometrica):
    """Clase que representa un círculo."""

    def __init__(self, radio):
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return self.pi * (self.radio ** 2)


# Constantes de ejemplo
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3


if __name__ == "__main__":
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")
