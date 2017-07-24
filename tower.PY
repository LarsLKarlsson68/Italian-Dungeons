# -*- coding: cp1252 -*-
from italian_dungeons import *
from gamemap import *
from agents import *
from things import *
import random
from phrase import *
import space_time
from gameinterface import *


class Floor(FreeSpace):
    image='lightgrey'

LockedDoor.image = "./img/doortiles.gif"
    
Wall.image = "./img/tiles2.gif"
Thing.image = "./img/thing.gif"

class TrapDoorUp(FreeSpace):
    image = "./img/trapdoor-up.gif"

class TrapDoorDown(FreeSpace):
    image = "./img/trapdoor.gif"


class Lance(Weapon):
    name = 'una lancia'
    strength=4
    image='./img/spear.gif'
    
class Faun(Enemy):
    name='un fauno'
    hp=10
    strength=3
    move_max=2
    weapon=Lance
    battle_text = 'Il fauno attacca.'           
    vulnerable_spirit = False
    questions = \
              1*[ prep_phrase(['di(2)'],['Roma','Milano','Italia','Sicilia']),
                  prep_phrase(['da(3)'],['Paolo(1)','Maria(1)']),
                  prep_phrase(['da(4)'],['Paolo','Maria']),
                  prep_phrase(['a(2)'],['Capri','Roma','Milano'],kind=['s'])
                ]+\
              2*[  prep_phrase(['in(0)'],['la casa','il cielo',"l'acqua",'la città','la campagna',"l'isola",
                             'lo spazio','il fiume',"l'aria",'il mare',"l'isola",'il paese', "l'incrocio",
                                          'Italia','Sicilia']),
                 prep_phrase(['in(1)','da'],['la città','la campagna','la stanza','la chiesa',"l'ufficio"]),
                 prep_phrase(['a(0)','a(1)','da'],['il mare','il cinema',"l'ospitale(m)"]),
                 prep_phrase(['su'],['il mare','la strada','la montagna','il fiume','la collina',
                                    'il pianeta(m)',  'la frontiera', 'la sopra', 'il fondo',
                                    "l'esterno", 'la via', 'la terra', 'il suolo', 'la pianura', 'la spiagga',
                                    'la costa', 'il ponte']),
                 prep_phrase(['tra','fra','intorno_a'],
                             ['il lago',"l'isola",'la montagna','la stella','la città'],
                             kind = ['pd'])            
            ] 

                
    image='./img/faun.gif'
    sound='./sounds/goat.wav'
    greeting_text='Un fauno con una lancia ula!'

class LongAxe(Weapon):
    name='una scure lunga'
    strength=5
    image='./img/axe.gif'

class BronzeArmour(Armour):
    name='una corazza di bronzo'
    strength=2
    image='./img/armour.gif'

class Faun2(Faun):
    name='un fauno furioso'
    hp=12
    strenght=4
    move_max=4
    weapon=LongAxe
    armour= BronzeArmour
    battle_text = 'Il fauno attacca.'           

    greeting_text='Un fauno furioso grida e brande una scure lunga!'

class Mace(Weapon):
    name='una mazza'
    strength=5
    image='./img/mace.gif'
 
class Minotaur(Enemy):
    name='un minotoro'
    hp=20
    strength=6
    move_max=2
    weapon=Mace
    battle_text = 'Il minotoro attacca.'           
    vulnerable_spirit = False
    questions = \
              [  phrase(['andare'],adverb2=['fuori','dentro','a sinistra','a destra','su',
     'giù','soprosotta', 'in mezzo','dietro','vicino','lontano','avanti','indietro','da qualche parte','dappertutto','in ogni luogo',
     'da qualsiasi parte', 'altrove', 'dovunque', 
     'da nessuna parte', 'qui', 'qua','lì', 'là','in macchina', 'in auto', 'in treno',
     'in autobus', 'in barca', 'in bicicletta',  'in barca', 'a piedi', 'a cavallo','rapido',
     'svelto', 'veloce', 'lento'],
                   person=['3sm'])]
                
    greeting_text = 'Un minotoro si avvicina!'
    image='./img/minotaur.gif'
    sound='./sounds/bull.wav'
    
class Gorgon(Enemy):
    name='una gorgona'
    hp=12
    strength=4
    sp=12
    craft=6
    move_max=4

    magic_text = 'La gorgona è terribile di vedere.'           
    questions = \
              [  noun_phrase(["l'esterno","l'interno",'la lungezza',"l'altezza",
                              'la largezza','i dimensioni','il posto','il luogo',"l'angelo"],
                             post=[prep_phrase(['di'],['la casa','la chiesa'])]),
                 noun_phrase(['la profondità', 'il fondo', 'la superfice','la largezza','i dimensioni',
                              'il mezzo'], 
                             post=[prep_phrase(['di'],['il lago','il mare','il fiume',"l'acqua"],
                                               adj2=['largo','stretto','profondo','poco profondo',False,False] )]),
                 noun_phrase(["l'altezza",'il lato','la sopra','la parte','il luogo'],
                              post=[prep_phrase(['di'],['la montagna','la collina'],
                                                adj2=['vicino','lontano','alto','basso',
                                                      'grande','piccolo',False,False])])]
                                         
                             
    greeting_text= 'Una gorgona ti vede!'
    image='./img/gorgon.gif'
    sound='./sounds/snakehiss.wav'

class Harpy(Enemy):
    name="un'arpia"
    hp=18
    strength=6
    sp=12
    craft=1
    move_max=4

    magic_text = "L'arpia vola verso te."           
    questions = \
              [ prep_phrase(['attraverso(1)','lungo'],
                            ['la via', 'la strada', 'il passagio', 'il sentiero', 'il fiume', 'la spiagga',
                             'il margine', "l'orlo", 'la frontiera'], \
                             adj2=[False,False,'lungo','corto', 'largo','stretto','vicino','lontano'],
                            kind=['sd','si','pd']) ]+\
            3*[prep_phrase(['davanti_a','dietro','vicino_a','sopra','sotto','accanto_a','verso','da'],
                            ['il pianeta(m)','la stella','la luna','il ponte', 'la casa','la montagna','la collina',
                             'il luogo','il posto' ],kind=['sd','si','pd']),
               prep_phrase(['attraverso(0)','attraverso(1)','oltre','intorno_a','dentro','fuori_di','da','verso'],
                            ['il lago', 'il mare', "l'area", 'la zona', 'il paese', 'la prateria', 'il deserto',
                             'la foresta', 'la pianura', 'la valle', "l'isola", 'il fiume' ],
                            kind=['sd','si','pd'])
               ]
    greeting_text= "Un'arpia mastica un vecchio osso!"
    image='./img/harpy.gif'
    sound='./sounds/eagle.wav'
    
class Cyclop(Enemy):
    name='un ciclopo'
    hp=20
    strength=8
    move_max=2
    weapon=Mace

    battle_text = 'Il ciclopo attacca.'           
    vulnerable_spirit = False
    questions = \
              [ phrase(['volare','decollare','atterrare','rotolare'],person=['3sm','3sf','3p']),
                phrase(['nuotare','tuffarsi0','galleggiare','affondare','navigare','cadere'],
                       person=['3sm','3sf','3p'],
                       post=[prep_phrase(['in'],['il lago','il mare','il fiume'])]*2+\
                           ['qui', 'qua','lì', 'là']),
                phrase(['salire','scendere','avvicinarsi0','passare'],
                       person=['3sm','3sf','3p'],
                       dobj=['la montagna','la collina']),
                phrase(['cavalcare','guidare','viaggare','strisciare',
                        'camminare','correre'],
                       person=['3sm','3sf','3p'],
                       post=[prep_phrase(['in','in','da'],
                                         ['la valle', 'la pianura','la foresta',
                                          'la terra','il deserto','la prateria',
                                          'la campagna', 'la piazza'])]),
                
                phrase(['attraversare','passare','esplorare'], person=['3sm','3sf','3p'],
                       dobj=['la valle','la prateria','la foresta','la piazza'])
             ]
                       
    greeting_text = 'Un grande ciclopo si avvincina!'
    image='./img/cyclops.gif'
    sound='./sounds/monster1.wav'


class Siren(Enemy):
    name='una sirena'
    hp=10
    strength=4
    sp=10
    craft=8
    move_max=4

    magic_text = 'La sirena canta.'           
    questions = Faun.questions+Minotaur.questions+Gorgon.questions+Cyclop.questions+Harpy.questions                                               
    greeting_text = 'Una sirena arriva!'
    image='./img/siren.gif'
    sound='./sounds/womansing.wav'


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
    
class Mirror(MagicThing):
    name='un specchio'
    off=3
    deff=2
    opponent_class=Gorgon
    understand=8
    activated_description = 'Il specchio ha potenza verso gorgone.'
    questions = Gorgon.questions
    image='./img/mirror.gif'

class Flute(MagicThing):
    name='un flauto'
    off=2
    deff=2
    opponent_class=Siren
    understand=8
    activated_description = 'Il flauto ha potenza verso sirene.'
    questions = Siren.questions
    
class IronKey(Key):
    name='un chiave di ferro'
    code='a'
class BronzeKey(Key):
    name='un chiave di bronzo'
    code='b'
class SilverKey(Key):
    name="un chiave d'argento"
    code='c'
class GoldKey(Key):
    name="un chiave d'oro"
    code='d'
Key.image='./img/key.gif'

class Skull(Thing):
    name='un cranio'
    image='./img/skull.gif'
class Bone(Thing):
    name='un osso'
    image='./img/bone.gif'
    
class CommonSword(Weapon):
    name='una spada'
    strength=5
    image='./img/sword.gif'

class Hero(Agent):
    name='Eroe'
    hp=20
    strength=5
    sp=20
    craft=4
    visible_on_map = True
    weapon = CommonSword
    image="./img/hero.gif"

class Treasure(Thing):
    name='il tesoro'
    image='./img/treasure.gif'

class TowerGame(Game):
    name='The tower'
    learning_goal = 'Prepositions, places'
    intro_text='Puoi prendere il tesoro nella torre?'
    startx=0
    starty=4
    startmap='level1'
    pattern_tables ={ \
        'level1': { \
        ' ' : (lambda : Floor(name='Un passagio')),
        'S' : (lambda : Floor(name='Una sala')),
        'f' : (lambda : Floor(name='Un passagio'),Faun),
        'F': (lambda : Floor(name='Una sala'),Faun2),
        'c' : (lambda : Floor(name='Un passagio'),Cyclop),
        'd': (lambda: LockedDoor(name='Una porta',code='a')),     
        '1' : (lambda : TrapDoorUp(name='Una scala che va su'),
               lambda : GateWay('stairs1','[su]lla scala','level2')),
          },
        'level2': { \
        ' ' : (lambda : Floor(name='Un passagio')),
        'S' : (lambda : Floor(name='Una sala')),
        'm' : (lambda : Floor(name='Un passagio'),Minotaur),
        'c' : (lambda : Floor(name='Un passagio'),Cyclop),
        'M': (lambda : Floor(name='Una sala'), Gorgon),
        'h' : (lambda : Floor(name='Un passagio'),Harpy),
        'd': (lambda: LockedDoor(name='Una porta',code='b')),
        '1' : (lambda : TrapDoorDown(name='Una scala che va giù'),
                lambda : GateWay('stairs1','[g]iù la scala','level1') ),
        '2' : (lambda : TrapDoorUp(name='Una scala che va su'),
                lambda : GateWay('stairs2','[su]lla scala','level3') ),
        },
        'level3': { \
        ' ' : (lambda : Floor(name='Un passagio')),
        'S' : (lambda : Floor(name='Una sala')),
        'm' : (lambda : Floor(name='Un passagio'),Siren),
        'h' : (lambda : Floor(name='Un passagio'),Harpy),
        '2' : (lambda : TrapDoorDown(name='Una scala che va giù'),
                lambda : GateWay('stairs2','[g]iù la scala','level2') ),
        'd': (lambda: LockedDoor(name='Una porta',code='c')),
        'e': (lambda: LockedDoor(name='Una porta',code='d')),
        'T': (lambda : Floor(name='Un passagio'), Treasure)
        }
    }
    
    map_patterns = {\
        'level1':
        [
        '###########',
        '#f   cSSFS#',
        '# # # #SSS#',
        '##### ### #',
        '    f     #',
        '##### ## ##',
        '#FS1# #FSS#',
        '#d### ### #',
        '#  f      #',
        '###########' ],
        'level2':
        [
        '#########',
        '#m SSm#2#',
        '# #SM##d#',
        '#Sh#  mc#',
        '#c#######',
        '#SS1## h#',
        '#MSS m  #',
        '#########' ],
        'level3':
        [
        '##########',
        '# e  dm#2#',
        '#m# m# # #',
        '#SS# # h #',
        '#ST# # # #',
        '##########' ]
    }

    def setup(self):
        IronKey().init_move(self.maps['level1'].random_place(1,1,9,3,Floor))
        for i in range(4):
            RedApple().init_move(self.maps['level1'].random_place(1,1,9,8,Floor))
        Mirror().init_move(self.maps['level1'].random_place(1,1,9,8,Floor))
        Skull().init_move(self.maps['level1'].random_place(1,1,9,8,Floor))
        Bone().init_move(self.maps['level1'].random_place(1,1,9,8,Floor))

        BronzeKey().init_move(self.maps['level2'].random_place(1,3,7,6,Floor))
        for i in range(3):
            GreenPear().init_move(self.maps['level2'].random_place(1,1,7,6,Floor))
        Bone().init_move(self.maps['level2'].random_place(1,1,7,6,Floor))
        Skull().init_move(self.maps['level2'].random_place(1,1,7,6,Floor))
        Flute().init_move(self.maps['level2'].random_place(1,1,7,6,Floor))

        SilverKey().init_move(self.maps['level3'].random_place(6,2,8,4,Floor))
        GoldKey().init_move(self.maps['level3'].random_place(3,2,8,4,Floor))
        for i in range(3):
            Skull().init_move(self.maps['level3'].random_place(1,1,8,4,Floor))

    goal_achieved = False
    
    def goal(self,gui,req_help=False):
        if self.player.get_things(Treasure) and (not self.goal_achieved or req_help):
            self.goal_achieved = True
            gui.prn('<bf>','Hai preso il tesoro! Bravo!')
        return self.goal_achieved

    phrase_list = Faun.questions+Minotaur.questions+Gorgon.questions+Cyclop.questions+Harpy.questions 
                           
    

    
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

    
class Field(FreeSpace):
    image='./img/grass.gif'
    name='Un campo'
    

    
class Faun3(Faun):
    questions = \
              [ noun_phrase(['il giorno','la notte','la sera','la mattina',"l'ora",
                              'il minuto','la settimana','il mese','la stagione',
                              "l'estate(f)", "l'autumno", "l'inverno",'la primavera',
                              "l'anno",'il secolo','il tempo','la data'],
                             adj1=['primo','secondo','ultimo','passato',False,False,
                                   'presente','futuro','precedente','prossimo'],
                             kind=['sd'])]+\
                 2*[phrase(['partire','arrivare','morire','nascere'],tempus=['present'],
                        person = ['3sm','3sf','3p'],
                        post=[prep_phrase(['in'],['la primavera', "l'inverno", "l'autumno","l'estate(f)"],kind=['s']),
                             prep_phrase(['a(1)'],['il mezzogiorno','la mezzanotte'],kind=['s']),
                              prep_phrase(['tra(2)'], ['il mese','il giorno',"l'ora",'la settimana'],
                                          count=[1,2,3],kind=['pi'])])]+\
                 [phrase(['finire','fare'],tempus=['perfect'],
                        person = ['3sm','3sf','3p'],
                        post=2*[prep_phrase(['da(5)','per','in'],['il mese','il giorno',"l'ora",'la settimana'],
                                          count=[1,2,3],kind=['pi'])] +\
                              [noun_phrase(['il mese','il giorno',"l'ora",'la settimana'],count=[1,2,3],kind=['pi'],
                                      post=['fa'])] ) ]
                
                  
class Faun4(Faun2):
    questions=Faun3.questions
                  


class Minotaur2(Minotaur):
    questions = \
              [  phrase(['andare','aspettare','fermare','cominciare','finire','riposarsi0','dormire','svegliarsi0',
                         'addormentarsi0'],
                        person = ['3sm','3sf','3p'],
                        adverb1=['sempre','non mai','qualche volta', 'spesso',
                                 'raramente','ancora(0)',
                                 'ancora(1)','non ancora','già',
                                 'presto(0)', 'fra poco','appena','di solito',
                                 'finalmente']),
                 phrase(['andare','aspettare','fermare','cominciare','finire','riposarsi0','dormire','svegliarsi0',
                         'addormentarsi0'],
                        person = ['3sm','3sf','3p'],
                        adverb2=['una volta','due volte','ancora(1)',
                                 'non piu', 'ora', 'tardi', 'per ultimo', 'per sempre',
                                 'stanotte', 'stasera', 'stamattina', 'allo stesso tempo',
                                 'adesso', 'presto(1)', 'prima', 'dopo',
                                 'finalmente','oggi'])
                 ]
                  

class SacredCrystal(Thing):
    image='./img/crystal.gif'
    name='un cristallo sacro'

class Temple(FreeSpace):
    image='./img/temple.gif'
    name='Un tempio'
    description='Il tempio é rubato. I cristalli sacri sono persi.'
    
class Swamp(KeepingTrap):
    name='una palude'
    image = './img/swamp.gif'
    intro_text = 'Entri una palude traditore'
    disarmed_text = 'Trovi una via attraverso la palude'
    effect_text = 'Ti impigli nella palluda'
    strength= 3
    craft = 1
    questions=Minotaur2.questions+Faun3.questions
    
class ForestGame(Game):
    name='The minotaur forest'
    learning_goal = 'Prepositions, time'
    intro_text='I quattro cristalli del tempio sono persi!'
    startx=0
    starty=2
    pattern_tables ={ \
        'main': {\
        ' ' : Field,
        '.' : ForestPath,
        '3' : (Field,Faun3),
        '4' : (Field,Faun4),
        'c' : (Hill),
        'h' : (Shrine,Minotaur2,SacredCrystal),
        'F' : DenseForest,
        'f' : SparseForest,
        's': Swamp,
        'A' :Temple
        }
    }
    map_patterns = {
        'main':
        [
        'FFFFFFFFFFFFFFFFFFFFFFF',
        'Fffff ss4fff 4FFF4 f sF',
        '.....3scsFFhFF...FFFh F',
        'FfAf...cffFFF..c.sFF fF',
        'Ff fcf..ff....cc.......',
        'Fffcff4....ff....cff4ff',
        'Ff3ff  .c sssssFFFFFfff',
        'Ff hc  sssss4f FFhFFfff',
        'Ffff  3fFFFFFss4F Fs ff',
        'Fccff  sss  f f    s ff',
        'FFFFFFFFFFFFFFFFFFFFFFF' ]
    }

    def setup(self):           
        for i in range(4):
            RedApple().init_move(self.maps['main'].random_place(1,1,23,11,FreeSpace))
        self.crystals = self.maps['main'].get_things(SacredCrystal)
        self.temple = self.maps['main'].get_places(Temple)
    goal_achieved = False
    
    def goal(self,gui,req_help=False):
        if every(lambda x: x.place in self.temple, self.crystals) and (not self.goal_achieved or req_help):
            self.goal_achieved = True
            gui.prn('<bf>','Hai tornato i quattro cristalli! Bravo!')
        return self.goal_achieved
    
    phrase_list = Minotaur2.questions+Faun3.questions                  
