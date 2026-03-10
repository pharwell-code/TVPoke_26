from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (40, 50, 75))

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        self.elements = []

        for move in self.trainers[0].pokemon[0].moves:
            self.elements.append(Button((x , y), 20, 10, move.name))
            y = -15

        y = 0
        #two rows of three
        trainerOneOrTwo = 1
        for trainer in self.trainers:
            if trainerOneOrTwo == 1:
                x = 13
                y = 85
            if trainerOneOrTwo == 2:
                x = 87
                y = 85
                
            for poke in trainer.pokemon:
                if trainerOneOrTwo == 1:
                    self.elements.append(Image((x, y), 18, 18, poke.img))
                    y -=15
                    self.elements.append(Label((x, y + 4), 20, 10, poke.name))
                    y -=20
                    trainerOneOrTwo +=1
            
                if trainerOneOrTwo == 2:
                    self.elements.append(Image((x, y), 18, 18, poke.img))
                    y -=15
                    self.elements.append(Label((x, y + 4), 20, 10, poke.name))
                    y -=20

        


