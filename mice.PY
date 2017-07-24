# -*- coding: latin_1 -*-

from italian_dungeons import *
from gamemap import *
from agents import *
from things import *
import random
from phrase import *
from gameinterface import *

rat_verbs = ['parlare','lasciare','vendere','credere','finire','partire']
rat_tempus=['imperative','present','imperfect','conditional','future','perfect']


class Rat(Enemy):
    name='un ratto'
    hp=8
    strength=4
    sp=8
    craft=1
    move_max=2
    vulnerable_spirit = True
    battle_text = 'Il ratto attacca con i sui affiliati denti.'
    greeting_text = 'Un brutto ratto molto arrabbiato attacca!'
    image='./img/rat.gif'
    sound = './sounds/mouse.wav'
    questions = [ phrase(rat_verbs,
                         person=[['1s','2s','3sm','1p','2p','3pm'],
                                 ['1s','2s','3sf','1p','2p','3pf'],
                                 ['1s','2s','3sp','1p','2p','3pp']],
                         tempus=rat_tempus),
                phrase(rat_verbs,
                         person=['1s','1s','2s','2s','3sm',
                                  '1p','1p','2p','2p','3pm'],
                         tempus=[rat_tempus]),
                  ]
    multiple_choice=6
    
class BigRat(Rat):
    name='un ratto grande'
    hp=12
    strength=6
    move_max=2
    vulnerable_spirit = False
    questions = [ phrase(rat_verbs,
                         person=['1s','1s','2s','2s','3sm','3sf','3sp',
                                  '1p','1p','2p','2p','3pm','3pf','3pp'],
                         tempus=rat_tempus)  ]
    multiple_choice=False
    battle_text = 'Il grande ratto attacca con i sui denti, grandi con due stilletti.'
    greeting_text= 'Un ratto raramente grande attacca!'

class ReallyBigRat(BigRat):
    name='un ratto grandissimo'
    hp=16
    strength=8
    move_max=2
    vulnerable_spirit = False

    battle_text = 'Il enormo ratto attacca con i sui denti, grandi con due spade.'
    greeting_text=  'Un ratto orribile e grande attacca!'


class ChildInRatMaze(AgentWithMessage):
    name='un bambino'
    greeting_text = 'Vedi un piccolo bambino.'
    message_text = 'Il bamino dice: La mia sorella è raputo delgli topi. Lo salva!'
    image="./img/child.gif"    

class Lemonade(Food):
    name='una bottiglia di limonata'
    hp=4
    image="./img/bottle.gif"

class ChildToRescue(AgentWithGift):
    name='una bambina'
    greeting_text = 'Vedi una piccola bambina in paura.'        
    message_text = 'La bamina dice: Grazie grazie! Il formaggio del villagio è alle sud.\n'+\
                'La bambina ti da una bottiglia di limonata.'
    things = [Lemonade]
    image="./img/child.gif"
    
class Cheese(Food):
    name='un pezzo di formaggio'
    hp=2
    image="./img/cheese.gif"

class CheeseTreasure(Thing):
    name='tutti il formaggio'   
    image="./img/cheese.gif"

class LeatherArmour(Armour):
    name='una armatura di cuoio'
    strength=2
    image='./img/armour.gif'
    
class Branch(Weapon):
    name='un ramo'
    strength=1
    image='./img/stick.gif'

class WoodenClub(Weapon):
    name='un bastone'
    strength=2
    image='./img/stick.gif'

class Hammer(Weapon):
    name='un martello'
    strength=3
    image='./img/hammer.gif'

class Hero(Agent):
    name='Eroe'
    hp=20
    strength=5
    sp=20
    craft=4
    weapon = Branch
    image="./img/hero.gif"
    visible_on_map = True

class DirtyTunnel(FreeSpace):
    name=['Una galleria sporca','Un varco puzzolente','Un passagio stretto']    

class CaveRoom(FreeSpace):
    name='Una grande sala'
#    image='./img/clam.gif'
    
class CheeseTreasurePlace(CaveRoom):
    def events(self,player,gui):
        gui.prn('Sei arrivato con il grande sala dove è il formaggio!')

class RatTrap(Trap):
    description='Un passagio con una trappola'
    name='trappola'
    strength=5
    things=[Cheese]
    questions = [ phrase(rat_verbs,
                         person=['1s','1s','2s','2s','3sm','3sf','3sp',
                                  '1p','1p','2p','2p','3pm','3pf','3pp'],
                         tempus=rat_tempus)  ]

class RatGame(Game):
    name='Rats'
    learning_goal = 'Regular verb conjunctions'

    startx=1
    starty=1

    intro_text = 'I ratti hanno rubato il formaggio!'
    pattern_table = \
    { ' ' : DirtyTunnel,
        'r' : (DirtyTunnel,Rat),
        'f' : (DirtyTunnel,Cheese), # hp = 2
        'a' : (DirtyTunnel,LeatherArmour), # hp = 2
        'R' : (DirtyTunnel,BigRat),
        'c' : (DirtyTunnel,ChildInRatMaze),
        'd' : (DirtyTunnel,ChildToRescue),
        'b': (DirtyTunnel,WoodenClub),
        'm': (DirtyTunnel,Hammer),
        'G' : (CaveRoom,ReallyBigRat),
        's': CaveRoom,
        'T' : (CheeseTreasurePlace,CheeseTreasure),
        't' : RatTrap
       }
    map_pattern = [ \
        '############',
        '# #f r r   #',
        '# ## ##### #',
        '#cr  # R #t#',
        '#tr#a#b#r  #',
        '##########R#',
        '#d R R #f# #',
        '## ##t r R #',
        '## #########',
        '#  #m##Gsss#',
        '#RR#t #Gs#T#',
        '# f   #s####',
        '#####Gssfsr#',
        '    ########']

    notified_goal=False
    
    def goal(self,gui,requested_help=False):
        if self.player.count_things(CheeseTreasure):
            if not self.notified_goal or requested_help:
                gui.prn('Il missione é completto!')
                self.notified_goal = True
            return True
        else:
            if requested_help:
                gui.prn('Devi trovare il formaggio del villagio.')
            return False
    phrase_list= Rat.questions+BigRat.questions
    
opp = [ Rat, BigRat, ReallyBigRat, ChildInRatMaze, ChildToRescue, (RatTrap,None,ChildToRescue) ]
                    
            
        
    

    
