# -*- coding: cp1252 -*-

from gamemap import *
from agents import *
from things import *
from gameinterface import *
import random
from phrase import *
from italian_dungeons import *

class DenseForest(MapItem):
    def can_enter(self,player):
        return False
    cannot_enter_text = 'La foresta é troppo fitto.'
    image = "./img/densewood.gif"

class SparseForest(FreeSpace):
    name=['Una foresta', 'Una foresta','Una foresta con alte alberi', 'Una collina nella foresta',\
                              'Una radura nella foresta', 'Una foresta molto vecchio']
    image = "./img/sparsewood.gif"

class SpiderForest(SparseForest):
    name='Una foresta con grande rangatele'

class ForestPath(FreeSpace):
    image='lightyellow'
    name='Una via'
    
class Shrine(FreeSpace):
    image = "./img/shrine.gif"
    name='Un vecchio e tranquillo santuario nella foresta'
    
class Hill(FreeSpace):
    image = "./img/hill.gif"
    name='Una collinetta con una apertura'
    
class TrapDoorUp(FreeSpace):
    image = "./img/trapdoor-up.gif"

class TrapDoorDown(FreeSpace):
    image = "./img/trapdoor.gif"

class Tunnel(FreeSpace):
    image='lightgrey'

class GroundWall(Wall):
    image='./img/earthwall.gif'
    
class Field(FreeSpace):
    image='lightgreen'
    name='Un campo'

class Floor(FreeSpace):
    image='lightgrey'

class PrisonDoor(LockedDoor):
    code='ogreprison'
    image = "./img/doortiles.gif"
    
Wall.image = "./img/tiles2.gif"
Thing.image = "./img/thing.gif"

class Prisoners(AgentWithMessage):
    name = 'un gruppo di prigionieri'
    greeting_text =  'Vedi un gruppo di gente che i orci hanno caturato.'
    image = "./img/child.gif"
    message_text = 'Uno degli prigionireri dice: ci hai salvato!'
    
class Spider(Enemy):
    name='un ragno'
    hp=6
    strength=4
    move_max=2
    battle_text = 'Il ragno attacca.'
    vulnerable_spirit = False
    questions = [ phrase(['vincere','andare','venire','partire'],
                         subject=[subj_pronoun_phrase(['1s','2s','3sm','3sf','3smn','3sfn','3sp',
                                               '1p','2p','3p','3pmn','3pfn','3pp'])]) ]
    greeting_text =  'Un ragno corre verso te!'
    image="./img/spider.gif"
    sound = './sounds/insect.wav'

class BigSpider(Enemy):
    name='un ragno gigante'
    hp=10
    strength=4
    move_max=2
    battle_text = 'Il ragno gigante attacca.'           
    vulnerable_spirit = False

    questions = [ phrase(['dire','parlare','rispondere','chiedere'],
                         person=['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3pp'],
                         iobj=[indir_pronoun_phrase(['a'],['1s','2s','3sm','3sf','3smn','3sfn','3sp',
                                               '1p','2p','3pmn','3pfn','3pp'])]) ]
    greeting_text =  'Un ragno gigante corre verso te!'
    image="./img/spider.gif" 
    sound = './sounds/insect.wav'

class Centipede(Enemy):
    name='un centopiedo gigante'
    hp=18
    strength=8
    move_max=2
    battle_text = 'Il centopiedo attacca.'
    vulnerable_spirit = False
    questions = [ phrase(['vedersi2','amarsi2'],person=['1p','2p','3p','3pp']),
                  phrase(['vestirsi0','nascondersi0'],person=['1s','2s','3sm','3sf','3sp']*3+\
                                                            ['1p','2p','3p','3pp']) ]
    
    greeting_text =  'Un centopiedo gigante striscia carponi verso te!'
    image = "./img/centipede.gif"
    sound = './sounds/dungbeetle.wav'

class Lance(Weapon):
    strength=3
    name='una lancia'
    image='./img/spear.gif'

class OgreScout(Enemy):
    name='un orco'
    hp=12
    strength=4
    move_max=2
    battle_text = 'Il orco attacca.'
    vulnerable_spirit = False
    weapon=Lance
    questions =  [ phrase(['prendere','aiutare','vedere','portare','cercare','trovare','trarre','muovere'],
                        person=['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3pp'],
                          dobj = [ dir_pronoun_phrase(['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3pp', '4s', '4p']) ])
                 ]
    greeting_text =  'Un orco con una lancia ti vede è attacca instantemente!'
    image = "./img/ogre1.gif"          
    sound = './sounds/warcry.wav'


class Mace(Weapon):
    name='una mazza'
    strength=5
    image='./img/mace.gif'
    
class Ogre1(Enemy):
    name='un orco grande con una mazza'
    hp=15
    strength=5
    move_max=2
    weapon=Mace
    battle_text = "L'orco attacca."           
    vulnerable_spirit = False
    questions = [ phrase(['prendere','dare'],
                         person=['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3pp'],
                        dobj=[ dir_pronoun_phrase(['1s','2s','3sm','3sf','3sp', '1p','2p','3pm','3pf','3pp','4s', '4p']) ],
                        iobj=[ indir_pronoun_phrase(['a'],['1s','2s','3sm','3sf','3sp', '1p','2p','3pm','3pf','3pp']) ]
                        ) ]
                              
    greeting_text = 'Un orco grande con una mazza ti vede è attacca instantemente!'
    image = "./img/ogre2.gif"          
    sound = './sounds/grunt.wav'


class CurvedSword(Weapon):
    name='una spada curva'
    strength=6
    image='./img/sword.gif'

class ChainMail(Armour):
    name='una maglia di ferro'
    strength=3
    image='./img/armour.gif'
    
class Ogre2(Enemy):
    name='un orco grande con una spada curva'
    hp=20
    strength=6
    move_max=1
    weapon=CurvedSword
    armour=ChainMail
    battle_text = 'Il orco attacca.'           
    vulnerable_spirit = False
    questions = [ noun_phrase(['il libro','la borsa','la casa','la macchina','la scarpa',
                                'la tazza', 'il capello','il calzino'],
                              indef=['ciascuno','qualche','ogni','nessuno'],
                              kind=['sd']),
                  noun_phrase(['il libro','la borsa','la casa','la macchina','la scarpa',
                                'la tazza', 'il capello','il calzino'],
                              indef=['poco','tanto','troppo','tutto'],
                              kind=['pd']),
                  noun_phrase(["l'acqua",'il vino'],
                              indef=['poco','tanto','troppo','tutto','nessuno'],
                              kind=['sd']),
                  indef_pronoun_phrase(['qualcuno','nessuno','ognuno','niente','nulla','qualcosa']) ]+\
                2*[ noun_phrase(['il libro','la borsa','la casa','la macchina','la scarpa',
                                'la tazza', 'il capello','il calzino'],
                              demon=['questo','quello','stesso','altro','certo','tale'],
                              kind=['sd','pd'])

                  ]

    greeting_text =  'Un orco grande con una con una spada curva ti vede è attacca instantemente!'
    image = "./img/ogre2.gif"          
    sound = './sounds/grunt.wav'

class PrisonKey(Key):
    name='un chiave'
    code='ogreprison'
    image='./img/key.gif'
    
class Ogre3(Ogre2):
    things=[PrisonKey]
    
class Spirit(Enemy):
    name='una fantasma malevolenza'
    sp=12
    craft=6
    move_max=2
    magic_text= 'la fantasma trova a ti paralizzare.'
    vulnerable_body = False
    questions = [ phrase(['prendere','aiutare','vedere','portare','cercare','trovare','trarre','muovere'],
                      person=['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3pp'],
                          dobj = [ dir_pronoun_phrase(['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3pp'],
                                                    ['solo','anche']),
                                 dir_pronoun_phrase(['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3pp'],
                                                    person2=['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3pp'])
                                 ]),
                  phrase(['andare','fuggire','partire'],
                      person=['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3pp'],
                           iobj=[indir_pronoun_phrase(['da','con'],['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3pp'])])
                  ]
    

    greeting_text = 'Una fantasma malevolenza si avvincia!'
    sound = './sounds/ghost2.wav'
    image = "./img/blackspirit.gif"
    
class Spectre(Enemy):
    name='un spettro'
    sp=20
    craft=8
    move_max=2
    magic_text= 'Il spettro desidera succhiare la tua anima.'
    vulnerable_body = False

    questions = [ noun_phrase(['il libro','la borsa','la casa','la macchina','la scarpa',
                                'la tazza', 'il capello','il calzino'],
                              poss=['1s','2s','3sm','3sf','3sp', '1p','2p','3pm','3pf','3pp'],
                              kind=['sd','pd']) ]

    greeting_text =  'Un spettro con occhie rosse si avvincia nel buio!'
    image = "./img/spectre.gif"
    sound = './sounds/ghost2.wav'

class TalismanWCrystal(MagicThing):
    name='un talismano con un cristallo'
    off=3
    deff=2
    description='Un bello talismano con un cristallo chiaro.'
    opponent_class=(Spectre,Spirit)
    understand=4
    activated_description = 'Questo cristallo ha potenza verso spettri e fantasme'    
    questions = Spectre.questions
    image='./img/necklace.gif'
    
class CommonSword(Weapon):
    name='una spada'
    strength=5

class Hero(Agent):
    name='Eroe'
    hp=20
    strength=5
    sp=20
    craft=4
    weapon = CommonSword
    image="./img/hero.gif"
    visible_on_map=True

class Ham(Food):
    name='un prosciutto'
    hp=4
    sp=4
    image="./img/ham.gif"
    
noun_dict['il libro']='book'
noun_dict['la borsa']='bag'
noun_dict['il soldo']='money'
noun_dict['la casa']='house'
noun_dict['la macchina']='car'
noun_dict['la scarpa']='shoe'
noun_dict['la tazza']='cup'
noun_dict['il capello']='hat'
noun_dict['il calzino']='sock'
noun_dict["l'acqua"]='water'
noun_dict["il vino"]='wine'



class  OgreGame(Game):
    name='Ogre castle'
    learning_goal='Pronouns'
    intro_text='Gli orci hanno imprigionato parecchie persone'
    startx=9
    starty=15
    startmap='main'
    
    pattern_tables ={ \
        'main': {\
        ' ' : Field,
        '.' : ForestPath,
        'o' : (Field,OgreScout),
        'i' : (Field,Spirit),
        'h' : (Shrine,TalismanWCrystal),
        'F' : DenseForest,
        'f' : SparseForest,
        'r' : (SpiderForest,Spider),
        'R' : (SpiderForest,BigSpider),
        'D' : PrisonDoor,
        'd' : (lambda : Floor(name='Fuori una porta solida')),
        'G' : (lambda : PrisonDoor(name='Il grande cancello della fortessa')),
        'g' : (lambda : ForestPath(name='Fuori il grande cancello della fortessa')),
        'a' : (lambda : Floor(name='Dentro il grande cancello della fortessa')),
        'y' : (lambda : Floor(name='Il cortile della fortessa')),
        'Y' : (lambda : Floor(name='Il cortile della fortessa'), Ogre1),
        't' : (lambda : Floor(name='Dentro un torre')),
        'T' : (lambda : Floor(name='Dentro un torre'), Ogre2),
        'h' : (lambda : Floor(name='Dentro un torre'),Ham),
        'p' : (lambda : Floor(name='Nella porta di un torre')),
        'u' : (lambda : Floor(name='Un casa nella fortessa')),
        'U' : (lambda : Floor(name='Un casa nella fortessa'), Ogre3),
        's' : (lambda : Floor(name='Dentro un torre'), Prisoners),
        '1' : (lambda : TrapDoorDown(name='Dentro un torre, con una botola'),\
               lambda : GateWay('trapdoor1','[en]ntri','under') ),
        '2' : (lambda : TrapDoorDown(name='Dentro un torre, con una botola'),\
               lambda: GateWay('trapdoor2','[en]ntri','under') ),
        '3' : (lambda : Hill(name='Una collinetta con una apertura'),\
                lambda : GateWay('mound1','[en]ntri','under') ),
        '4' : (lambda : Hill(name='Una collinetta con una apertura'),\
                lambda: GateWay('mound2','[en]ntri','under') )
        },
    
        'under':{ \
        ' ' : (lambda : GroundWall()),
        'p' : (lambda : Tunnel(name='Un passaggio molto buio')),
        'P' : (lambda : Tunnel(name='Un passaggio molto buio'),Spectre),
        't' : (lambda : Tunnel(name='Un passaggio molto stretto')),
        'T' : (lambda : Tunnel(name='Un passaggio molto stretto'),Centipede),
        's' : (lambda : Floor(name='Una sala sotterranea')),
        'S' : (lambda : Floor(name='Una sala sotterranea'),Ogre2),
        'h' : (lambda : Floor(name='Una sala sotterranea con proviste'),Ham),
        '1' : (lambda : TrapDoorUp(name='Sotto una botola'),\
                lambda : GateWay('trapdoor1','[es]ci','main') ),
        '2' : (lambda : TrapDoorUp(name='Sotto una botola'),\
                lambda : GateWay('trapdoor2','[es]ci','main') ),
        '3' : (lambda : Floor(name='La uscita del sepulcro'),\
                lambda: GateWay('mound1','[es]ci','main') ),
        '4' : (lambda : Floor(name='La uscita del sepulcro'),\
                lambda : GateWay('mound2','[es]ci','main') )
        }
    }

    map_patterns = {
        'main': 
        ['FFFF f  hFFFFFFFFF',
        'Ffif3R ffRFF ffffff',
        'Ffo iffrfi ffif4iRf',
        'FR           o    f',
        'Ff ######  ######  ',
        'f  #sDdt####htth# o',
        'f  #t#Tt#Uu#1tTt#  ',
        'fo ###p##Yy##p###  ',
        'f   #yYyyyyyyYy#  f',
        'fr  #yyyyYyyyyy# rf',
        'fo ###p##yy###p## o',
        'fo #sDt2#aY#t#Tt# f',
        'f  #t#Tt#G##sDdT#  ',
        '   ######g ###### f',
        'ffo      .    o    ',
        'ff ff    . ffffffff'],

        'under':
        ['                   ',
        '    3              ',
        '    p    ppp   4   ',
        '  ppPtTttp pPppp   ',
        '         P   t     ',
        '  pppppPppT  t     ',
        ' Pp                ',
        '  pP tttT## 1##    ',
        '   ttT #ss# hs#    ',
        '   t##pSspppp##    ',
        '    #Ss#sh         ',
        '    ##p2#          ',
        '    #ss#           ',
        '    #sh#           ',
        '    ####           ',
        '                   ',
        '                   ',
        '                   ']
    }

    def setup(self):
        self.prison_doors = self.maps['main'].get_places(PrisonDoor)
        self.mission_accomplished = False
        
    def goal(self,gui,requested_help=False):
        if every(lambda x: not x.locked, self.prison_doors):
            if not self.mission_accomplished:
                gui.prn('<bf>','I prigonieri ora possono fugire!')
                self.mission_accomplished=True
        return self.mission_accomplished
    
    phrase_list= Spider.questions+BigSpider.questions+OgreScout.questions+Ogre1.questions+\
                 Ogre2.questions+Spectre.questions+Spirit.questions

    pronouns_used = True
    
