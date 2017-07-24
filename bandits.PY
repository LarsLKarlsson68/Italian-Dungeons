# -*- coding: latin_1 -*-
# Scenario with bandits


from gamemap import *
from agents import *
from things import *
from phrase import *
from random import choice
from italian_dungeons import *

bandit_verbs = ['essere','avere','sapere','potere','dovere','volere']
bandit_tempus = ['imperative','present','imperfect','conditional','future','perfect']

class Stiletto(Weapon):
    name='un stiletto'
    hp=3
    image='./img/sword.gif'
    
class WoodenClub(Weapon):
    name='un bastone'
    hp=2
    image='./img/stick.gif'
    
class SmallBandit(Enemy): 
    name='un bandito'
    hp=10
    strength=4
    move_max=1
    weapon=[WoodenClub,Stiletto]
    greeting_text = 'Un bandito attacca!'

    battle_text = 'Il bandito attacca!'
    defeated_text = 'Il bandito è morte!'
    sound = 'sounds/evillaugh.wav'
    image='./img/bandit.gif'
    questions =  [ phrase(bandit_verbs,tempus=bandit_tempus,
                          person=[['1s','2s','3sm','1p','2p','3pm'],
                                 ['1s','2s','3sf','1p','2p','3pf'],
                                 ['1s','2s','3sp','1p','2p','3pp']]) ]
    multiple_choice=6


class Lance(Weapon):
    name='una lancia'
    strength=4
    image='./img/spear.gif'
    
class Axe(Weapon):
    name='una scure'
    strength=4
    image='./img/axe.gif'

class BigBandit(Enemy):
    name='un bandito forte'
    hp=16
    strength=6
    move_max=2
    weapon = [Lance,Axe]
    greeting_text = 'Un bandito forte attacca!'
    battle_text = ['Il bandito è furioso!', 'Il bandito ula: Muori!']
    defeated_text = 'Il bandito è morte!'
    sound = 'sounds/evillaugh.wav'
    image='./img/bandit.gif'

    questions =  [ phrase(bandit_verbs,tempus=bandit_tempus,
                          person=['1s','1s','2s','2s','3sm','3sf',
                                  '1p','1p','2p','2p','3pm','3pf']) ]

class Sword(Weapon):
    name='una spada'
    strength=5
    image='./img/sword.gif'

class ChainMail(Armour):
    name='una maglia di ferro'
    strength=3
    image='./img/armour.gif'

class Purse(Thing):
    name='una borsa con i soldi'
    image='./img/thing.gif'
    
class BanditLeader(BigBandit):
    name='un capo dei banditi'
    hp=20
    strength=6
    move_max=2
    weapon = Sword
    armour = ChainMail
    things=[Purse]
    image='./img/bandit2.gif'
    greeting_text='Un capo dei banditi è qui!'
    
    def greeting(self,player,gui):
        Enemy.greeting(self,player,gui)
        if player.game.bandit_leaders_killed == 0:
            gui.prn('Dice: Una vittima. Bene!')
        elif player.game.bandit_leaders_killed < 3:
            gui.prn('Dice: Desidero vendetta!')
        else:
            gui.prn('Dice: Aiuto! Bah, muori, smidollato!')
            
    defeated_text =  'Uno dei capi dei banditi é morte.'

    def defeated(self,player,gui):
        player.game.bandit_leaders_killed += 1
        Enemy.defeated(self,player,gui)
    

class Wolf(Enemy):
    name='un lupo'
    hp=10
    strength=6
    move_max=2
    greeting_text = 'Un lupo ti sale!'
    defeated_text = 'Il lupo è morte!'
    questions = BigBandit.questions
    sound = 'sounds/wolf.wav'
    image='./img/wolf.gif'

class Elderman(AgentWithMessage):
    name='un anziano'
    move_max=0
    greeting_text = 'Vedi il anziano dell villagio.'
    image="./img/child.gif"    
    def talk_with(self,player,gui):
        if player.game.bandit_leaders_killed == 0:
            gui.prn('Il anzanio dice: Quattro bandi dei banditi atterrirono il nostro villagio! Devi uccidere i quattro capi dei banditi.')
        elif player.game.bandit_leaders_killed < 3:    
            gui.prn('Il anzanio dice: Bravo! Ma %s capi dei banditi rimanono.' % ['tre', 'due'][player.game.bandit_leaders_killed-1])      
        elif player.game.bandit_leaders_killed == 3:    
            gui.prn('Il anzanio dice: Bravo! Solo uno capo dei banditi rimane.')
        else:
            gui.prn("Sei un'eroe!")
        return False

class WorriedPeasant(AgentWithMessage):
    name='un contadino'
    move_max=1
    greeting_text = 'Vedi un povero contadino.'
    message_text = 'Il contadino dice: I banditi sono terribele.'
    image="./img/child.gif"

class MagicApple(Food):
    name='una mela incantata'
    hp=8
    image="./img/apple.gif"
    
class Ninfa(ReluctantAgentWithGift,WaryReluctantAgent):
    name='una ninfa'
    move_max=3
    things=[MagicApple]
    greeting_text = 'Vedi una bella ninfa.'
    message_text='Piaci la ninfa?'
    success_text = 'La ninfa ti da una mela magica, e parta nella foresta'
    failure_text = 'La ninfa in silenza parta nella foresta.'
    questions = BigBandit.questions
    image="./img/girl.gif"

class BlueBerries(Food):
    name='mirtilli'
    hp=2
    image='./img/berries.gif'

class Hero(Agent):
    name='Eroe'
    hp=20
    strength=5
    sp=20
    craft=4
    weapon = WoodenClub
    image="./img/hero.gif"
    visible_on_map = True

class Grass(FreeSpace):
    name=['Un prato con le fiore','Un campo']
    image='olivedrab1'
    
class DenseForest(MapItem):
    def can_enter(self,agent):
        return False
    cannot_enter_text='La foresta é troppo denso!'
    image='./img/densewood.gif'
    
class SparseForest(FreeSpace):
    name = ['Una foresta', 'Una foresta','Una foresta con alte alberi', 'Una collina nella foresta',\
                              'Una radura nella foresta', 'Una foresta molto vecchio']
    image='./img/sparsewood.gif'
        

class ForestPath(FreeSpace):
    image = 'yellow'
    name='Una via'
    
class House(FreeSpace):
    image='./img/house.gif'

class PeasantHouse(House):
    name='Una casa'
    agents=[WorriedPeasant]

class EldermanHouse(House):
    name='Una casa grande'
    agents=[Elderman]

class AbdandonedHouse(House):
    name='Una casa abbandonata'

class BanditGame(Game):
    name='Bandits'
    learning_goal='Auxilliary verbs'
    intro_text = 'Vai a un piccolo villagio nella foresta!' 
    startx = 1
    starty = 1
    pattern_table = {   ' ' : Grass,
                        'F' : DenseForest,
                        'f' : SparseForest,
                        'b' : (SparseForest,SmallBandit),
                        'B' : (SparseForest,BigBandit),
                        'L' : (SparseForest,BanditLeader),
                        'w' : (SparseForest,Wolf),
                        'm' : (SparseForest,BlueBerries),
                        '.' :  ForestPath,
                        'c' : (ForestPath,SmallBandit),
                        'P' : PeasantHouse,
                        'A' : AbdandonedHouse,
                        'E' : EldermanHouse,
                        'n' : (lambda : SparseForest(agents=[Ninfa()]))
                       }
    map_pattern = [ \
        'FFFFFFFFFFFFFFFFFFFF',    
        'F..c.......cFffwfFFF',        
        'FffBffmffw.fFFmfLnFF',    
        'FfwFFnfffP. ffffBfFF',    
        'FLmBfffff .fffbwfFFF',    
        'FFFfwff   .   ffFmFF',    
        'FFfbfA f P.Ef  ffffF',    
        'FFff..........ffffff',    
        'F.c..fffff.ff..c..ff',    
        '..ffff   f.f  fffc..',    
        'FffffFFFffc.ffffFfff',    
        'FFFFfbFFFff.fmFFBFFF',    
        'FBfmfffw  P.fffwnFFF',      
        'FLfnFwmFb c.FBf fLFF',    
        'FFFFFFFFFF.FFFFFFFFF']

    def setup(self):
        self.bandit_leaders_killed = 0
        self.success_announced=False
        
    def goal(self,gui,requested_help=False):
        if self.bandit_leaders_killed == 4:
            if not self.success_announced:
                self.success_announced = True
                gui.prn('<bf>','Ha completo il missione!')
            return True
        else:
            return False
    phrase_list=SmallBandit.questions+BigBandit.questions   

