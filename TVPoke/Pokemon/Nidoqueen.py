from TVPoke.BaseClasses.PokeTypes import Poison
from TVPoke.BaseClasses.Move import Move

class NidoQueen(Poison):
    def __init__(self):
        moves = [
            Move("Poisen point", "POISEN", 40),
            Move("Sludge wave", "POISON", 40),
            Move("Body slam", "NORMAL", 80),
            Move("Rock slide", "NORMAL", 0)
        ]
        super().__init__("NidoQueen", 80, moves, "./TVPoke/Pokemon/imgs/NidoQueen.png")