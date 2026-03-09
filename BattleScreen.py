from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        self.elements = []

        y = 0
        #two rows of three
        trainerOneOrTwo = 1
        for trainer in self.trainers:
            if trainerOneOrTwo == 1:
                x = 10
                y = 90
            if trainerOneOrTwo == 2:
                x = 90
                y = 90
                
            for poke in trainer.pokemon:
                if trainerOneOrTwo == 1:
                    self.elements.append(Image((x, y), 20, 20, poke.img))
                    y -=18
                    self.elements.append(Label((x, y + 10), 20, 10, poke.name))
                    y -=23
                    trainerOneOrTwo +=1
            
                if trainerOneOrTwo == 2:
                    self.elements.append(Image((x, y), 20, 20, poke.img))
                    y -=18
                    self.elements.append(Label((x, y + 10), 20, 10, poke.name))
                    y -=23
   
                




