# -*- coding: latin_1 -*-
# Scenario with vampires


from verb import *
from gamemap import *
from agents import *
from things import *
from phrase import *
from gameinterface import *


all_verbs = verbs.keys()
vampire_tempus = ['imperative','present','imperfect','conditional','future','perfect','pluskvamperfect']

irreg_verbs = ['dare','fare','andare','vedere','venire','dire','porre','bere','trarre','uscire','morire','sedere',
               'piacere','tenere']

obj_verbs = ['toccare',  'aprire',  'dovere', 'accendere', 'trarre',   'coprire', 'trovare',  'prendere', 'cadere',
 'chiudere',  'costare', 'avere', 'stringere',  'tirare',  'scoprire',   'finire',  'levare', 'portare',
  'stare', 'spingere',  'vincere', 'spegnere', 'tenere', 'bere', 'comprare', 'vendere',   'cambiare', 
  'lasciare',  'lavorare', 'usare',  'fare', 'dare', 'mangiare',  
   'essere', 'vestire', 'pagare',  'porre', 'mettere', 'succedere',  'cominciare']


agent_verbs = ['conoscere', 'rispondere', 'amare', 'dimenticare', 'capire', 'piangere', 'decidere', 'scrivere','pensare',
 'leggere', 'chiedere', 'sapere',  'chiamare', 'dire', 'credere', 'permettere', 'incontrare',
 'proporre', 'vietare', 'preferire', 'imparare', 'ridere',  'giacere', 'morire', 'nascere', 'dormire',
 'ricordare', 'vedere', 'vivere', 'insegnare', 'aiutare', 'suporre', 'odiare', 'potere', 'volere', 
'piacere', 'parlare', 'udire', 'servire', 'sentire', 'provare', 'fallire' ] 

move_verbs =[  'riuscire', 'cercare', 'nascondere', 'spedire', 'venire',  'ricevere', 'perdere',
   'entrare', 'partire', 'girare', 'correre', 'arrivare', 'fermare', 'tornare', 'muovere', 
   'diventare', 'seguire',  'condurre', 'fuggire', 'uscire', 'aspettare', 'inseguire', 'andare',
    'camminare', 'sedere' ]

class DenseForest(MapItem):
    def can_enter(self):
        return False
    cannot_enter_text = 'La foresta é troppo fitto.'
    image="./img/densewood.gif"
    
class Cliff(MapItem):
    def can_enter(self):
        return False
    cannot_enter_text = 'Questi rupi non puoi scalare.'
    image="./img/cliff.gif"
    
class SparseForest(FreeSpace):
    description = 'Una foresta'
                      #choice(['Una foresta', 'Una foresta','Una foresta con alte alberi', 'Una collina nella foresta',\
                      #        'Una radura nella foresta', 'Una foresta molto vecchio'])
    image="./img/sparsewood.gif"

                       
class ForestPath(FreeSpace):
    image = 'yellow'
                       
class House(FreeSpace):
    image="./img/house.gif"
    
class GraveYard(FreeSpace):
    image="./img/grave.gif"

class Tomb(FreeSpace):
    image="./img/tomb.gif"

class Grass(FreeSpace):
    image='olivedrab1'

class Floor(FreeSpace):
    image='grey30'
                       
class ThornBushes(KeepingTrap):    
    intro_text = "Questi cespugli hanno lunghi spini."
    effect_text = "Gli spini ti fa male."
    questions = phrase(obj_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','3sp','1p','1p','2p','2p','3pm','3pf','3pp'])
    image="./img/thorn.gif"
        


class Vampire(Agent):
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
                       person=['1s','1s','2s','2s','3sm','3sf','3sp','1p','1p','2p','2p','3pm','3pf','3pp'])
                       
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
                       person=['1s','1s','2s','2s','3sm','3sf','3sp','1p','1p','2p','2p','3pm','3pf','3pp'])

class Spectre(Agent):
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
                       person=['1s','1s','2s','2s','3sm','3sf','3sp','1p','1p','2p','2p','3pm','3pf','3pp'])

class Gorgoco(Agent):
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
                       person=['1s','1s','2s','2s','3sm','3sf','3sp','1p','1p','2p','2p','3pm','3pf','3pp'])
        
class Bat(Agent):
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
                       person=['1s','1s','2s','2s','3sm','3sf','3sp','1p','1p','2p','2p','3pm','3pf','3pp'])

class Wolf(Agent):
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
                       person=['1s','1s','2s','2s','3sm','3sf','3sp','1p','1p','2p','2p','3pm','3pf','3pp'])

class GhostHound(Agent):
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
                       person=['1s','1s','2s','2s','3sm','3sf','3sp','1p','1p','2p','2p','3pm','3pf','3pp'])

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
    special_damage=8
    understand=8
    activated_description = "Il coltello ha un maledizione verso Gorgoco."
    questions = phrase(irreg_verbs,tempus=vampire_tempus,
                       person=['1s','1s','2s','2s','3sm','3sf','3sp','1p','1p','2p','2p','3pm','3pf','3pp'])


