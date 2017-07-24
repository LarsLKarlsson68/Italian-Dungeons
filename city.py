# -*- coding: cp1252 -*-
from italian_dungeons import *
from gamemap import *
from agents import *
from things import *
import random
from phrase import *
from gameinterface import *
from social import *


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

class Mansion_l(Wall):
    image='./img/mansion-l.gif'
class Mansion_c(Wall):
    image='./img/mansion-c.gif'
class Mansion_r(Wall):
    image='./img/mansion-r.gif'

class BigHouse_l(Wall):
    image='./img/bighouse-l.gif'
class BigHouse_r(Wall):
    image='./img/bighouse-r.gif'
class BigHouse_r_sign(Wall):
    image='./img/bighouse-r-sign.gif'

class SmallHouse(Wall):
    image='./img/smallhouse.gif'
class SmallShop(Wall):
    image='./img/smallshop.gif'
class SmallPub(Wall):
    image='./img/smallpub.gif'

class Well(FreeSpace):
    image='./img/well.gif'
    name='Un pozzo'

class CityWall(Wall):
    image='./img/tiles2.gif'

class LockedGate(LockedDoor):
    image='./img/gatetiles.gif'
    image_opp='./img/gatetiles-open.gif'
    name='Una porta'
    
class OpenGate(LockedDoor):
    image='./img/gatetiles-open.gif'
    image_opp='./img/gatetiles.gif'
    name='Una porta'
    locked = False

class GraveYard(HidingPlace):
    image="./img/grave.gif"
    name = 'Un cimitero'
    
class Tomb(FreeSpace):
    image="./img/tomb.gif"
    name='Una vecchia tomba'

class GrainField(FreeSpace):
    image="./img/grain.gif"
    name='Un campo di grano'

class VegetableField(FreeSpace):
    image="./img/vegetables.gif"
    name='Un campo di verdure'

class Pasture(FreeSpace):
    image="./img/pasture.gif"
    name='Un pascolo'
    
# Indoor places
class MansionFloor(FreeSpace):
    image='grey75'
    name='In un bel palazzo'
    
class MansionLockedDoor(LockedDoor):
    image='./img/doortiles.gif'
    image_opp='./img/doortiles-open.gif'
    name='Una porta'
    
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

class HouseFloor(FreeSpace):
    image='grey75'
    name='In una casa'
    
class HouseLockedDoor(LockedDoor):
    image='./img/wooddoor.gif'
    image_opp='./img/wooddoor-open.gif'
    name='Una porta'
    
class HouseOpenDoor(LockedDoor):
    image='./img/wooddoor-open.gif'
    image_opp='./img/wodddoor.gif'
    name='Una porta'
    locked = False
    
class HouseWall(Wall):
    image='./img/woodwall.gif'
class HouseWallWindow(Wall):
    image='./img/woodwindow.gif'

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

class TrapDoor(FreeSpace):
    image='./img/trapdoor.gif'
    name='Una scala segreta'

    def enter_events(self,player,from_place,gui):
        gui.prn("I bandito hanno entrato la città qui!")
        player.game.discovered_passage = True      

    

class Chest(LockedContainer):
    name='Un baule'
    image='./img/chest-closed.gif'
    image_opp='./img/chest-open.gif'

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
    
class GuardAtGate(ReluctantAgentOpeningDoor,ViolentReluctantAgent):
    tries = 2
    move_max=0
    strength=1
    name='una guardia'
    greeting_text='Una guardia ti guarda con sospetto.'
    message_text = 'La guardia dice: Sei un bandito? Non puoi passare la porta!\n'\
       'Puoi convincere la guardia che non sei un bandito?'
    success_text = 'La guardia dice: Scusi! Devo stare attento.\nApre la grande porta.'
    failure_text = 'La guardia dice: Bandito! Va via!'
    image = "./img/hero3.gif"
    questions=[subjv_q]

class GuardAtNorthernGate(GuardAtGate):
    code='northgate'
class GuardAtSouthernGate(GuardAtGate):
    code='southgate'

class Lute(Thing):
    name='un liuto'
    image='./img/lute.gif'
    
class GuardAtMansion(ReluctantAgentOpeningDoor,ViolentReluctantAgent):
    tries=2
    move_max=0
    strength=1
    name='una guardia'
    code='mansion'
    def talk_with(self,player,gui):
        if not player.get_things(Lute):
            gui.prn('La guardia dice: Vai via!')
        else:
            ViolentReluctantAgent.talk_with(self,player,gui)
            
    greeting_text='Una guardia ti guarda con sospetto.'
    message_text = 'La guardia dice: Sei vero una musicista? Suona!\n'\
       'Puoi convincere la guardia che sei una musicista?'
    success_text = 'La guardia dice: Bello! La musica piace molto il principe. Entri!\nApre la grande porta.'
    failure_text = 'La guardia dice: Male! Va via!'
    image = "./img/hero3.gif"
    questions=[subjv_q]

class PrincesGuard(AgentWithMessage):
    name='una guardia'
    image = "./img/hero3.gif"
    greeting_text='Una guardia con una spada sanguigna è qui'
    message_text='La guardia dice: Ho ucciso un bandito!'
    
class Prince(Agent):
    move_max=0
    strength=1
    name='il principe'
    image = "./img/hero3.gif"
    questions=[subjv_q]
    tries=3
    been_played_for=False
    convinced=0
    
    def talk_with(self,player,gui):
            if not self.convinced and not player.get_things(Lute):
                gui.prn('Il principe dice: Non ho tempo per te. Vai!')
            elif self.convinced < 6:
                if not self.been_played_for:
                    gui.prn('Il principe dice: Souna, musicista! Ci fai dimenticare i nostri problemi.')
                    gui.prn('Suoni, e canti un canzone sui banditi è sui fare resistenza.')
                    self.been_played_for=True
                else:
                    gui.prn('Il principe dice: Un altra canzone, e speriamo che è meglio questa volta.')
                    gui.prn('Suoni, e canti un altro canzone sui banditi è sui fare resistenza.')
                if self.challenge(player,gui,self.tries):
                    self.convinced+=2
                    gui.pr('Il principe dice: Bravo!')
                    if self.convinced >=6:
                        gui.prn('Ho capito... Dobbiamo combattere i banditi! Prendi la mia spada!')  
                        player.game.convinced_prince=True
                        self.send_out_guards(player,gui)
                    else:
                        gui.prn('')
                        gui.prn('Ma non sembra sufficiente convinto.')
                else:
                    gui.prn('Il principe dice: Era terribile!')
                    self.convinced = max(self.convinced-1,0)
            if self.convinced >= 6 and not player.game.prince_knows_about_passage:
                gui.prn('Il principe dice: Man anche dobbiamo scoprire come i banditi possono entrare la città.')
                if player.game.discovered_passage:
                    gui.prn('Dici il principe sul passaggio!')
                    player.game.prince_knows_about_passage=True
                    gui.prn('Il principe dice: Bene! Chiudiamo il passagio!')

    def send_out_guards(self,player,gui):
        bandits=reduce(lambda x,y: x+y,[ player.game.maps[m].get_agents(Enemy,lambda x: not x.dead ) \
                           for m in player.game.maps if not m=='house_mario'],[])
        random.shuffle(bandits)
        for i in range(min(len(bandits),10)):
            b=bandits[i]
            guard = PrincesGuard()
            guard.move(b.place)
            killed=random.choice([guard,b,b])
            killed.dead=True
            killed.status_text=' (morte)'
            
class Musician(Agent):
    name='una musicista'
    greeting_text='Una musicista suona un liuto è canta. I clienti applaudicono.'
    weapon=Lute
    tries=3
    def talk_with(self,player,gui):
        if self.get_things(Lute):
            gui.prn('La musicista dice: Pensi tu sai cantare meglio di me?'\
                'Ascolta - sai cantare meglio, ti do il mio liuto.')
            gui.prn('Suoni, e canti un altro canzone sui banditi è sui fare resistenza.')
            if self.challenge(player,gui,self.tries):
                gui.prn('I clienti applaudicono tanto. La mucisista ti da il liuto.')
                self.get_things(Lute)[0].move(player)
            else:
                gui.prn('I clienti non applaudicono. La mucisista ride.')
    image='./img/girl2.gif'
    questions=[subjv_q]          

        
class WomanInNeed(Agent): 
    name='una donna'
    image='./img/girl2.gif'
    things= [ [Bread,Purse,Ham] ]
    def encounter(self,player,gui):
        if self.state==0:
            gui.prn('Una donna dice: Aiuto! Mi salva!')
            self.state=1
            self.bandits=self.place.game_map.get_agents(Enemy)
        if self.state==1 and every(lambda x: x.dead, self.bandits):
            gui.prn('La donna dice: Grazie!')
            if self.things:
                gui.prn('Ti da ',self.things[0].name)
                self.things[0].move(player)
            self.state==2
        return 0
    def talk_with(self, player, gui):
        pass


class ManInNeed(Agent): 
    name='un signore'
    image='./img/hero2.gif'
    things = [ [Bread,Purse,Ham] ]
    
    def encounter(self,player,gui):
        if self.state==0:
            gui.prn('Un signore dice: Aiuto! I banditi mi rubano!')
            self.state=1
            self.bandits=filter(lambda x: self.place.distance(x.place) <= 1, self.place.game_map.get_agents(Enemy))
        if self.state==1 and every(lambda x: x.dead, self.bandits):
            gui.prn('Il signore dice: Grazie!')
            if self.things:
                gui.prn('Ti da ',self.things[0].name)
                self.things[0].move(player)
            self.state==2
        return 0
    def talk_with(self, player, gui):
        pass

class ManInPub(AgentWithMessage):
    name='un cliente'
    message_text=['Il cliente dice: Il principe è un vigliacco. Solo senti la musica.',
                  'Il cliente dice: Come i banditi possano entrare la città?',
                  'Il cliente dice: I banditi rubano tanto.']
    image='./img/hero2.gif'

class ManOnStreet(AgentWithMessage):
    name='un signore'
    image='./img/hero2.gif'
    message_text=['Il signore dice: Perchè il principe fa niente?',
                  "Il signore dice: C'è una bella locanda sul ovest.",
                  'Il signore dice: Qualcuno dovrebbe fare qualcosa verso i banditi.'] 

    
class Rope(Thing):
    name='una corda'
    image='./img/rope.gif'

    def use(self, player,gui):
        if isinstance(player.place,Well):
            gui.prn('Lascia la corda dentro il pozzo.')
        man_in_well = player.place.get_agents(ManInWell, lambda x: x.in_well)
        if man_in_well:
            man_in_well[0].in_well=False
            gui.prn('Il signore sale la corda.')
            
class ManInWell(Agent): 
    name='un signore'
    image='./img/hero2.gif'
    in_well=True
    visible_on_map=False
    status_text=' (nel pozzo)'
    move_max=0
    def encounter(self,player,gui):
        if self.in_well:
            gui.prn('Nel pozzo, tu senti un voce: Aiuto!')
            player.game.need_rope=True
        elif self.state==0:
            self.status_text=''
            self.visible_on_map=True
            gui.prn('Il signore dice: Hai mi salvato.')
            gui.prn('Anche dice: I banditi ne mi hanno butato.')
            gui.prn('Perchè io suspetta Mario Brutto, che sta nella grande casa verso sudest.')
            player.game.knowns_about_traitor=True
            self.state=1
            self.move_max=8
            
class ShopKeeperRope(Agent):
    name='un negoziante'
    image='./img/hero2.gif'
    
    def talk_with(self,player,gui):
        gui.prn('Il negoziante dice: Dimmi che hai bisogno di qualcosa!')
        if player.game.need_rope and not player.get_things(Rope):
            gui.prn('Rispondi: Ho bisogno una corda lunga.')
            purse =  player.get_things(Purse)
            if purse:
                gui.prn('Il negoziante ti vende una corda.')
                Rope().move(player)
                purse[0].move(self)
            else:
                gui.prn('Ma non hai i soldi!')

class ChainMail(Armour):
    name='una maglia di ferro'
    strength=3
    image='./img/armour.gif'

class LeatherArmour(Armour):
    name='una armatura di cuoio'
    strength=1
    image='./img/armour.gif'

class MarioLockedDoor(HouseLockedDoor):
    code='bandit'
    
class MarioBrutto(Enemy):
    name='Un singore brutto'
    image='./img/hero2.gif'
    strength=4
    hp=15
    craft=3
    sp=15
    things= [ChainMail]
    weapon=CommonSword
    armour=ChainMail
    accused=False
    initiative=0
    greeting_text='Un signore brutto si occupa il negozio.'
    battle_text='Mario ti attacca!'
    visible_on_map=True
    questions=[subjv_q]
    
    def encounter(self,player,gui):
        Agent.encounter(self,player,gui)
        if self.state==0:
            self.talk_with(player,gui)
            self.state=1
        if self.accused:
            self.state=0
            Enemy.encounter(self,player,gui)
            
    def talk_with(self,player,gui):
        if not player.game.knowns_about_traitor and not self.accused:
            gui.prn('Il signore dice: Cia! Sono Mario il Brutto.')
            chainmails=self.get_things(ChainMail,lambda x: not x == self.armour)
            purses=player.get_things(Purse)
            if chainmails:
                gui.prn('Dice: Vuoi vendere una maglia?')
                if purses:
                    gui.prn('Dico: Si, graze!')
                    gui.prn('Lo paghi con %s!'%purses[0].name)                    
                    chainmails[0].move(player)
                    purses[0].move(self)
                else:
                    gui.prn('Ma non hai i soldi.')
                    
        elif not self.accused:
            gui.prn('Il signore dice: Cia! Sono Mario il Brutto. Ti posso vendere qualcosa?')
            gui.prn('Dici: Come hai venduto la città?')
            gui.prn('Ula: Ragazzi!')
            gui.prn('Mario apre una porta.')
            for d in self.place.game_map.get_places(LockedDoor, lambda d: d.code=='bandit'):
                d.lock_or_unlock(gui)
            self.move(self.place.game_map.place_in_direction(self.place,'e'))
            player.place.game_map.show_place(player.place,gui)
            for b in self.place.game_map.get_agents(BigBandit):
                b.move(player.place)
            for b in self.place.get_agents(Enemy):
                b.encounter(player,gui)
            self.accused=True
        else:
            Enemy.encounter(self,player,gui)

    

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
    questions =  4*[ nouns_q ]+[ adjs_q ]


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

    questions =  2*[intransv_q]+[pluralv_q]
    
class Sword(Weapon):
    name='una spada'
    strength=5
    image='./img/sword.gif'

    
class BanditLeader(BigBandit):
    name='un bandito grande'
    hp=20
    strength=6
    move_max=2
    weapon = Sword
    armour = LeatherArmour
    things=[Purse]
    image='./img/bandit2.gif'
    greeting_text='Un bandito grande ti vede è ride: ha ha ha!'    
    question=5*[transv_q]+[specialv_q]
    
class Hero(Agent):
    name='Eroe'
    hp=20
    strength=5
    sp=20
    craft=4
    visible_on_map = True
    weapon = CommonSword
    image="./img/hero.gif"
     
class CityGame(Game):
    startx=7
    starty=13
    name="Bandits and the City"
    learning_goal="Social (verbs incl subjunctive form, nouns, adjectives)" 

    need_rope=False
    convinced_prince=False
    discovered_passage=False
    prince_knows_about_passage=False
    knowns_about_traitor=False
    
    pattern_tables ={ \
        'main': {\
        '#': CityWall,
        ' ' : Field,
        '.' : Path,
        '=' : Road,
        '1' : (lambda: Path(name='Fuori di una casa'), lambda: GateWay('house_1','[n]')),
        '2' : ( lambda: Road(name='Fuori di un negozio'), lambda: GateWay('house_shop1','[n]')),
        '3': (lambda: Road(name='Fouri al palazzo'),lambda: GateWay('mansion_1','[n]')),
        '4' : ( lambda: Road(name='Fuori di una locanda'), lambda: GateWay('house_guest','[n]')),
        '5' : ( lambda: Road(name='Fuori di un negozio'), lambda: GateWay('house_mario','[n]')),
        '6' : (lambda: Road(name='Fuori di una casa'), lambda: GateWay('house_2','[n]')),
        '7' : (lambda: Road(name='Fuori di una casa'), lambda: GateWay('house_3','[n]')),
        '8' : (lambda: Road(name='Fuori di una locanda'), lambda: GateWay('house_4','[n]')),
        '9' : (lambda: Road(name='Fuori di una locanda'), lambda: GateWay('house_5','[n]')),
        'A' : Mansion_l,
        'B' : Mansion_c,
        'C': Mansion_r,
        'D':BigHouse_l,
        'E':BigHouse_r,
        'F':BigHouse_r_sign,
        'G':SmallHouse,
        'H':SmallShop,
        'I':SmallPub,
        'w':(Well,ManInWell),
        'v':VegetableField,
        'f':GrainField,
        'p':Pasture,
        'g':GraveYard,
        't':Tomb,
        '!': (lambda: LockedGate(code='northgate')),
        '"': (Road, GuardAtNorthernGate),
        '¤': (lambda: LockedGate(code='southgate')),
        '%': (Road, GuardAtSouthernGate),
        '&': (Road,ManInNeed,BigBandit),
        '/': (Road,SmallBandit),
        '*': (Road,BigBandit),
        '@': (Road,BanditLeader),
        '+': (Road,ManOnStreet)
        },
        'mansion': {\
            '_' : Field,
            ' ':MansionFloor,
            'h': (MansionFloor,Bread),
            'H': (MansionFloor,Ham),            
            '&':MansionWallWindow,
            'd': MansionOpenDoor,
            '%': MansionWallTapestry,
            'f': Fireplace,
            't': Table,
            'c': Chair,
            's': TableAndStool,
            '3': (lambda: Road(name='Fouri al palazzo'),GuardAtMansion,lambda: GateWay('mansion_1','[s]','main')),
            'b': Barrels,
            'C': Carpet,
            'l': Bookshelf,
            'j': Jarshelf,
            'w': Bottleshelf,
            'k': Chest,
            '!': (lambda: MansionLockedDoor(code='mansion')),
            '*': (Carpet,Prince)
            },
            'house': {\
            '_' : Field,
            ' ':HouseFloor,
            'h': (HouseFloor,Bread),
            'H': (HouseFloor,Ham),            
            '#':HouseWall,
            '&':HouseWallWindow,
            'd': HouseOpenDoor,
            'f': Fireplace,
            't': Table,
            'c': Chair,
            's': TableAndStool,
            'a': Armory,
            'B': Bed,
            '1': (Path,lambda: GateWay('house_1','[s]','main')),
            '2' : ( lambda: Road(name='Fuori di un negozio'), lambda: GateWay('house_shop1','[s]','main')),
            '4' : ( lambda: Road(name='Fuori di una locanda'), lambda: GateWay('house_guest','[s]','main')),
            '5' : ( lambda: Road(name='Fuori di un negozio'), lambda: GateWay('house_mario','[s]','main')),
            '6' : (lambda: Road(name='Fuori di una casa'), lambda: GateWay('house_2','[s]','main')),
            '7' : (lambda: Road(name='Fuori di una casa'), lambda: GateWay('house_3','[s]','main')),
            '8' : (lambda: Road(name='Fuori di una locanda'), lambda: GateWay('house_4','[s]','main')),
            '9' : (lambda: Road(name='Fuori di una locanda'), lambda: GateWay('house_5','[s]','main')),
            'b': Barrels,
            'C': Carpet,
            'l': Bookshelf,
            'j': Jarshelf,
            'w': Bottleshelf,
            'k': Chest,
            '?': TrapDoor,
            '!': (HouseFloor, WomanInNeed,SmallBandit),
            '"': (HouseFloor,SmallBandit),
            '¤': (HouseFloor,ShopKeeperRope),
            'M': (HouseFloor,Musician),
            '+': (TableAndStool,ManInPub),
            'x': (HouseFloor,MarioBrutto),
            'y': MarioLockedDoor,
            '/': (HouseFloor,SmallBandit),
            '*': (HouseFloor,BigBandit),
            '@': (HouseFloor,BanditLeader)

            }

    }

    map_patterns= {\
        'main':
        [
        '      p = ff    ',
        '     ff " vv    ', 
        '  ######!###### ',
        '  #ABC=H=GHG=I# ',
        '  #=3@+=&==+*9# ',
        '  #DF=G=w=G=GG# ',
        '  #=4&H===I&DE# ',
        '  #DE=2=G+8/==# ',
        '  #=/=G=7= DE@# ',
        '  #GG=6+=/==5=# ',
        '  ######¤###### ',
        '        %fffff  ',
        '   fffGf=p      ',
        '   ffp1.=       '
        ],
        'house_1':
        ['##&##',
         '#f H#',
         '&"s"&',
         '# !b#',
         '#&d&#',
         '__1__'],
        'house_2':
        ['##&##',
         '#fhB#',
         '&"s"&',
         '# !b#',
         '#&d&#',
         '__6__'],
        'house_3':
        ['##&###',
         '#kfhB#',
         '&@  @&',
         '#H! b#',
         '#&d&##',
         '__7___'],
        'house_4':
        ['##&###',
         '# f +#',
         '&ts +&',
         '#b  +#',
         '#&d&##',
         '__8___'],
        'house_5':
        ['##&###',
         '#fts+#',
         '&! H+&',
         '#w hb#',
         '#&d&##',
         '__9___'],
        'house_shop1':
        ['##&##',
         '#ktj#',
         '& ¤ &',
         '#b k#',
         '#&d&#',
         '__2__'],
        'mansion_1':
        [
        '#%#&##&#&###&##',
        '#ctch# C #b  w#',
        '%H*  d   d t f#',
        '#k  l% C %   j#',
        '#&##&#   #&##&#',
        '_____#&!&#_____',
        '_______3_______'
        ],
        'house_guest':
        [
        '##&##&##&##',
        '#shfh+#B B#',
        '&+ M s##d##',
        '#bk   d   #',
        '########d##',
        '________4__'
        ],
        'house_mario':
        [
        '########&##',
        '#?bh# tc a#',
        '# @@y x  a#',
        '# bk#H   k#',
        '#####&#d###',
        '_______5___'
        ]

    }
    
    def setup(self):           
        pass

    goal_achieved = False
    bandits=[]    
    def goal(self,gui,req_help=False):
        if not self.bandits:
            self.bandits=[ a for m in self.maps for a in self.maps[m].get_agents(Enemy) ]
            self.bandit_count=len(self.bandits) 
        self.bandits = filter(lambda x: not x.dead, self.bandits)
        if self.prince_knows_about_passage and len(self.bandits) < 0.2*self.bandit_count and not self.goal_achieved:
            gui.prn('<bf>','Hai sconfigguto i banditi! Bravo!')
            self.goal_achieved= True
        return self.goal_achieved            

    phrase_list = [subjv_q,intransv_q,pluralv_q,transv_q,specialv_q,nouns_q,adjs_q]
    
    
def City():
    CityGame(Hero()).play()

    
