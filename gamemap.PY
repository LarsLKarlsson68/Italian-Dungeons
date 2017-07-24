# -*- coding: latin_1 -*-


import string
import random
from phrase import choice_if_list
import basic_item

class MapItem(basic_item.BasicItem):
    def __init__(self,name=False,description=False,agents=[],things=[],hidden_things=[],gateway=False):
        # self.agents = agents[:]+filter(lambda x : x, map(lambda a: ((choice_if_list(a) or (lambda : False))()), self.agents))
        self.agents = agents[:]+list(filter(lambda x : x, map(lambda a: ((choice_if_list(a) or (lambda : False))()), self.agents)))
        for a in self.agents:
            a.place = self
        # self.things = things[:]+filter(lambda x : x, map(lambda o: ((choice_if_list(o) or (lambda : False))()), self.things))
        self.things = things[:]+list(filter(lambda x : x, map(lambda o: ((choice_if_list(o) or (lambda : False))()), self.things)))
        for t in self.things:
            t.place = self
        # self.hidden_things = hidden_things[:]+filter(lambda x : x, map(lambda o: ((choice_if_list(o) or (lambda : False))()), self.hidden_things))
        self.hidden_things = hidden_things[:]+list(filter(lambda x : x, map(lambda o: ((choice_if_list(o) or (lambda : False))()), self.hidden_things)))
        if name:
            self.name=name
        if description:
            self.description = description
        if gateway:
            self.gateway = gateway
        elif self.gateway:
            self.gateway=self.gateway()
        basic_item.BasicItem.__init__(self)

    agents=[]
    things=[]
    hidden_things=[]
    gateway = False
    gateway_direction = False
    cannot_enter_text = 'Non poui!'
    image = 'black'
    description=False
    name='un posto'
    status_text=''
    described=False # Been at this class before
    explored = False # Been near
    visited = False #Been at this place before

    def get_image(self):
        if type(self.image) in [tuple,list]:
            x,y = self.coords
            return self.image[my_rand(x,y,len(self.image))]
        else:
            return self.image
        
    def show_on_map(self,gui):
        if not self.explored:
            self.explored = True
            x,y = self.coords
            gui.add_update(('background',self.get_image(),x,y))
        
    def describe(self,gui):
        if not self.description:
            return False
        elif type(self.description) in [tuple,list]:
            x,y = self.coords
            gui.prn(self.description[my_rand(x,y,len(self.description))])
        else:
            gui.prn(self.description)
            
    def prn_name(self,gui):
        if type(self.name) in [tuple,list]:
            x,y = self.coords
            gui.prn(self.name[my_rand(x,y,len(self.name))]+self.status_text)
        else:
            gui.prn(self.name+self.status_text)
            
    def can_enter(self,agent):
        return True
    def events(self,player,gui):
        pass
    def enter_events(self,player,from_place,gui):
        pass
    def can_leave(self,player,to_place,gui):
        return True
    def make_inventory(self,player,gui):
        self.inventory = self.agents[:]+self.things
        self.inventory.remove(player)
        for i in range(len(self.inventory)):
            gui.prn(i+1, self.inventory[i].name+self.inventory[i].status_text)

    def get_agents(self,agent_class,condition=False):
        return [ ag for ag in self.agents
                 if isinstance(ag,agent_class) and (not condition or condition(ag))]
        
    def get_things(self,thing_class,condition=False):
        return [ th for th in self.things
                 if isinstance(th,thing_class) and (not condition or condition(th))]
    
    def distance(self,place):
        x1,y1=self.coords
        x2,y2=place.coords
        return abs(x1-x2)+abs(y1-y2)
            
class GateWay:
    def __init__(self,name,direction,dest_map=False,dest_gateway=False):
        if name:
            self.name = name
        if direction:
            self.direction = direction
        if dest_map or name:
            self.dest_map = dest_map or name
        if dest_gateway or name:
            self.dest_gateway = dest_gateway or name

    def enter(self,player,gui):
        try:
            dest_place = self.map_dict[self.dest_map].gateways[self.dest_gateway]
            player.move(dest_place)
        except KeyError:
            print(self.dest_map, self.dest_gateway)
            gui.prn('Errore, non puoi!')
            
class Wall(MapItem):
    image = 'grey80'
    def can_enter(self,agent):
        return False
    cannot_enter_text = 'C\'é un muro.'

class FreeSpace(MapItem):
    image =  'white'
    def show_on_map(self,gui):
        MapItem.show_on_map(self,gui)
        agents = [ x for x in self.agents if x.visible_on_map ]
        things = [ x for x in self.things if x.visible_on_map ]
        to_display=agents+things
        l=len(to_display)
        for i in range(l):
            to_display[i].show_on_map(gui,xshift=float(2*i+1-l)/(2*(l+2)))
        return None

class Lockable(FreeSpace):
    locked = True
    code=''
    
class LockedDoor(Lockable):
    def __init__(self,name=False,description=False,agents=[],things=[],code=False):
        MapItem.__init__(self,name,description,agents,things)
        if code:
            self.code = code        
        self.status_text= self.locked and '(chiuso)' or ''

    image =  'brown'
    image_opp = False
    
    def can_enter(self,agent):
        return not self.locked
    locked = True
    cannot_enter_text = 'La porta è chiuso con un chiave.'

    def lock_or_unlock(self,gui):
        self.locked= not self.locked
        self.status_text= self.locked and '(chiuso)' or ''
        if self.image_opp:
            self.image, self.image_opp = self.image_opp, self.image
            if self.explored:
                self.game_map.show_place_again(self,gui)

class LockedContainer(Lockable):
    def __init__(self,name=False,description=False,agents=[],things=[],hidden_things=[],code=False):
        MapItem.__init__(self,name,description,agents,things,hidden_things)
        if code:
            self.code = code        
    image =  'brown'
    image_opp = False
    code=''
    locked = True
    contents=[]
    
    def lock_or_unlock(self,gui):
        self.locked = not self.locked
        if self.locked:
            self.hidden_things=self.things[:]
            for x in self.hidden_things:
                x.move(False)
            self.status_text=''
        else:
            for x in self.hidden_things:
                x.move(self)
            self.hidden_things=[]
            self.status_text='(aperto)'
        if self.image_opp:
            self.image, self.image_opp = self.image_opp, self.image
        if self.explored:
            self.game_map.show_place_again(self,gui)

class HidingPlace(FreeSpace):

    def uncover(self,gui):
        for x in self.hidden_things:
            x.move(self)
        self.hidden_things=[]
        if self.explored:
            self.game_map.show_place_again(self,gui)
        
class Trap(FreeSpace):
    intro_text = "C'e una trappola qui. La scorpi?"
    disarmed_text = 'La trappola e disarmato.'
    effect_text = 'La trappola ti ferisce.'
    active = True
    strength=0
    craft=0
    questions=[]
    tries=1
    def enter_events(self,player,from_place,gui):
        if self.active:
            gui.prn(self.intro_text)
            outcome  = self.challenge(player,gui,self.tries)
            if outcome:
                gui.prn(self.disarmed_text)
            else:
                gui.prn(self.effect_text)
                self.effects(player,gui)
            self.active = False
                    
    def effects(self,player,gui):
        player_damage =  self.strength
        player.hp -= player_damage
        player.long_hp -= player_damage/2
        player_magic_damage =  self.craft
        player.sp -= player_magic_damage
        player.long_sp -= player_magic_damage/2
        if player.sp <= 0 or player.hp <= 0:
            player.dead = True
            gui.prn('Soccombi!')
            try:
                winsound.PlaySound('sounds/death.wav',0)
            except RuntimeError:
                pass
            return True

class KeepingTrap(Trap):
    intro_text = "Questo é un posto pericoloso."
    effect_text = "Ti fa male."

    def enter_events(self,player,from_place,gui):
        pass
    
    def can_leave(self,player,to_place,gui):
        gui.prn(self.intro_text)
        outcome  = self.challenge(player,gui,self.tries)
        if outcome:
            return True
        else:
            gui.prn(self.effect_text)
            self.effects(player,gui)
            return False

class AboveCliff(FreeSpace):
    pass

class BelowCliff(Trap):
    down_text = 'Provi a scendere.'
    up_text = 'Provi a salire.'    
    effect_text = 'Aaahh! Cadi!'
    multiple_choice=False
    tries=1
    
    def can_leave(self,player,to_place,gui):
        if isinstance(to_place,AboveCliff):
            gui.prn(self.down_text)
            outcome  = self.challenge(player,gui,self.tries)
            if outcome:
                return True
            else:
                gui.prn(self.effect_text)
                self.effects(player,gui)
                return False
        else:
            return True
                
    def enter_events(self,player,from_place,gui):
        if isinstance(from_place,AboveCliff):
            gui.prn(self.up_text)
            outcome  = self.challenge(player,gui,self.tries)
            if not outcome:
                gui.prn(self.effect_text)
                self.effects(player,gui)

        
class Map:
    active=False
    def __init__(self,grid_pattern,special_pattern_table = {},name='',map_dict={}):
        self.grid = [ [ map_pattern(x,special_pattern_table) for x in y ] for y in grid_pattern ]
        self.max_x = len(self.grid[0])
        self.max_y = len(self.grid)
        self.all_agents = []
        self.all_things = []
        map_dict[name] = self
        self.name=name
        self.gateways = {}
        for y in range(self.max_y):
            for x in range(self.max_x):            
                self.grid[y][x].coords = (x,y)
                self.grid[y][x].game_map = self
                self.all_agents.extend(self.grid[y][x].agents)
                self.all_things.extend(self.grid[y][x].things+self.grid[y][x].hidden_things+\
                                       [ t for ag in self.grid[y][x].agents for t in ag.things])  
                if self.grid[y][x].gateway:
                    self.gateways[self.grid[y][x].gateway.name] = self.grid[y][x]
                    self.grid[y][x].gateway.map_dict = map_dict
                
    def get_place(self,x,y):
        if 0 <= x < self.max_x and 0 <= y < self.max_y:
            return self.grid[y][x]
        else:
            return False

    def set_place(self,x,y,place):
        if 0 <= x < self.max_x and 0 <= y < self.max_y:
            self.grid[y][x] = place
            place.coords=(x,y)
            
    def show_place(self,place,gui):
        gui.add_update(('center',place.coords[0],place.coords[1]))
        gui.add_update(('clear',))
        place.show_on_map(gui)
        grid = self.grid
        x,y = place.coords
        if x-1 >= 0:
            grid[y][x-1].show_on_map(gui)
        if x+1 < self.max_x:
            grid[y][x+1].show_on_map(gui)
        if y-1 >= 0:
            grid[y-1][x].show_on_map(gui)
        if y+1 < self.max_y:
            grid[y+1][x].show_on_map(gui)
        gui.updates_ready()

    def show_place_again(self,place,gui):
        if self.active:
            place.explored=False
            place.show_on_map(gui)
            gui.updates_ready()
    
    def place_in_direction(self,place,direction):
        coords = place.coords
        try:
            move_coords = {'n': (0,-1), 's': (0,1), 'e': (1,0), 'o': (-1,0) }[direction]
        except KeyError:
            return False
        coords = (coords[0]+move_coords[0],coords[1]+move_coords[1])
        if 0 <= coords[0] < self.max_x and 0 <= coords[1] < self.max_y:
            return self.grid[coords[1]][coords[0]]
        else:
            return False
        
    def random_place(self,xmin,ymin,xmax,ymax,place_class):
        place = False
        count = 0
        while count < 100:
            place = self.get_place(random.randint(xmin,xmax),random.randint(ymin,ymax))
            if isinstance(place,place_class):
                return place
            count += 1
        for x in range(xmin,xmax+1):
            for y in range(ymin,ymax+1):
                place = self.get_place(x,y)
                if isinstance(place,place_class):
                    return place                    
        print('Warning: Could not find a good place (%d %d %d %d %s)'% (xmin,ymin,xmax,ymax,place_class))
        return False

    def redraw_map(self,gui):
        gui.add_update(('newmap', [ [p.explored and p.get_image() for p in line] for line in self.grid ]))
        
    def get_places(self,place_class,condition=False):
        return [ pl for row in self.grid for pl in row
                 if isinstance(pl,place_class) and (condition and condition(pl) or not condition)
                 ]
        
    def get_agents(self,agent_class,condition=False):
        return [ ag for ag in self.all_agents
                 if isinstance(ag,agent_class) and (not condition or condition(ag))]
        
    def get_things(self,thing_class,condition=False):
        return [ th for th in self.all_things
                 if isinstance(th,thing_class) and (not condition or condition(th))]

                
standard_pattern_table =\
 { '#' : Wall,
   ' ' : FreeSpace
   }

def map_pattern(ch,special_pattern_table):
    try:
        place_spec = special_pattern_table[ch]
    except KeyError:
        try:
            place_spec = standard_pattern_table[ch]
        except KeyError:
            return FreeSpace()
    if not type(place_spec) in [tuple,list]:
        return place_spec()
    else:
        place=False
        gateway=False
        rest=[]
        for c in place_spec:
            o = choice_if_list(c)()
            if isinstance(o,MapItem):
                place=o
            elif isinstance(o,GateWay):
                gateway=o
            else:
                rest+=[o]
        if not place and not ch==' ':
            place=map_pattern(' ',special_pattern_table)
        elif not place:
            print("Error in map: "+ch)
            place= FreeSpace()
        place.gateway=gateway
        for o in rest:
            o.move(place)
        return place

def my_rand(x,y,limit):
    s1=str((x+2)**(1.0/2))
    if '.' in s1:
        s1=s1[s1.find('.')+1:]
    s2=str((y+2)**(1.0/3))
    if '.' in s2:
        s2=s2[s2.find('.')+1:]
    return (int(s1)+int(s2))%limit

    
