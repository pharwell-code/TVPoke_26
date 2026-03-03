from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Magmar(Fire):
    def __init__(self):
        moves = [
            Move("Heat Wave", "FIRE", 100),
            Move("V- Create-", "FIRE", 180),
            Move("Sacred Fire", "FIRE", 100),
            Move("Eruption", "FIRE", 200)
        ]
        super().__init__("Magmar", 120, moves, "magmar.png")