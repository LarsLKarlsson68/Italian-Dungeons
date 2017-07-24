import random
import math

class QuestElement:

    __expanded__ = False 

    def __init__(self,parent= None,grid=None,label=''):
        self.parent = parent
        self.label = label
        self.grid = grid
        self.children = dict()
        self.props = dict()
        
    # Expand the present quest element
    def expand(self):
      self.__expanded__ = True 
       
    # Selects expansions
    def select(self,label,number,alternatives):
        if type(number) == tuple:
            number = random.randint(number[0],number[1])
        remaining_alternatives = alternatives
        self.children.setdefault(label,list())
        start_index= len(self.children[label])
        for n in range(number):
            selected_alternative = random.choice(remaining_alternatives)
            remaining_alternatives.remove(selected_alternative)
            new_quest_element = selected_alternative(self,label)
            self.children[label].append(new_quest_element)
        for i in self.children[label][start_index:]:
            i.expand()


class KillDragonQuest(QuestElement):

    def expand(self):
        self.select('place', 1, [MountainQuestPlace, CaveQuestPlace])
        self.select('start', 1, [OldManQuestGiver, BardQuestGiver])
        self.select('reward', (1,2), [TreasureQuestItem, SwordQuestItem, ArmorQuestItem])
        super(KillDragonQuest,self).expand()

class MountainQuestPlace(QuestElement):
     pass                    
            
class CaveQuestPlace(QuestElement):
     pass   

class OldManQuestGiver(QuestElement):
     pass

class BardQuestGiver(QuestElement):
     pass

class TreasureQuestItem(QuestElement):
     pass

class SwordQuestItem(QuestElement):
     pass

class ArmorQuestItem(QuestElement):
     pass

