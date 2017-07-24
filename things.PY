# -*- coding: latin_1 -*-

import gamemap 
from agents import get_agent_class
import basic_item

class Thing(basic_item.BasicItem):
    visible_on_map = True
    use_cost = 2
    image = 'yellow'
    description = False
    name= '???'
    status_text=''
    
    def __init__(self,name=False):
        if name:
            self.name = name
        self.place = False
        basic_item.BasicItem.__init__(self)

    def move(self,dest):
        current_place = self.place
        if current_place:
            current_place.things.remove(self)
        if dest:
            dest.things.append(self)
        self.place = dest

    def init_move(self,place):
        self.move(place)
        if isinstance(place,get_agent_class()):
            self.place.place.game_map.all_things.append(self)
        else:    
            self.place.game_map.all_things.append(self)
        
    def use(self,player,gui):
        pass

    def dont_use(self,player,gui):
        pass

    def look_at(self,player,gui):
        if self.description:
            gui.prn(self.description)
        else:
            gui.prn("Vedi niente particulare.")            

    def is_magic_thing(self):
        return False

    def show_on_map(self,gui,xshift=0):
        x,y=self.place.coords
        gui.add_update(('foreground',self.image,x+xshift,y))
     
class Weapon(Thing):
    use_cost = 1
    strength = 1
    opponent_class=False
    special_strength=0
    def __init__(self,name=False):
        if not self.description:
            self.description = 'Forte: %d.' % self.strength
        Thing.__init__(self,name)
        
    def use(self,player,gui):
        self.move(player)
        player.weapon = self
        gui.prn('Usi %s.' % self.name)

    def dont_use(self,player,gui):
        if player.weapon == self:
            player.weapon = False
            gui.prn('Cessi a usare %s.' % self.name)

    def get_special_damage(self,target):
        return self.opponent_class and isinstance(target,self.opponent_class) and self.special_strength or 0
    
class Armour(Thing):
    strength=1
    opponent_class=False
    special_strength=0
    def __init__(self,name=False):
        if not self.description:
            self.description = 'Protezione: %d.' % self.strength
        Thing.__init__(self,name)
        
    def use(self,player,gui):
        self.move(player)
        player.armour = self
        gui.prn('Usi %s.' % self.name)

    def dont_use(self,player,gui):
        if player.armour == self:
            player.armour = False
            gui.prn('Cessi a usare %s.' % self.name)
            
    def get_protection(self,attacker,damage):
        protection = self.strength+(self.opponent_class and\
                  (isinstance(attacker,self.opponent_class) or\
                   attacker.weapon and isinstance(attacker.weapon,self.opponent_class)) and\
                   self.special_strength) or 0
        return min((protection+1)/2,damage)+min(protection,max(0,damage-(protection+1)/2))/2

class Food(Thing):
    hp=0
    sp=0

    def __init__(self,name=False,hp=False,sp=False):
        if not hp== False:
            self.hp=hp
        if not sp== False:
            self.sp=sp
        Thing.__init__(self,name)
        
    def use(self,player,gui):
        self.move(False)
        if player.failed_questions:
            question = player.failed_questions.pop()
            if not question[0](*(question[1]+(gui,))):
                self.hp /= 2
                self.sp /= 2
            if len(player.failed_questions) < 10:
                player.failed_questions.append(question)
        player.hp = min(player.max_hp,player.hp+self.hp)
        player.long_hp = min(player.max_hp,player.long_hp+self.hp)
        player.sp = min(player.max_sp,player.sp+self.sp)
        player.long_sp = min(player.max_sp,player.long_sp+self.sp)
        gui.prn(self.use_text)

    use_text = 'Buono!'

class BasicMagicThing(Thing):
    use_cost = 1
    activated = True
    def craft_aid_off(self,opponent):
        return 1
    
    def craft_aid_def(self,opponent):
        return 1
   
    def use(self,player,gui):
        self.move(player)
        player.magic = self
        gui.prn('Usi', self.name+'.')

    def dont_use(self,player,gui):
        if player.magic == self:
            player.magic = False
            gui.prn('Cessi a usare %s.' % self.name)
    def is_magic_thing(self):
        return True
        
class MagicThing(BasicMagicThing):
    off=1
    deff=1
    opponent_class=get_agent_class()
    understand=5
    activated=False
    activated_description= False
    multiple_choice=False
    
    def craft_aid_off(self,opponent):
        return self.activated and isinstance(opponent,self.opponent_class) and self.off or 1
        
    def craft_aid_def(self,opponent):
        return self.activated and isinstance(opponent,self.opponent_class) and self.deff or 1

    def look_at(self,player,gui):
        Thing.look_at(self,player,gui)
        if not self.activated:
            gui.prn("C'è qualcosa misterioso qui.")
            understand = self.understand
            while understand > 0:
                outcome = self.challenge(player,gui)
                if not outcome:
                    player_damage = min((understand+3)//4,player.sp)
                    gui.prn('Perdi %d punti di spirito.\n' % player_damage)
                    player.sp -= player_damage
                    player.long_sp -= player_damage/2
                    return False
                else:
                    understand = understand-player.craft
            self.activated = True
        if self.activated_description:
            gui.prn(self.activated_description)
        return True

    def use(self,player,gui):
        if self.activated:
            BasicMagicThing.use(self,player,gui)
            
class MagicWeapon(Weapon,MagicThing):
    def __init__(self,name= False):    
        MagicThing.__init__(self,name)
        Weapon.__init__(self,name)
    def use(self,player,gui):
        player.weapon = self
        if self.activated:
            player.magic = self
        gui.prn('Usi', self.name+'.')
   
class Key(Thing):
    name='un chiave'
    def __init__(self,name=False,code=False):
        if code:
            self.code=code
        Thing.__init__(self,name)
        
    def use(self,player,gui):
        unlocked_something = False
        if isinstance(player.place,gamemap.LockedContainer) and self.code == player.place.code:
            key_in_place= (self.place==player.place)
            if key_in_place:
                self.move(player)
            player.place.lock_or_unlock(gui)
            if player.place.locked:
                gui.prn('Hai chiuso il coperchio.')
            else:
                gui.prn('Hai aperto il coperchio.')
            unlocked_something = True           
            if key_in_place:
                self.move(player.place)
        for direct in 'eons':
            place = player.place.game_map.place_in_direction(player.place,direct)
            if place and isinstance(place,gamemap.LockedDoor):
                #print 'Trying to unlock door with code', place.code, self.code
                if  self.code == place.code:
                    place.lock_or_unlock(gui)
                    if place.locked:
                        gui.prn('Hai chiuso la porta.')
                    else:
                        gui.prn('Hai aperto la porta.')
                    unlocked_something = True
        if not unlocked_something:
            gui.prn('Non puoi aprire niente qui.')
