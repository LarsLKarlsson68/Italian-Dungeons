# -*- coding: cp1252 -*-
from italian_dungeons import *
from gamemap import *
from agents import *
from things import *
import random
from phrase import *
from conjunctions import *
import space_time
from gameinterface import *

def test_query(q,times=1):
    for i in range(times):
        qc = q.choice()
        print(qc.it(),qc.eng())

# Relative pronouns

q1 = noun_phrase(["l'uomo/man","la donna/woman"],
                 post=phrase(subject=rel_pronoun_phrase(eng_form="who",person=["3sm"]),
                        verb=["venire","partire"]))

test_query(q1,0)

q2 = noun_phrase(["l'uomo/man","la donna/woman"],
                 post=phrase(pre=rel_pronoun_phrase(eng_form="whom",person=["3sm"]),
                             person=['1s','2s','1p','2p'],
                        verb=["vedere","incontrare"]))

test_query(q2,0)

q3 = noun_phrase(["l'uomo/man","la donna/woman"],
                 post=phrase(pre=rel_pronoun_phrase(person=False,eng_form="whose",obj_noun=["il libro/book","la tazza/cup"],obj_kind=["s","p"]),
                             person=['1s','2s','1p','2p'],
                            verb=["prendere","portare"]))

test_query(q3,0)

q4 = noun_phrase(["l'uomo/man","la donna/woman"],
                 post=phrase(pre=rel_pronoun_phrase(eng_form="whom",person=["3sm"],prep=["a","da"]),
                             person=['1s','2s','1p','2p'],
                        verb=["andare"]))

test_query(q4,0)

# Conjunctions

q5 = phrase(conj=single_conjuctions,
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["mangiare","bere"])

test_query(q5,0)

q6 = phrase(person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["venire","parlare"],
    post= phrase(conj=combining_conjunctions,
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["partire","udire"]))

test_query(q6,0)


q7 = phrase(person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["venire","parlare"],
    post= phrase(conj=conditional_conjunctions,
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["partire","udire"]))

test_query(q7,0)

q8 = phrase(person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["mangiare","dormire"],
    post= phrase(conj=time_conjunctions,
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["venire","partire"]))

test_query(q8,0)

q9 = phrase(conj="se",
            person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["venire","parlare"],tempus='subjunctive imperfect',
    post= phrase(
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["partire","udire"],tempus="conditional"))

test_query(q9,0)

q10 = phrase(person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["lavorare","pagare"],
    post= phrase(conj=cause_goal_conjunctions,
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],

                verb=["mangiare","partire","andare"]))

test_query(q10,0)

q11 = phrase(person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["vedere","udire","sapere"],
    post= phrase(conj='come',
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["desiderare","fare","fare","mangiare","andare","parlare","vivere"]))

test_query(q11,5)

# Interrogatives
q12 = query_phrase(interrogative = ['quando','perchè','come','dove'],
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["mangiare","bere","andare"],tempus=['present','perfect','future'])

test_query(q12,10)

q13 = query_phrase(interrogative = 'chi(0)',
                verb=["mangiare","bere","andare","venire"],tempus=['present','perfect','future'])

test_query(q13,5)

q14 = query_phrase(interrogative = 'chi(1)',
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["aiutare","amare","odiare"],tempus=['present','perfect','future'])

test_query(q14,5)

q15 = query_phrase(interrogative = 'di chi',
                person=['3smn','3pmn'],
                verb=["essere"],tempus=['present','perfect','future'])

test_query(q15,5)

q16 = query_phrase(interrogative = 'quale(0)', int_obj=['il libro/book','la tazza/cup','il pane/bread','il cane/dog'],
                   int_kind=['s','p'],
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["comprare","prendere","portare"],tempus=['present','perfect','future'])

test_query(q16,5)

q17 = query_phrase(interrogative = ['quanto(1)'], int_obj=['il libro/book','la tazza/cup','la mela/apple'],
                int_kind='p',
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["comprare","prendere","portare"],tempus=['present','perfect','future'])

test_query(q17,5)


q18 = query_phrase(interrogative = 'quale(0)', int_prep=['a','con'], int_obj=['la donna/woman','il uomo/man'],
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["andare","venire"],tempus=['present','perfect','future'])

test_query(q18,5)

q19 = query_phrase(interrogative = ['quale(0)','quanto(0)'], int_obj=['il vino/wine',"l'olio/oil"],
                int_kind='s',
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["comprare","prendere","portare"],tempus=['present','perfect','future'])

test_query(q19,5)

q20 = query_phrase(interrogative = ['quale(1)','quali'],
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["comprare","prendere","portare"],tempus=['present','perfect','future'])

test_query(q20,5)

q21 = query_phrase(interrogative = ['dove'],
                subject=['la donna/woman',"l'uomo/man", "la tavola/table", "la sedia/chair", "la casa/house"],
                verb=["essere"],tempus=['present','perfect','future'])

test_query(q21,5)

q22 = query_phrase(interrogative = 'che cosa', 
                person=['1s','2s','3sm','3sf','1p','2p','3pm','3pf'],
                verb=["comprare","prendere","portare"],tempus=['present','perfect','future'])

test_query(q22,5)

class BigSpider(Enemy):
    name='un ragno gigante'
    hp=10
    strength=4
    move_max=2
    battle_text = 'Il ragno gigante attacca.'           
    vulnerable_spirit = False

    questions = [ q5,q6,q7,q8,q9,q10, q11 ]
    greeting_text =  'Un ragno gigante corre verso te!'
    image="./img/spider.gif" 
    sound = './sounds/insect.wav'

class Spectre(Enemy):
    name='un spettro'
    sp=14
    craft=6
    move_max=0
    magic_text= 'Il spettro desidera succhiare la tua anima.'
    vulnerable_body = False
    greeting_text = 'Un spettro con occhie rosse si avvincia!'
    image="./img/spectre.gif"
    sound = './sounds/ghost2.wav'
    questions = [ q5,q6,q7,q8,q9,q10, q11 ]
    
class Mace(Weapon):
    name='una mazza'
    strength=5
    image='./img/mace.gif'

class Ogre(Enemy):
    name='un orco grande con una mazza'
    hp=15
    strength=5
    move_max=2
    weapon=Mace
    battle_text = "L'orco attacca."           
    vulnerable_spirit = False
    questions = [ q12, q12, q12, q12, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q21, q22 ]
                              
    greeting_text = 'Un orco grande con una mazza ti vede è attacca instantemente!'
    image = "./img/ogre2.gif"          
    sound = './sounds/grunt.wav'


class CommonSword(Weapon):
    name='una spada'
    strength=4
    image='./img/sword.gif'

class LongSword(Weapon):
    name='una spada lunga'
    strength=6
    image='./img/sword.gif'

class ChainMail(Armour):
    name='una maglia di ferro'
    strength=3
    image='./img/armour.gif'

class Hero(Agent):
    name='Eroe'
    hp=20
    strength=5
    sp=20
    craft=4
    visible_on_map = True
    weapon = CommonSword
    image="./img/hero.gif"

class RedApple(Food):
    name='una mela rossa'
    hp=2
    sp=2
    image='./img/apple.gif'
    
class GreenPear(Food):
    name='una pera verde'
    hp=3
    sp=3
    image='./img/pear.gif'

class Ham(Food):
    name='un prosciutto'
    hp=4
    sp=4
    image="./img/ham.gif"
    
class DenseForest(MapItem):
    def can_enter(self,player):
        return False
    cannot_enter_text = 'La foresta é troppo fitto.'
    image = "./img/densewood.gif"

class SparseForest(FreeSpace):
    name=['Una foresta', 'Una foresta','Una foresta con alte alberi', 'Una collina nella foresta',\
                              'Una radura nella foresta', 'Una foresta molto vecchio']
    image = ["./img/sparsewood.gif","./img/sparsewood2.gif","./img/sparsewood3.gif"]

class ForestPath(FreeSpace):
    image='./img/road.gif'
    name='Una via'
    
class Shrine(FreeSpace):
    image = "./img/shrine.gif"
    name='Un vecchio e tranquillo santuario nella foresta'
    
class Hill(FreeSpace):
    image = "./img/hill.gif"
    name='Una collinetta'


class HillCave(FreeSpace):
    image = "./img/hill-cave.gif"
    name='Una collinetta con una porta oscura'
    
class Field(FreeSpace):
    image='./img/grass.gif'
    name='Un campo'
    
                  

class Crystal(Thing):
    image='./img/crystal.gif'
    name='un cristallo'

    
class Swamp(KeepingTrap):
    name='Una palude'
    image = './img/swamp.gif'
    intro_text = 'Entri una palude traditore'
    disarmed_text = 'Trovi una via attraverso la palude'
    effect_text = 'Ti impigli nella palluda'
    strength= 3
    craft = 1
    questions=[q1,q2,q3,q4]

class ThornBushes(KeepingTrap):
    name='Cespugli'
    intro_text = "Questi cespugli hanno lunghi spini."
    strength=2
    effect_text = "Gli spini ti fa male."
    questions=[q1,q2,q3,q4]
    image="./img/thorn.gif"

class GraveYard(FreeSpace):
    image="./img/grave.gif"
    name = 'un cimitero'

class DirtyTunnel(FreeSpace):
    name=['Una galleria sporca','Un varco puzzolente','Un passagio stretto']    

class CaveRoom(FreeSpace):
    name='Una grande sala'

class CaveGate(FreeSpace):
    name='Un portone'
    image='./img/gatetiles-open.gif'

class CaveObstacle(Wall):
    image=['./img/altar.gif','./img/idol1.gif','./img/fire.gif']
    
class TrollGame(Game):
    name='The troll cave'
    learning_goal = 'Conjunctions, relative pronouns'
    intro_text='Trova quattro cristalli nella caverna degli orci!'
    startx=7
    starty=15
    pattern_tables ={ \
        'main': {\
        ' ' : Field,
        '.' : ForestPath,
        'c' : Hill,
        '1': (HillCave, lambda: GateWay('1', '[en]tra', 'cave','1')),
        'F' : DenseForest,
        'f' : SparseForest,
        'S' : (SparseForest,BigSpider),
        's': Swamp,
        't': ThornBushes,
        'g': GraveYard,
        '2': (GraveYard,Spectre,LongSword),
        '3': (GraveYard,Spectre,ChainMail)

        },
        'cave': {
        ' ' : DirtyTunnel, 
        's': CaveRoom,
        'O': (CaveRoom,Ogre),
        'g': CaveGate,
        'o': CaveObstacle,
        '1': (CaveGate, lambda: GateWay('1', '[es]ce', 'main ','1'))
       }

    }
    map_patterns = {
        'main':
        [
        'FFFFFFFFFFFFFFFFF',
        'Ffffc sscfff tFFF',
        'Ft2gffscsFFcFFSfF',
        'FsFScssc1fFFF  cF',
        'Ff fcf  fS    ccF',
        'Ffg  fSFFFFFffS3fF',
        'FftffcFFSFFssssFF',
        'Ff  FFF    sssgFF',
        'Fft   ctSFFFF   F',
        'FfffS       f ftF',
        'F    FFFFFF ffSfF',
        'F  ssss     ffffF',
        'F  sccs  ssss   F',
        'F tssSs   scsfSfF',
        'F tS   FFFFFF   F',
        'F  FFF   fSfs ccF'
        'FFFFFFFFFFFFFFFFF' ],
        'cave':
        [
            '#############',
            '#   gsOsosss#'
            '# ###sssssso#',
            '#  o#sssssss#',
            '# ###sOsos###',
            '#  o####### #',
            '##          #',
            '##g######## #',
            '#sssss#     #',
            '#Ossso# o#  #',
            '#sssss#  #  #',
            '#ossOsg o#  #',
            '##########  #',
            '#o          #',
            '######1######'
            ]
    }

    def setup(self):           
        for i in range(4):
            RedApple().init_move(self.maps['main'].random_place(2,6,15,15,FreeSpace))
        for i in range(3):
            GreenPear().init_move(self.maps['main'].random_place(2,2,15,7,FreeSpace))
        for i in range(3):
            Ham().init_move(self.maps['cave'].random_place(2,2,11,11,FreeSpace))
        for i in range(5):
            Crystal().init_move(self.maps['cave'].random_place(2,2,11,11,FreeSpace))
        self.crystals = self.maps['cave'].get_things(Crystal)
#        LongSword().init_move(self.maps['main'].random_place(2,2,15,7,FreeSpace))
#        ChainMail().init_move(self.maps['main'].random_place(2,2,15,7,FreeSpace))
        
    goal_achieved = False
    
    def goal(self,gui,req_help=False):
        if every(lambda x: x.place == self.player, self.crystals) and (not self.goal_achieved or req_help):
            self.goal_achieved = True
            gui.prn('<bf>','Hai trovati tutti i cristalli! Bravo!')
        return self.goal_achieved
    
    phrase_list = Swamp.questions+BigSpider.questions+Ogre.questions                 
