# -*- coding: latin_1 -*-
# Scenario with vampires


from verb import *
from gamemap import *
from agents import *
from things import *
from phrase import *
from italian_dungeons import *


vampire_tempus = ['imperative','present','present','imperfect','conditional','future','future','perfect','pluskvamperfect']

irreg_verbs = ['dare','fare','stare','andare','vedere','venire','dire','porre','bere','trarre','uscire','morire','sedere',
               'piacere','tenere']

obj_verbs1 = ['toccare',  'aprire',  'accendere', 'trarre',   'coprire', 'trovare',  'prendere', 'cadere',
 'chiudere',  'costare', 'stringere',  'tirare',  'scoprire',   'finire',  'levare', 'portare',
   'spingere',  'vincere', 'spegnere', 'tenere', 'bere', 'comprare', 'vendere',   'cambiare', 
  'lasciare',  'lavorare', 'usare',  'fare', 'dare', 'mangiare',  
   'vestire', 'pagare',  'porre', 'mettere', 'succedere',  'cominciare']


agent_verbs1 = ['conoscere', 'rispondere', 'amare', 'dimenticare', 'capire', 'piangere', 'decidere', 'scrivere','pensare',
 'leggere', 'chiedere', 'chiamare', 'dire', 'credere', 'permettere', 'incontrare',
 'proporre', 'vietare', 'preferire', 'imparare', 'ridere',  'giacere', 'morire', 'nascere', 'dormire',
 'ricordare', 'vedere', 'vivere', 'insegnare', 'aiutare', 'suporre', 'odiare', 
'piacere', 'parlare', 'udire', 'servire', 'sentire', 'provare', 'fallire' ] 

move_verbs1 =[  'stare','riuscire', 'cercare', 'nascondere', 'spedire', 'venire',  'ricevere', 'perdere',
   'entrare', 'partire', 'girare', 'correre', 'arrivare', 'fermare', 'tornare', 'muovere', 
   'diventare', 'seguire',  'condurre', 'fuggire', 'uscire', 'aspettare', 'inseguire', 'andare',
    'camminare', 'sedere' ]

all_verbs = obj_verbs1+agent_verbs1+move_verbs1

def multiply_difficult_verbs(verb_list):
    new_verb_list = []
    for v in verb_list:
        if 'ref' in verbs[v]:
            v2 = verbs[v]['ref']
        else:
            v2 = v
        count=1
        if 'present' in verbs[v2]:
            count += 1
        if 'perfect' in verbs[v2]:
            count += 1
        new_verb_list += count*[v]
    return new_verb_list
            
obj_verbs = multiply_difficult_verbs(obj_verbs1)
move_verbs = multiply_difficult_verbs(move_verbs1)
agent_verbs = multiply_difficult_verbs(agent_verbs1)

class House(FreeSpace):
    image="./img/house.gif"

class Vampire(Enemy):
    name= 'un vampiro'
    hp=16
    strength=8
    sp=16
    craft=5
    move_max=3
    forbidden_places=House

    battle_text= [ 'Il vampiro sibila!',
                   'Il vampiro é putrido!', 
                    'Il vampiro puzza come nella tomba!',
                    'Questro mostro della notte desidere sangue.']
    
    greeting_text = 'Un vampiro attacca!'
    image="./img/vampire.gif"
    sound = './sounds/snakehiss.wav'
    questions = phrase(agent_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])
                       
class VampireDemon(Vampire):
    name='un vampiro demonico'
    hp=24
    strength=8
    sp=24
    craft=10
    move_max=3
    image="./img/vampiredemon.gif"
    greeting_text = 'Un vampiro demonico attacca!'
    questions = phrase(irreg_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])

class Spectre(Enemy):
    name='un spettro'
    sp=14
    craft=6
    move_max=2
    magic_text= 'Il spettro desidera succhiare la tua anima.'
    vulnerable_body = False
    greeting_text = 'Un spettro con occhie rosse si avvincia!'
    image="./img/spectre.gif"
    sound = './sounds/ghost2.wav'
    questions = phrase(move_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])

class Gorgoco(Enemy):
    name='Gorgoco'
    sp=40
    craft=12
    hp=10
    move_max=2
    battle_text= 'Gorogoco chiama il dio del morte.'
    vulnerable_body = False
    greeting_text = 'Hai trovato Gorocogo, il mago cattivo!\nGorgoco dice: Anche tu diventicerai il mio schiavo. Ma prima, muori!\n'
    image="./img/wizard.gif"
    sound = './sounds/evillaugh.wav'
    questions = phrase(all_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])
        
class Bat(Enemy):
    name='un pipistrello grosso'
    hp=8
    strength=4
    move_max=2
    forbidden_places=House
    battle_text = 'Il pipistrello si lancia in picchiata.'           
    vulnerable_spirit = False
    greeting_text =  'Un pipistrello nero vola verso te!'        
    image="./img/bat.gif"
    sound = './sounds/bats.wav'
    questions = phrase(all_verbs,tempus=['infinitive'],
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])

class Bat1(Bat):
    questions = phrase(agent_verbs1,tempus=['infinitive'],
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])

class Bat2(Bat):
    questions = phrase(obj_verbs1,tempus=['infinitive'],
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])

class Bat3(Bat):
    questions = phrase(move_verbs1,tempus=['infinitive'],
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])
    
class Wolf(Enemy):
    name='un lupo'
    hp=10
    strength=6
    move_max=2
    forbidden_places=House
    battle_text = 'Il lupo attacca.'           
    vulnerable_spirit = False
    greeting_text =  'Un lupo ti sale!'
    image="./img/wolf.gif"
    sound = './sounds/wolf.wav'
    questions = phrase(obj_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])

class GhostHound(Enemy):
    name='un cane spettrale'
    sp=15
    craft=4
    move_max=2
    forbidden_places=House
    magic_text= 'Il cane spettrale propaga pazzia.'
    vulnerable_body = False
    greeting_text = 'Un cane spettro con una bocca rossa si avvincia!'
    image="./img/ghostdog.gif"
    sound = './sounds/doggrowl.wav'
    questions = phrase(obj_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])

class InnKeeper(AgentWithMessage):
    name='il ospite della locanda'
    greeting_text = "L'ospite della locanda é un vecchio uomo."
    message_text =  'Il ospite bisbiglia: Fa attenzione! Orribile creature vanno al buio.\n Vengono dal cimetero!'
    image="./img/child.gif"
    
class WorriedPeasant(AgentWithMessage):
    name='un contadino'
    greeting_text = 'Vedi un povero contadino.'
    message_text = 'Il contadino dice: I morti non stanno nelle tombe più.'
    image="./img/child.gif"

class ChildInWoods(AgentWithMessage):
    name='una bambina'
    greeting_text = 'Vedi una bambina con un chestino.'
                   
    message_text = 'La bambina dice: Racoglio erbe nella foresta che protteggano contro i demoni. '+\
        'Anche le animali della foresta sono preoccupato. Mi aiutano.'
    image="./img/child.gif"
        
class GhostOfBidaro(AgentWithMessage):
    name='il spettro di Bidaro'
    greeting_text ='Vedi un spettro che sembra un vecchio uomo in un abito.'
    image="./img/ghost1.gif"
    
    def talk_with(self,player,gui):
        gui.prn('Il spettro parla a voce bassa:')
        gui.pr('Io ero Bidaro, un mago. Una volta avevo una apprendista, Gorgoco, che era molto potente.')
        gui.pr('Ma anche diventicava molto corrotto. Gorgoco é nell vecchio tempio al nord.')
        gui.pr('Crea un esercito degli demoni. Devi uccidere Gorgoco con un coltello.')
        gui.prn('Lo trovi nella mia tomba.')

class KnifeOfBidaro(MagicWeapon):
    name='il coltello di Bidaro'
    description='Un bello coltello'
    strength=3
    off=1
    deff=2
    opponent_class=Gorgoco
    special_strength=8
    understand=8
    activated_description = "Il coltello ha un maledizione verso Gorgoco."
    questions = phrase(irreg_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])


class VampireTalisman(MagicThing):
    name='un talismano con una pietra nera'
    off=3
    deff=2
    opponent_class=Vampire
    understand=4
    activated_description = 'Questo talismano ha potenza verso vampiri.'
    questions = phrase(irreg_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])
    image="./img/necklace.gif"

class Owl(ReluctantAgentWithGift,WaryReluctantAgent):
    name='un gufo'
    move_max=3
    things=[VampireTalisman]
    greeting_text = 'Vedi un gufo. Piaci il gufo?'
    success_text = 'Il gufo ti da un talismano, e vola via.'
    failure_text = 'Il gufo in silenza vola nella foresta.'
    questions = phrase(agent_verbs,tempus=vampire_tempus, 
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])
    image="./img/owl.gif"
    

class Chrystal(MagicThing):
    name='un cristallo'
    off=3
    deff=2
    opponent_class=(Spectre,GhostHound)
    understand=4
    activated_description = 'Questo cristallo ha potenza verso spettri (anche cani)'
    questions = phrase(irreg_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])
    image="./img/crystal.gif"

class Apple(Food):
    name='una mela'
    hp=3
    sp=3
    image="./img/apple.gif"
    
class Fox(ReluctantAgentWithGift,WaryReluctantAgent):
    name='un volpe'
    move_max=3
    things=[Apple]
    greeting_text = 'Vedi un volpe. Piaci il volpe?'
    success_text = 'Il volpe ti da una mela, e va via.'
    failure_text = 'Il volpe in silenza parte nella foresta.'
    questions = phrase(agent_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])
    image="./img/fox.gif"

class CommonSword(Weapon):
    name='una spada'
    strength=5
    image="./img/sword.gif"

class Hero(Agent):
    name='Eroe'
    hp=20
    strength=5
    sp=20
    craft=4
    weapon = CommonSword
    image="./img/hero.gif"
    visible_on_map = True


class Blueberries(Food):
    name='mirtilli'
    hp=4
    image="./img/berries.gif"

class Whiteflowers(Food):
    name='un fiore bianco'
    hp=2
    sp=4
    image="./img/berries.gif"
    

class DenseForest(MapItem):
    def can_enter(self,agent):
        return False
    cannot_enter_text = 'La foresta é troppo fitto.'
    image="./img/densewood.gif"
    
class Cliff(MapItem):
    def can_enter(self,agent):
        return False
    cannot_enter_text = 'Questi rupi non puoi scalare.'
    image="./img/cliff.gif"
    
class SparseForest(FreeSpace):
    name = ['Una foresta', 'Una foresta','Una foresta con alte alberi', 'Una collina nella foresta',\
                   'Una radura nella foresta', 'Una foresta molto vecchio']
    image="./img/sparsewood.gif"

                       
class ForestPath(FreeSpace):
    image = 'yellow'
    name='Una via'
    
class AbandonedHouse(House):
    name='Una casa abbandonata'

class PeasantHouse(House):
    name='Una casa'
    agents=[WorriedPeasant]
    
class GuestHouse(House):
    name='Una locanda'
    agents=[InnKeeper]
    
class GraveYard(FreeSpace):
    image="./img/grave.gif"
    name = 'un cimitero'
    
class Tomb(FreeSpace):
    image="./img/tomb.gif"
    name='una vecchia tomba'
    
class Altar(FreeSpace):
    image="./img/altar.gif"
    name = 'Un altare macchiato di sangue'

class Grass(FreeSpace):
    image='olivedrab1'
    name=['Un prato con i fiori','Un campo']
    
class TombFloor(FreeSpace):
    image='grey30'
    name = 'una tomba'

class TombFloorExit(TombFloor):
    name='La uscita della tomba'

class TempleFloor(FreeSpace):
    name = 'Interno il tempio'    
    image='grey30'

class TempleEntrance(FreeSpace):
    name = 'La porta del tempio'    
    image='./img/gatetiles-open.gif'

class ThornBushes(KeepingTrap):
    name='Cespugli'
    intro_text = "Questi cespugli hanno lunghi spini."
    strength=2
    effect_text = "Gli spini ti fa male."
    questions = phrase(obj_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','1p','1p','2p','2p','3pm','3pf'])
    image="./img/thorn.gif"

Wall.image='./img/tiles2.gif'

class VampireGame(Game):
    name='Vampires'
    learning_goal='Mostly irregular verbs (andare, prendere ,dire,...)'
    intro_text='Qualcosa è male nell viaggio.'
    
    startx = 7
    starty = 14
    startmap = 'main'
    
    pattern_tables= { \
        'main': {
		' ' : Grass,
		'F' : DenseForest,
		'f' : SparseForest,
		'a' : (Grass,)+4*(Whiteflowers,),
		'C' : Cliff,
		't' : ThornBushes,
		'c' : GraveYard,
		's' : (GraveYard,Spectre),  
		'v' : (SparseForest,Vampire),
		'b' : (SparseForest,Bat),
		'w' : (SparseForest,Wolf),
		'h' : (SparseForest,GhostHound),
		'o' : (SparseForest,Owl),
		'x' : (SparseForest,Fox),
		'm' : (SparseForest,Blueberries),
		'.' : ForestPath,
		'S' : (ForestPath,Spectre),
		'P' : PeasantHouse,
		'I' : GuestHouse,
		'A' : AbandonedHouse,
		'i' : (SparseForest,ChildInWoods),        
		'B' : (GraveYard,GhostOfBidaro),
		'1' : (Tomb, lambda : GateWay('tomb_1','[en]ntri','tomb_1') ),
		'2' : (Tomb, lambda : GateWay('tomb_2','[en]ntri','tomb_2') ),
		'3' : (Tomb, lambda : GateWay('tomb_3','[en]ntri','tomb_3') ),
		'4' : (TempleEntrance,
                       lambda : GateWay('temple','[en]ntri','temple') )
	   },
        'tomb' : {\
		' ' : TombFloor,
		's' : (TombFloor,Spectre),
		'b' : (TombFloor,GhostHound),
		'1' : (TombFloorExit, lambda : GateWay('tomb_1','[es]ci','main') ),
		'2' : (TombFloorExit, lambda : GateWay('tomb_2','[es]ci','main') ),
		'3' : (TombFloorExit, lambda : GateWay('tomb_3','[es]ci','main') ),
		'B' : (lambda : TombFloor(name='Al sarcofago di Bidaro'), KnifeOfBidaro),
		'c' : (lambda : TombFloor(name='Al un sarcofago corrotto'), Chrystal)
		},
        'temple' : {\
            '4' : (lambda : TempleFloor(name='Il cancello del tempio'),
                   lambda : GateWay('temple','[es]ci','main') ),
            ' ' : TempleFloor,
            'a' : (Altar,VampireDemon),       
            'G' : (lambda : TempleFloor(name = 'Una stanza con vecchi libri, bottigli, ossi e cranii.'),\
                    Gorgoco )
            } }
        
    map_patterns = { \
        'main': 
        [ 'fttttffvfw ###ttf',
        'v...S....t #4#mvt',
        'm.tCCCC .........',
        'f.A...CCCFFCCCCCC',
        'w...v.......S.hCC',
        'CCCCCCCCCFFF.. fa',
        'fc1s2s3c....SAwfF',
        'fcccscBc#tthffffo',
        'f#####ss#ftt FFFF',
        'ffhf.....S ftvfbm',
        'ffmtf f..Sifhtfmf',
        'fbtto P.I   tFFFF',
        'Caxt  A.P  txvbma',
        'CCmFbff.Pib ttmFF',
        'FFFFFFF.FFFFFFFFF'],    

    'tomb_1':
    ['######',
    '#B   #',
    '#    #',
    '###s##',
    '###  #',
    '###1##' ],

    'tomb_2' :
    ['######',
    '# b b#',
    '# #  #',
    '# # ##',
    '### ##',
    '###2##'],

    'tomb_3':
    ['######',
    '#  c #',
    '#s####',
    '#   ##',
    '### ##',
    '###3##'],

    'temple':
    ['##########',
    '#  a  a  #',
    '#        #',
    '## #  ## #',
    '## #  #  #',
    '#G #  # a#',
    '####  ####',
    '#  a     #',
    '#####4####']
    }
    
    def setup(self):
        self.target = self.maps['temple'].get_agents(Gorgoco)[0]
        self.mission_accomplished = False
        
    def goal(self,gui,requested_help=False):
        if self.target.dead:
            if not self.mission_accomplished:
                self.mission_accomplished = True
                gui.prn('<bf>','Hai uccesso il cattivo Gorgoco! Bravo!')
        return self.mission_accomplished

    phrase_list= [Vampire.questions,VampireDemon.questions,Gorgoco.questions,Wolf.questions,\
                 GhostHound.questions,Spectre.questions,Fox.questions,Owl.questions ]

class SmallVampireGame(Game):
    name='Vampires (small)'
    learning_goal='A few mostly irregular verbs (dire,...)'
    intro_text='Devi trovare il talismano magico nella tomba.'
    startx=0
    starty=1
    
    pattern_table = {\
		' ' : TombFloor,
                'v': (TombFloor,Vampire),
                'b': (TombFloor,Bat1)
                }
    map_pattern= [ \
        '############',
        '  b# v # #v#',
        '#  # # v   #',
        '#b b #### ##',
        '## # ##    #',
        '# b#   v#v##',
        '#   v## #  #',
        '############' ]
    def setup(self):
        VampireTalisman().move(self.maps['main'].random_place(6,1,10,6,TombFloor))
        self.mission_accomplished = False
        
    def goal(self,gui,requested_help=False):
        if len(self.player.get_things(VampireTalisman)) >= 1:
            if not self.mission_accomplished:
                self.mission_accomplished = True
                gui.prn('<bf>','Hai trovato il talismano! Bravo!')
        return self.mission_accomplished

    phrase_list= [Vampire.questions]
    
class SmallWolfGame(Game):
    name='Wolf (small)'
    learning_goal='A few mostly irregular verbs (prendere,...)'
    intro_text='Devi prendere cinque fiore biance nella foresta.'
    startx = 0
    starty = 2
    pattern_table = {\
		' ' : Grass,
                'w' : (SparseForest,Wolf),
                'b' : (SparseForest,Bat2),
		'F' : DenseForest,
		'f' : SparseForest,
		'C' : Cliff,
		't' : ThornBushes
                }
    map_pattern= [ \
        'FFFFFFFFFF',
        'FbFFff fwF',
        '   tbwf  F',
        'Ft t FFFFF',
        'FFbFtCCfft',
        'C FFw  ftt',
        'C tbfffw t',
        'F   fff  b',
        'ftwf bf tt', 
        'FFFFFFFFFF' ]
    
    def setup(self):
        for i in range(7):
            Whiteflowers().init_move(self.maps['main'].random_place(1,1,8,8,(Grass,SparseForest)))
        self.mission_accomplished = False
        
    def goal(self,gui,requested_help=False):
        if len(self.player.get_things(Whiteflowers)) >= 5:
            if not self.mission_accomplished:
                self.mission_accomplished = True
                gui.prn('<bf>','Hai trovato cinque fiore biance! Bravo!')
        return self.mission_accomplished

    phrase_list= [Wolf.questions ]

class SilverSword(CommonSword):
    name='una spada di argento'

class SmallSpectreGame(Game):
    name='Spectres (small)'
    learning_goal='A few mostly irregular verbs (andare,...)'
    intro_text='Devi trovare una spada di argento nella foresta.'
    startx=0
    starty=3
    
    pattern_table = {\
		' ' : GraveYard,
                's': (Tomb,Spectre),
		'F' : DenseForest,
		'f' : SparseForest,
		'C' : Cliff,
                'b': (GraveYard,Bat3)
                }
    map_pattern= [ \
        'CCCCCCCCCCCCC',
        'F F  bF FF  F',
        'F b    s  s F',
        '  F FFF  F  F',
        'F b   Fs Fs F',
        'F F  b      F',
        'F  b  FF s CC',
        'C  C  s  fffC', 
        'CCCCCCCCCCCCC']
    
    def setup(self):
        SilverSword().init_move(self.maps['main'].random_place(7,1,11,7,GraveYard))
        self.mission_accomplished = False
        
    def goal(self,gui,requested_help=False):
        if len(self.player.get_things(SilverSword)) >= 1:
            if not self.mission_accomplished:
                self.mission_accomplished = True
                gui.prn('<bf>','Hai trovato la spada di argento! Bravo!')
        return self.mission_accomplished

    phrase_list= [Spectre.questions ]


class MadWizard(AgentWithMessage):
    name='un mago pazzo'
    greeting_text = "Un mago pazzo è qui."
    message_text =  'Ride: Ha ha ha, ho chiamato i demoni vampiri!'
    image="./img/child.gif"


class SmallVampireDemonGame(Game):
    name='Vampire demons (small)'
    learning_goal='A few very irregular verbs (dire,...)'
    intro_text='Devi distruire tutti i demoni.'
    startx=0
    starty=1
    
    pattern_table = {\
		' ' : TempleFloor,
                'a': Altar,
                'v': (TempleFloor,VampireDemon),
                'w': (TempleFloor,MadWizard),
                'A': (TempleFloor,Apple)
                }
    map_pattern= [ \
        '########',
        '   w  a#',
        '#  a  A#', 
        '#  # #v#',
        '#   A###',
        '#v #  v#',
        '########' ]
    
    def setup(self):
        VampireTalisman().move(self.maps['main'].random_place(1,1,4,4,TempleFloor))
        self.targets = self.maps['main'].get_agents(VampireDemon)
        self.mission_accomplished = False
        
    def goal(self,gui,requested_help=False):
        for t in self.targets:
            if not t.dead:
                return self.mission_accomplished
        if not self.mission_accomplished:
            self.mission_accomplished = True
            gui.prn('<bf>','Hai uccesso i demoni vampiri! Bravo!')
        return self.mission_accomplished

    phrase_list= [VampireDemon.questions]
