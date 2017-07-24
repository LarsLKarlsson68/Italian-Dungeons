# -*- coding: cp1252 -*-
from italian_dungeons import *
from gamemap import *
from agents import *
from things import *
import random
from phrase import *
from gameinterface import *
from domestic import *
import winsound

## Outdoor places

class Path(FreeSpace):
    image='./img/road.gif'
    name='Una via'

class Road(FreeSpace):
    image='lightgrey'
    name='Una via'

class Field(FreeSpace):
    image='./img/grass.gif'
    name='Un campo'
 
class Well(FreeSpace):
    image='./img/well.gif'
    name='Un pozzo'

class VegetableField(FreeSpace):
    image="./img/vegetables.gif"
    name='Un campo di verdure'

class TreeBottom(BelowCliff):
    name="Sotto un'albero"
    image="./img/bigtree.gif[0,1]"
    questions= q4
    strength=2
    
class TreeTop(AboveCliff):
    name="In un'albero"
    image="./img/bigtree.gif[0,0]"
    def can_enter(self,agent):
        return isinstance(agent.place,TreeBottom)
    def can_leave(self,player,to_place,gui):
        return isinstance(to_place,TreeBottom)
    
# Indoor places
class MansionFloor(FreeSpace):
    image='grey75'
    name='In un bel palazzo'
    
class MansionLockedDoor(LockedDoor):
    image='./img/doortiles.gif'
    image_opp='./img/doortiles-open.gif'
    name='Una porta'

class StudyDoor(MansionLockedDoor):
    code='study'
    
class MansionOpenDoor(LockedDoor):
    image='./img/doortiles-open.gif'
    image_opp='./img/doortiles.gif'
    name='Una porta'
    locked = False
    
class MansionWall(Wall):
    image='./img/tiles2.gif'
class MansionWallWindow(Wall):
    image='./img/tiles-window.gif'
class MansionWallTapestry(Wall):
    image=('./img/tiles-tapestry.gif','./img/tiles-tapestry2.gif')

class Fireplace(FreeSpace):
    image='./img/fireplace.gif'
    name='Un caminetto'
class Table(FreeSpace):
    image='./img/table.gif'
    name='Un tavolo'
class Chair(FreeSpace):
    image='./img/chair.gif'
    name='Una sedia'
class TableAndStool(FreeSpace):
    image='./img/table-n-stool.gif'
    name='Una tavola semplice'
class Bed(FreeSpace):
    image='./img/bed.gif'
    name='Un letto'
class Barrels(FreeSpace):
    image='./img/barrels.gif'
    name='Qualche botti'
class Carpet(FreeSpace):
    image=('./img/carpet.gif','./img/carpet2.gif','./img/carpet3.gif')
    name='Un bel tapetto'
class Bookshelf(FreeSpace):
    image='./img/bookshelf.gif'
    name='Una libreria'
class Jarshelf(FreeSpace):
    image='./img/jarshelf.gif'
    name='Scaffali con i vasetti'
class Bottleshelf(FreeSpace):
    image='./img/bottleshelf.gif'
    name='Scaffali con le bottigle'

class Armory(FreeSpace):
    image='./img/armory.gif'
    name='Un arsenale'

class Chest(LockedContainer):
    name='Un baule'
    image='./img/chest-closed.gif'
    image_opp='./img/chest-open.gif'

class TrapDoorUp(FreeSpace):
    name = 'una scala'
    image = "./img/trapdoor-up.gif"

class TrapDoorDown(FreeSpace):
    name = 'una scala'
    image = "./img/trapdoor.gif"

class SpiritStartingPosition(MansionFloor):
    pass

class Tunnel(FreeSpace):
    image='darkgrey'
    name='Un passaggio molto buio'

class EarthWall(Wall):
    image='./img/earthwall.gif'
    
class Hill(FreeSpace):
    image = "./img/hill.gif"
    name='Una collinetta con una apertura'

class CommonSword(Weapon):
    name='una spada'
    strength=5
    image='./img/sword.gif'

class Purse(Thing):
    name='una borsa con i soldi'
    image='./img/thing.gif'

class Bread(Food):
    name='un pane'
    image='./img/bread.gif'
    hp=2

class Ham(Food):
    name='un prosciutto'
    image='./img/ham.gif'
    hp=4

class Spider(Enemy):
    name='un ragno'
    hp=8
    strength=4
    move_max=2
    battle_text = 'Il ragno attacca.'
    vulnerable_spirit = False
    questions = q1
    greeting_text =  'Un ragno corre verso te!'
    image="./img/spider.gif"
    sound = './sounds/insect.wav'

class Squirrel(Enemy):
    name='un scoiattolo grande' 
    hp= 12
    strength=4
    move_max=0
    image = './img/squirrel.gif'   
    sound = './sounds/squirrel.wav'
    visible_on_map = False
    questions= q3

class Rabbit(Enemy):
    name='un coniglio grande' 
    hp= 15
    strength=5
    move_max=2
    image = './img/rabbit.gif'
    sound = './sounds/rabbit.wav'
    visible_on_map = False
    questions= q2
    greeting_text =  'Un coniglio grande attacca!'

class Spirit(Enemy):
    name='una fantasma malevolenza'
    sp=12
    craft=6
    move_max=2
    magic_text= 'la fantasma trova a ti paralizzare.'
    vulnerable_body = False
    questions = q5+q6
    greeting_text = 'Una fantasma malevolenza si avvincia!'
    sound = './sounds/ghost2.wav'
    image = "./img/blackspirit.gif"

class Mario(AgentWithMessage):
    name= 'il singore Mario'
    move_max=0
    image = './img/hero2.gif'    
#    sound = file_name (opt)
    visible_on_map = True
    greeting_text='Il signore Mario è qui.'

    def talk_with(self,player,gui):
        if not player.game.spirits_done:
            gui.prn("Il signore dice: Le fantasme, le fantasme! Non doveva incantare le formule magice nell vecchio libro.") 
        else:
            gui.prn("Il signore dice: Grazie!")


class Lance(Weapon):
    name='una lancia'
    strength=4
    image='./img/spear.gif'

class Cheese(Food):
    name='un pezzo di formaggio'
    hp=3
    sp=3
    image="./img/cheese.gif"

class MagicApple(Food):
    name='una mela incantata'
    sp=8
    image="./img/apple.gif"

class Maria(AgentWithMessage):
    name= 'la singora Maria'
    move_max=0
    image = './img/girl.gif'    
#    sound = file_name (opt)
    visible_on_map = True

    # For keeping track of progress
    bread_given = False
    spiders_done=False
    rabbits_done=False
    squirrels_done=False
    spirits_done=False
    greeting_text='La signora Maria è qui.'
    
    def talk_with(self,player,gui):
        if not player.game.spiders_done:
            gui.prn("La signora dice: Ce sono molti ragni nel primo piano della casa.")
            if not self.bread_given:
                gui.prn('Ti da due pani.')
                Bread().init_move(player)
                Bread().init_move(player)
                self.bread_given = True
            return True
        elif not self.spiders_done:
            self.spiders_done = True
            gui.prn("La signora dice: Grazie per uccidere i ragni.")
            gui.prn('Ti da una lancia e un prosciutto.')
            Lance().init_move(player)
            Ham().init_move(player)
        if not player.game.rabbits_done:
            gui.prn("La signora dice: Ce sono molti conigli nell'orto.")            
            return True
        elif not self.rabbits_done:
            self.rabbits_done = True
            gui.prn("La signora dice: Grazie per uccidere i conigli.")
            gui.prn('Ti da due pezzi di formaggio.')
            Cheese().init_move(player)
            Cheese().init_move(player)
        if not player.game.squirrels_done:
            gui.prn("La signora dice: Ce sono molti scoiatoli nell'alberi.")
            return True
        elif not self.squirrels_done:
            self.squirrels_done = True
            gui.prn("La signora dice: Grazie per uccidere i scoiatoli.")
            gui.prn('Ti da una bella mela.')
            MagicApple().init_move(player)
        if not player.game.spirits_activated:
            gui.prn("La signora dice: Mi preoccupato il signore Mario. È su nell studio.")
        elif not player.game.spirits_done:
            gui.prn("La signora dice: Qualcosa terribele è successo!")
        elif not self.spirits_done:
            gui.prn("La signora dice: Grazie!")
            self.spirits_done = True
        else:
            gui.prn("La signora dice: Ora tutto è bene!")
            
class SpiritBook(MagicThing):
    name='un vecchio libro'
    off=2
    deff=2
    opponent_class=Spirit
    understand=5
    image='./img/book.gif'
    questions=q5+q6


class WoodenClub(Weapon):
    name='un bastone'
    hp=2
    image='./img/stick.gif'
            
class Hero(Agent):
    name='Eroe'
    hp=20
    strength=5
    sp=20
    craft=4
    visible_on_map = True
    weapon = WoodenClub
    image="./img/hero.gif"
    
class HouseGame(Game):
    startx = 7
    starty = 5
    name="Home sweet home"
    learning_goal="Domestic (verbs, nouns, adjectives)" 

    pattern_tables ={\
        'main': {\
        '#': MansionWall,
        '.' : Path,
        '=' : Road,
        '_' : Field,
        'v' : VegetableField,
        'V': (VegetableField, Rabbit),
        ' ':MansionFloor,
        'H': (MansionFloor,Ham),
        'D': (MansionFloor,Bread),
        '#':MansionWall,
        '&':MansionWallWindow,
        'd': MansionOpenDoor,
        '%': MansionWallTapestry,
        'f': Fireplace,
        't': Table,
        'c': Chair,
        's': TableAndStool,
        'b': Barrels,
        'C': Carpet,
        'l': Bookshelf,
        'j': Jarshelf,
        'w': Bottleshelf,
        'k': Chest,
        'a': Armory,
        'B': Bed,
        '0': (TreeTop,Squirrel),
        '|': TreeBottom,
        'I': (TreeBottom,MagicApple),
        'x': (MansionFloor,Spider),
        'y': SpiritStartingPosition,
        '1': (Hill, lambda : GateWay('underground','[en]tro')),
        '2': (TrapDoorUp, lambda : GateWay('main_secondfloor','[su]')),
        '3': (TrapDoorDown, lambda : GateWay('main_secondfloor','[g]iù','main')),
        '4': StudyDoor,
        '5': (MansionFloor,Maria),
        '6': (Table,SpiritBook)
        },
        'underground': {\
        ' ' : EarthWall,
        'p' : Tunnel,
        'D' : (Tunnel,Bread),
        '1' : (Tunnel, lambda : GateWay('underground','[es]ci','main')),
        'P' : (Tunnel,Rabbit)
        }
            
    }
    map_patterns= {\
        'main': [\
            '_0_0_0__0_0__0_',
            '_|_|_|_.|_|__I_',
            '_______._______',
            '1vvvV__.____vvV',
            '_vvvv__.____vvv',
            '_______.______v',
            '__#&###d#&###__',
            '__#tc%  %x j#__',
            '__#C d 5d tf#__',
            '__&xl# C#H b#__',
            '__####2 ##%##__',
            '__#BB% c%a k#__',
            '__&CxdD d xs#__',
            '__##&##d##&##__',
            '_______._______'
            
            ],
        'main_secondfloor': [\
            '#&###&#%#&##',
            '#at d yk# f#',
            '&yC ##d##yc&',
            '#t k#H  d l#',
            '#####3 C####',
            '#lly4  DdyB#',
            '&6cy% t % C&',
            '###&##&###&#'
            ],
            
        'underground': [\
            '        ',
            ' 1ppPpp ',
            '   p  D ',
            '  DP  P ',
            ' pp  pp ',
            '        '
            ]
        
    }

    def activate_spirits(self,gui):        
        gui.prn("Senti un'urlo terrorizato!")
        winsound.PlaySound('./sounds/man_scream.wav',0)
        for p in self.maps['main_secondfloor'].get_places(SpiritStartingPosition):
            Spirit().init_move(p)
        for p in self.maps['main_secondfloor'].get_places(StudyDoor):
            p.lock_or_unlock(gui)
            Mario().init_move(p)

    def setup(self):
        self.spiders=self.maps['main'].get_agents(Spider)
        self.rabbits=self.maps['main'].get_agents(Rabbit)+self.maps['underground'].get_agents(Rabbit)
        self.squirrels=self.maps['main'].get_agents(Squirrel)
        self.Maria=self.maps['main'].get_agents(Maria)[0]
        self.spirits=[]
        self.spiders_done=False
        self.rabbits_done=False
        self.squirrels_done=False
        self.spirits_done=False
        self.spirits_activated=False
        
    def goal(self,gui,req_help=False):
        self.spiders_done= self.spiders_done or every(lambda x: x.dead, self.spiders) 
        self.rabbits_done= self.rabbits_done or every(lambda x: x.dead, self.rabbits) 
        self.squirrels_done= self.squirrels_done or every(lambda x: x.dead, self.squirrels) 
        self.spirits_done= self.spirits_done or (self.spirits_activated and every(lambda x: x.dead, self.spirits)) 
        if self.Maria.squirrels_done and not self.spirits_activated and random.random() < 0.25:
            self.activate_spirits(gui)
            self.spirits_activated=True
            self.spirits=self.maps['main_secondfloor'].get_agents(Spirit)
        return False

    phrase_list = q1+q2+q3+q4+q5+q6
    
