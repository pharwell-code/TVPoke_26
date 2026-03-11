from TVPoke.BaseClasses.PokeTypes import Grass
from TVPoke.BaseClasses.Move import Move

class Oddish(Grass):
    def __init__(self):
        moves = [
            Move(),
            Move(),
            Move(),
            Move()
        ]
        super().__init__("Oddish", 90, moves, "./TVPoke/Pokemon/imgs/Oddish.png")