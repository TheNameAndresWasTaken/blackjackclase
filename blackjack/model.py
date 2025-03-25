import random
from collections import defaultdict
from dataclasses import dataclass, field
from typing import ClassVar

CORAZON = "\u2764\uFE0F"
TREBOL = "\u2663\uFE0F"
DIAMANTE = "\u2666\uFE0F"
ESPADA = "\u2660\uFE0F"
OCULTA = "\u25AE\uFE0F"


@dataclass
class Carta:
    VALORES: ClassVar[list[str]] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    PINTAS: ClassVar[list[str]] = [CORAZON, TREBOL, DIAMANTE, ESPADA]
    pinta: str
    valor: str
    oculta: bool = True

@dataclass
class Baraja:
    cartas: list[Carta] = field(init=False, default_factory=list)

    def reiniciar(self):
        self.cartas.clear()
        for pinta in Carta.PINTAS:
            for valor in Carta.VALORES:
                self.cartas.append(Carta(pinta, valor))

    def revolver(self):
        random.shuffle(self.cartas)

    def repartir_cartas(self, oculta: bool = False) -> Carta | None:
        if len(self.cartas) > 0:
            carta = self.cartas.pop()
            if oculta:
                carta.ocultar()

            return carta
        else:
            return None


class Mano:

    def __init__(self):
        self.cartas: list[Carta] = []

    def es_blackjack(self) -> bool:
        if len(self.cartas) > 2:
            return False

        return self.cartas[0].valor == "A" and self.cartas[1].valor in ["10","J","Q", "K"] \
               or self.cartas[1].valor == "A" and self.cartas[0].valor in ["10","J","Q", "K"]

    def agregar_carta(self,carta: Carta):
        if carta.valor == "A"
            self.cartas.append(carta)
            self.cantidad_ases += 1

    def calcular_valor(self) -> int: