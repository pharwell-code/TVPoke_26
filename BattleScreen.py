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
        trainerOneOrTwo = 1
        # for trainer in self.trainers:
        #     self.elements.append(Image((50, 50), 18, 18, poke.img))
            
        #     if trainerOneOrTwo == 1:
        #         x = 13
        #         y = 90
        #     else:
        #         x = 87
        #         y = 90
                
        #     for poke in trainer.pokemon:
        #         if trainerOneOrTwo == 1:
        #             self.elements.append(Image((x, y), 18, 18, poke.img))
        #             y -=13
        #             self.elements.append(Label((x, y), 20, 10, poke.name))
        #             y -=20
        #             trainerOneOrTwo +=1
            
        #         else:
        #             self.elements.append(Image((x, y), 18, 18, poke.img))
        #             y -=13
        #             self.elements.append(Label((x, y), 20, 10, poke.name))
        #             y -=20



        x = 35
        y = 50
        pokemon = self.trainers[0].pokemon[0]
        self.elements.append(Image((x, y), 20, 20, pokemon.img))
        self.elements.append(Label((x, y + 15), 20, 20, pokemon.name))
        

        x = 65
        y = 50
        pokemon = self.trainers[1].pokemon[0]
        self.elements.append(Image((x, y), 20, 20, pokemon.img))
        self.elements.append(Label((x, y + 15), 20, 20, pokemon.name))


class Attack1(Button):
    def __init__(self,pokemon):
        super().__init__((35, 40), 15, 5, (pokemon.move), (0, 255, 0), ) #adding moves for the pokemon. hard code each button? possibly. for the text, need to get each of the special abilitys

        


