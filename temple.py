# -*- coding: cp1252 -*-
from italian_dungeons import *
from gamemap import *
from agents import *
from things import *
import random
from phrase import *
import space_time
from gameinterface import *
from mind import q1, q2, q3, q3b, q4, q5, q6, q7, q8


class Skull(Thing):
    name='un cranio'
    image='./img/skull.gif'

class Bone(Thing):
    name='un osso'
    image='./img/bone.gif'

class GraveYard(HidingPlace):
    image="./img/grave.gif"
    name = 'Un cimitero'
    hidden_things=[[Skull,Bone,False,False,False]]
    
class Tomb(FreeSpace):
    image="./img/tomb.gif"
    name='Una vecchia tomba'
    
class Altar(FreeSpace):
    image="./img/altar.gif"
    name = 'Un altare macchiato di sangue'

class Floor(FreeSpace):
    image='lightgrey'
    name='Dentro il tempio'

class InnerTemple(FreeSpace):
    image='grey'
    name='Dentro la sala interiore del tempio'
    things=[[Skull,Bone,False,False,False,False]]
    
class ToolHouse(Floor):
    name='Una casa con attrezzature'
    
class Path(FreeSpace):
    image='./img/road.gif'
    name='Una via'

class Field(FreeSpace):
    image='./img/grass.gif'
    name='Un campo'

class OuterFloor(Floor):
    name='Fuori il tempio'

class Statue(Floor):
    name=('Una statua imponente','una statua bella')
    image=('./img/statue1.gif','./img/statue2.gif')

class Pillars(Wall):
    image='./img/pillars.gif'
    
class TempleDoor(LockedDoor):
    image = "./img/doortiles.gif"
    image_opp = "./img/doortiles-open.gif"
    name='una porta grande con immagine belle'

class TempleDoor1(TempleDoor):
    code='temple1'

class TempleDoor2(TempleDoor):
    code='temple2'

class OpenDoor(LockedDoor):
    image_opp = "./img/doortiles.gif"
    image = "./img/doortiles-open.gif"
    name='Una porta'
    locked=False
    
class DemonIdol(Floor):
    name='una statua maligna'
    description='Questa brutta statua ha malignità'
    image='./img/idol1.gif'
    destroyed=False
    def destroy(self,player,gui):
        if not self.destroyed:
            self.destroyed = True
            gui.prn('La statua è rotta!')
            self.image='./img/rubble.gif'
            self.game_map.show_place_again(self,gui)

Wall.image = "./img/tiles2.gif"
Thing.image = "./img/thing.gif"

class CommonSword(Weapon):
    name='una spada'
    strength=5
    image='./img/sword.gif'


class Spade(Thing):
    name='una pala'
    image='./img/mace.gif'

    def use(self,player,gui):
        place=player.place
        if isinstance(place,GraveYard):
            gui.prn('Scavi!')
            if place.hidden_things:
                gui.prn('Trovi qualcosa!')
                place.uncover(gui)
        else:
            gui.prn('Non puoi!')


    
                
class Hero(Agent):
    name='Eroe'
    hp=20
    strength=5
    sp=20
    craft=4
    weapon = CommonSword
    image="./img/hero.gif"
    visible_on_map=True
    

class GuardingSpirit(GuardingAgentOnce):
    name='una fantasma guardia'
    sp=12
    craft=4
    vulnerable_body=False
    move_max=2
    magic_text= 'La fantasma trova a ti paralizzare.'
    greeting_text = 'Puoi domare la fantasma guardia?'
    success_text = 'La fantasma ti lascia passare.'
    failure_text = 'La fantasma urla!'
    sound = './sounds/ghost2.wav'
    image = "./img/blackspirit.gif"
    tries=3
    questions = 2*[ q1 ]+[ q2 ]+3*[ q3 ] 

class Dagger(Weapon):
    name='un pugnale'
    strength=3
    image='./img/sword.gif'

class Skeleton(Enemy):
    name='un scheletro'
    hp = 12
    strength = 2
    sp=16
    craft=1
    weapon = Dagger
    greeting_text='Un scheletro attacca!'
    battle_text='Il scheletro attacca!'
    image='./img/skeleton.gif'
    questions = [ q4 ]


class Hammer(Weapon):
    name='un martello'
    strength=4
    image='./img/hammer.gif'
    opponent_class = Skeleton
    special_strength=4
    description='Questo martello pesante puo rompere sasso e osso.' 

    def use(self,player,gui):
        if isinstance(player.place,DemonIdol):
            player.place.destroy(player,gui)
        else:
            Weapon.use(self,player,gui)
            
class Demon(Enemy):
    name='un demonio'
    greeting_text='In fumo e fiamme, un terribile demonio appare!'
    sp=25
    craft=10
    vulnerable_body=False
    move_max=0
    image='./img/demon1.gif'
    sound='./sounds/lightning.wav'
    questions= 4*[ q5 ]+ 3*[ q6 ]+ [q7, q8 ]

class Skeleton2(Skeleton):
    weapon=CommonSword
    questions= [q3, q3b ]

class Skeleton3(Skeleton):
    weapon=CommonSword
    questions= GuardingSpirit.questions
    
class DemonBook(MagicThing):
    name='un vecchio libro'
    off=3
    deff=3
    opponent_class = Demon
    understand=6
    description='É un libro molto vecchio, con simboli strani.'
    activated_description= 'Il libro ha formuli di cacciare via i demoni'
    questions= Demon.questions
    image='./img/book.gif'

class DoorKeepingSpirit(ReluctantAgentOpeningDoor,WaryReluctantAgent):
    tries = 2
    move_max=2
    name='una fantasma triste'
    greeting_text='Una fantasma triste é qui.'
    message_text = 'La fantasma triste dice: non puoi passare la porta!\nPuoi convincere la fantasma?'
    success_text = 'La fantasma apre una porta.'
    failure_text = 'La fantasma scompare.'
    sound = './sounds/ghost2.wav'
    image = "./img/ghost1.gif"
    questions=GuardingSpirit.questions         

class Potion(Food):
    name='una bottiglia'
    hp=6
    sp=6

class Bread(Food):
    name='un pane sacro'
    image='./img/bread.gif'
    hp=3
    sp=3
    
class SpiritWithPotion(ReluctantAgentWithGift,WaryReluctantAgent):
    tries = 2
    move_max=2
    name='una fantasma triste'
    greeting_text='Una fantasma triste é qui.'
    message_text = 'La fantasma triste dice: non puoi prendere la mia bottiglia!\nPuoi convincere la fantasma?'
    success_text = 'La fantasma ti da una bottiglia.'
    failure_text = 'La fantasma scompare.'
    sound = './sounds/ghost2.wav'
    image = "./img/ghost1.gif"
    questions=GuardingSpirit.questions
    things = [ Potion ]
    
class DoorKeepingSpirit1(DoorKeepingSpirit):
    code='temple1'

class DoorKeepingSpirit2(DoorKeepingSpirit):
    code='temple2'

class GhostTellingAboutBook(AgentWithMessage):
    name= 'una phantasma preoccupata'
    move_max=0
    image = './img/ghost1.gif'    
    visible_on_map = True
    greeting_text='Una phantasma aspetta qui!'
    message_text='La phantasma dice: Signore Cato aveva un libro di demoni.'

class TempleGame(Game):
    name="Temple of the dead"
    learning_goal="The mind (verbs incl subjunctive form, nouns, adjectives)" 
    startx=7
    starty=20
    
    pattern_table = {\
        'g': GraveYard,
        's': (GraveYard,Skeleton),
        'z': (GraveYard,Skeleton2),
        't': ToolHouse,
        'o': Field,
        'H': (ToolHouse,Skeleton,Hammer),
        'S': (ToolHouse,Skeleton2,Spade),
        '.': Path,
        'b': (GraveYard,GhostTellingAboutBook),
        '1': TempleDoor1,
        'A': (DoorKeepingSpirit1,OuterFloor),
        '2': TempleDoor2,
        'B': (DoorKeepingSpirit2,Floor),
        'f': OuterFloor,
        'I': Pillars,
        'X': Statue,
        'G': (Floor,GuardingSpirit),
        ' ':Floor,
        'D':(Floor,Demon),
        'a':Altar,
        'i': InnerTemple,
        '3': (DemonIdol,Demon),
        '4': (InnerTemple,Skeleton3),
        'P': (Floor,SpiritWithPotion),
        'd': OpenDoor
    }

    map_pattern= [\
        'ooo#########ooo',
        'ooo#iai3iai#ooo',
        'ooo#i4iii4i#ooo',
        'ooo#iii4iii#ooo',  
        'ooo####i####ooo',
        'oooo#II2II#oooo',
        'oooo#X    X#oooo',
        'ooo##G a G##ooo',
        'ooo#P# B #P#ooo',
        'ooo# dG Gd #ooo', 
        'oo#####d#####oo',
        'oo#X   D   X#oo',
        'oo#X G   G X#oo',
        'oo#X   G   X#oo',
        'oo##II#1#II##oo',
        '###fffffffAf###',
        '#ggggzg.gzgggg#',
        '#gsgsgb.ggsgzg#',
        '###oooo.oooo###',
        '#Hdoooo.oooodS#',
        '#######.#######' ]

    def setup(self):
        graveyard_places=self.maps['main'].get_places(GraveYard)
        catos_grave=random.choice(graveyard_places)
        catos_grave.hidden_things = [DemonBook()]
        places_for_bread = random.sample(self.maps['main'].get_places(GraveYard)+self.maps['main'].get_places(Floor),6)
        for p in places_for_bread:
            b = Bread()
            b.init_move(p)
        catos_grave.name = catos_grave.name+"\nA una tomba c'è scritto: Cato, Grande Mago."
        self.demon_idol=self.maps['main'].get_places(DemonIdol)
        

    goal_achieved=False
    
    def goal(self,gui,help_req=False):
        if every(lambda x: x.destroyed, self.demon_idol) and not self.goal_achieved:
            self.goal_achieved=True
            gui.prn('<bf>','Bravo!')
        return self.goal_achieved
                    

    phrase_list = [q1,q2,q3,q3b,q4,q5,q6,q7,q8]

