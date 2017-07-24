# -*- coding: latin_1 -*-

import sys
import time
import random
import operator
import gamemap
from phrase import choice_if_list
import winsound
import copy
import basic_item
import dictionary_help

def get_agent_class():
    return Agent

# The player and adversaries are of class agent (or derivatives)
class Agent(basic_item.BasicItem):
    def __init__(self,name=False,things=[],weapon=False,magic=False,armour=False):
        if name:
            self.name=name
        self.max_hp = self.hp
        self.long_hp = self.hp
        self.max_sp = self.sp
        self.long_sp = self.sp
        self.place = False
        self.state = 0
        self.dead = False
        self.things = [ choice_if_list(o) for o in things]+[ choice_if_list(o)() for o in self.things ]
        if weapon:
            self.weapon=choice_if_list(weapon)
            self.things.insert(-1,self.weapon)
        elif self.weapon:
            self.weapon = choice_if_list(self.weapon)()
            self.things.insert(-1,self.weapon)
        if magic:
            self.magic=choice_if_list(magic)
            self.things.insert(-1,self.magic)
        elif self.magic:
            self.magic = choice_if_list(self.magic)()
            self.things.insert(-1,self.magic)
        if armour:
            self.armour=choice_if_list(armour)
            self.things.insert(-1,self.armour)
        elif self.armour:
            self.armour = choice_if_list(self.armour)()
            self.things.insert(-1,self.armour)
##            
##        self.things = filter(lambda x: x, map(lambda o: choice_if_list(o), things)+\
##                             map(lambda o: ((choice_if_list(o) or (lambda : False))()), self.things)+((self.weapon and [self.weapon]) or [])+\
##                            ((self.magic and [self.magic]) or [])+((self.armour and [self.armour]) or []))
        for t in self.things:
            t.place = self
        self.escape_place = False
        self.base = False
        basic_item.BasicItem.__init__(self)


    name= '???'
    hp=10
    strength=1
    sp=10
    craft=1
    things=[]
    weapon=False
    magic=False
    armour=False
    move_max=0
    allowed_places=gamemap.MapItem
    forbidden_places=tuple()
    image = 'red'    
    sound = False
    visible_on_map = True
    multiple_choice=False
    greeting_text=''
    status_text=''

    def look_at(self,player,gui):
        gui.prn("Vedi niente particulare.")
    
    def move(self,dest):
        current_place = self.place
        self.escape_place = current_place
        if current_place:
            current_place.agents.remove(self)
        if dest:
            dest.agents.append(self)
        self.place = dest

    def init_move(self,place):
        self.move(place)
        self.place.game_map.all_agents.extend([self])
        self.place.game_map.all_things.extend(self.things)

    def random_move(self,stay_prob=0.25):
        if (not self.dead) and self.place and (self.move_max > 0) and (random.random() > stay_prob):
            if not self.base:
                self.base = self.place.coords
            directions = ['n','s','e','o']
            while directions:
                try_dir = random.choice(directions)
                directions.remove(try_dir)
                try_place = self.place.game_map.place_in_direction(self.place,try_dir)
                if try_place and try_place.can_enter(self) and isinstance(try_place,self.allowed_places)  and \
                    not isinstance(try_place,self.forbidden_places):
                    try_coords = try_place.coords
                    if abs(self.base[0]-try_coords[0])+abs(self.base[1]-try_coords[1]) <= self.move_max:
                        self.move(try_place)
                        return True
        return False

    # encounter : provides the interface and mechanics for an encounter with
    # an adversary or other agent
    # Should be modified for peaceful agents
    
    def encounter(self,player,gui):
       # return True
        if self.dead or player.dead:
            return False
        # Introduction to encounter (specified in subclasses)
        if self.state == 0:
            self.greeting(player,gui)
        player.redisplay = True

    def craft_aid_off(self,opponent):
        if self.magic:
            return self.magic.craft_aid_off(opponent)
        else:
            return 1

    def craft_aid_def(self,opponent):
        if self.magic:
            return self.magic.craft_aid_def(opponent)
        else:
            return 1
                                    
    def greeting(self,player,gui):
        gui.prn(choice_if_list(self.greeting_text))
        equip=[]
        if self.weapon:
            equip+= [self.weapon.name]
        if self.armour:
            equip+= [self.armour.name]
        if self.magic:
            equip+= [self.magic.name]
        if equip:
            equip_text = 'Ha '
            equip_max = len(equip)-1
            for i in range(equip_max+1):
                if i == equip_max:
                    if i > 0:
                        equip_text+=' e '
                    equip_text+= equip[i]+'.'
                else:
                    equip_text+= equip[i]
                    if i+1 < equip_max:
                        equip_text+= ', '
            gui.prn(equip_text)
        self.state = 1
        gui.prn('')

    def talk_with(self,player,gui):
        return False


    def print_status(self,gui):    
        gui.prn('PC: %d(%d) PS: %d(%d) Arma: %s Armatura: %s Magia: %s' % \
              (self.hp, self.max_hp, self.sp, self.max_sp,
              (self.weapon and self.weapon.name) or '-',
                (self.armour and self.armour.name) or '-',
               (self.magic and self.magic.name) or '-'))
        
    def inventory(self,gui):
        use_cost = 0
        while True:
            max_no = len(self.things)
            if max_no == 0:
                gui.prn('Hai niente.')
                return True
            else:
                gui.prn('Attrezzatura:')
            for i in range(max_no):
                gui.prn(i+1, self.things[i].name)
            gui.prn("[l]ascio #num [u]so #num [c]esso di usare #num [v]edo #num [<-\'] fino")
            reply = (gui.get_input()).strip().split(' ')
            if reply == ['']:
                return use_cost
            try:
                numbers = [ int(s)-1 for s in reply[1:] ] # map(lambda s: int(s)-1, reply[1:])
            except ValueError:
                gui.prn('Errore!')
                numbers = []
            things_copy = self.things[:]
            if reply[0][0] in 'lL':
                gui.pr('Lasci: ')
                for j in numbers:
                    if 0 <= j < max_no:
                        things_copy[j].move(self.place)
                        if things_copy[j] == self.weapon:
                            self.weapon = False
                        if things_copy[j] == self.magic:
                            self.magic = False
                        gui.pr(things_copy[j].name)
                gui.prn('')
            elif reply[0][0] in 'uU':
                for j in numbers:
                    if 0 <= j < max_no:
                        things_copy[j].use(self,gui)
                        self.print_status(gui)
                        use_cost += things_copy[j].use_cost
            elif reply[0][0] in 'cC':
                for j in numbers:
                    if 0 <= j < max_no:
                        things_copy[j].dont_use(self,gui)
                        use_cost += things_copy[j].use_cost
            elif reply[0][0] in 'vV':
                for j in numbers:
                    if 0 <= j < max_no:
                        things_copy[j].look_at(self,gui)
            else:
                gui.prn('Non è una alternativa.')

    def show_on_map(self,gui,xshift=0):
        x,y=self.place.coords
        gui.add_update(('foreground',self.image,x+xshift,y))

    def get_things(self,obj_class,condition=False):
        # obj_list = filter(lambda x: isinstance(x,obj_class) and (not condition or condition(x)),
        #                  self.things)
        obj_list = [ x for x in self.things if isinstance(x,obj_class) and (not condition or condition(x)) ]
        return obj_list
    
    def count_things(self,obj_class,condition=False):
        return len(self.get_things(obj_class,condition))
                          

class Enemy(Agent):

    battle_text = False
    magic_text = False
    defeated_text = 'Sei vittorioso!'
    dead_suffix_text = ' (morte)'    
    vulnerable_body = True
    vulnerable_spirit = True
    initiative = False
    multiple_choice=False
    questions=[]
    visible_on_map = False
    
    def encounter(self,player,gui):
       # return True
        if self.dead or player.dead:
            return False
        # Introduction to encounter (specified in subclasses)
        if self.state == 0:
            self.greeting(player,gui)
        player.redisplay = True
        player_initiative = self.initiative==False and random.randint(0,1) or self.initiative
        last_reply = (self.vulnerable_body and 'c' or 'i')
        extra_attack=False
        if self.sound:
            try:
                winsound.PlaySound(self.sound,0)
            except RuntimeError:
                pass            
        while True:
            prev_player_initiative = player_initiative
            player.print_status(gui)
            if player_initiative:
                gui.prn('Che cosa fai? [c]ombatto%s [i]ncanto%s [f]uggo [a]ttrezzatura (%s): '\
                        % (extra_attack and last_reply=='c' and ' in [p]iu' or '',\
                           extra_attack and last_reply=='i' and ' in [p]iu' or '',last_reply))
                reply = (gui.get_input()).strip() or last_reply
            else:
                reply = self.encounter_action(player)
            if reply in 'Cc':
                last_reply = 'c'
                player_initiative = self.encounter_battle_phase(player,player_initiative,gui)
            elif reply in 'iI':
                last_reply = 'i'
                player_initiative = self.encounter_magic_phase(player,player_initiative,gui)
            elif reply in 'pP' and extra_attack:
                if last_reply == 'c':
                    player_initiative = self.encounter_battle_phase(player,player_initiative,gui,extra=True)
                else:
                    player_initiative = self.encounter_magic_phase(player,player_initiative,gui,extra=True)
            elif reply in 'fF':
                last_reply = 'f'
                if player.escape_place:
                    reply2 = self.encounter_action(player)
                    if reply2 in 'Cc':
                        player_initiative = self.encounter_battle_phase(player,0,gui)
                    elif reply2 in 'iI':
                         player_initiative = self.encounter_magic_phase(player,0,gui)
                    if player_initiative:    
                        player.move(player.escape_place)
                        gui.prn('Fuggi!')
                        return True
                    else:
                        gui.prn('Non riusci a fuggire!') 
            elif reply in 'aA':
                gui.prn("Puoi cambiare arma o magia senza perdere l'iniziativa.")
                use_cost = player.inventory(gui)
                if use_cost > 1:
                    player_initiative = 0
            elif reply[0] == '?':
                dictionary_help.dictionary_help_dialogue(reply.split(' '),player.game,gui)
            # After action - check if anybody is dead
            if player.sp <= 0 or player.hp <= 0:
                player.dead = True
                gui.prn('Soccombi!')
                try:
                    winsound.PlaySound('sounds/death.wav',0)
                except RuntimeError:
                    pass
                return True
            elif self.sp <= 0 or self.hp <= 0:
                self.defeated(player,gui)
                return True
            if player_initiative == 1 and prev_player_initiative == 1:
                extra_attack=True
            else:
                extra_attack=False
                
    def encounter_action(self,player):                
        if self.strength >= self.craft:
            return 'c'
        else:
            return 'i'

    def encounter_battle_phase(self,player,player_initiative,gui,extra=False):
        extra_damage_mult = extra and 3 or 1
        tries = extra and 2 or 1
        if player_initiative:
            gui.prn('Attacchi %s!' % self.name)
        else:
            battle_text = choice_if_list(self.battle_text)
            gui.prn(battle_text or (self.name.capitalize() + ' attacca!'))
        if player_initiative and not self.vulnerable_body and\
           not (player.weapon and player.weapon.get_special_damage(self)):
            gui.prn('Forza non ha effetto su %s!\n' % self.name)
            outcome = 0
        else:
            outcome = self.challenge(player,gui,tries)                
        self_damage = outcome*player_initiative and \
                      (random.randint(1,extra_damage_mult*(player.strength+((player.weapon and player.weapon.strength) or 0))+\
                        (player.weapon and player.weapon.get_special_damage(self) or 0)))   
        if self_damage > 0:
            self_protection = self.armour and self.armour.get_protection(player,self_damage) or 0
            gui.prn(self.name.capitalize(), 'perde %d punti di corpo.\n' % (self_damage-self_protection))
            self.hp -= max(0,self_damage-self_protection)
            try:
                winsound.PlaySound('sounds/punch.wav',0)
            except RuntimeError:
                pass

        player_damage = (1-outcome)*(1-player_initiative) and \
                        (random.randint(1,self.strength+((self.weapon and self.weapon.strength) or 0))+\
                        (self.weapon and self.weapon.get_special_damage(player) or 0))  
        if player_damage > 0:
            player_protection = player.armour and player.armour.get_protection(self,player_damage) or 0
            gui.prn('Perdi %d punti di corpo.\n' % (player_damage-player_protection))
            player.hp -= max(0,player_damage-player_protection)
            player.long_hp -= max(0,player_damage-player_protection)/2
            if self.sound:
                try:
                    winsound.PlaySound(self.sound,0)
                except RuntimeError:
                    pass

        return outcome

    def encounter_magic_phase(self,player,player_initiative,gui,extra= False):
        extra_damage_mult = extra and 3 or 1
        tries = extra and 2 or 1
        if player_initiative:
            gui.prn('Incanti!')
        else:
            gui.prn(choice_if_list(self.magic_text))
        if player_initiative and not self.vulnerable_spirit:
            gui.prn('Incantesimi non hanno effetto su %s!' % self.name)
            outcome = 0
        else:
            outcome = self.challenge(player,gui,tries)                
        self_damage = outcome*player_initiative*\
                      random.randint(1,max(1,int(extra_damage_mult*(player.craft*player.craft_aid_off(self)/self.craft_aid_def(player)))))
        if self_damage > 0:
            gui.prn(self.name.capitalize(), 'perde %d punti di spirito.\n' % self_damage)
            self.sp -= self_damage
            try:
                winsound.PlaySound('sounds/lightning.wav',0)
            except RuntimeError:
                pass
        player_damage =  (1-outcome)*(1-player_initiative)*\
                        random.randint(1,max(1,int(self.craft*self.craft_aid_off(player)/player.craft_aid_def(self))))
        if player_damage > 0:
            gui.prn('Perdi %d punti di spirito.\n' % player_damage)
            player.sp -= player_damage
            player.long_sp -= player_damage/2
            if self.sound:
                try:
                    winsound.PlaySound(self.sound,0)
                except RuntimeError:
                    pass

        return outcome                  

    def defeated(self,player,gui):
        self.dead = True
        self.status_text = self.dead_suffix_text
        for t in self.things[:]:
            t.move(self.place)
        gui.prn(choice_if_list(self.defeated_text))
        try:
            winsound.PlaySound('sounds/victory.wav',0)
        except RuntimeError:
            pass

        player.redisplay=True

    def greeting(self,player,gui):
        if self.image:
            gui.prim(self.image)
        Agent.greeting(self,player,gui)
        
class AgentWithMessage(Agent):
    visible_on_map = True
    message_text="Bla bla bla!"
    def encounter(self,player,gui):
        gui.prn(choice_if_list(self.greeting_text))
        gui.prn('')
        if self.state == 0:
            self.talk_with(player,gui)
            self.state = 1
            
    def talk_with(self,player,gui):
        gui.prn(choice_if_list(self.message_text))
        gui.prn('')

class AgentWithGift(AgentWithMessage):
    done = False
    done_text=False
    def talk_with(self,player,gui):
        if self.done:
            if self.done_text:
                gui.prn(choice_if_list(self.done_text))
                gui.prn('')
            return False
        gui.prn(choice_if_list(self.message_text))
        gui.prn('')
        self.things[0].move(player)
        self.done=True
        
class ReluctantAgentWithHelp(AgentWithMessage):
    tries = 1
    done = False
    done_text=False
    multiple_choice=False
    def talk_with(self,player,gui):
        if self.done:
            if self.done_text:
                gui.prn(choice_if_list(self.done_text))
                gui.prn('')
            return False
        gui.prn(choice_if_list(self.message_text))
        gui.prn('')
        result = self.challenge(player,gui,self.tries) 
        if result:
            gui.prn(choice_if_list(self.success_text))
            gui.prn('')
            self.success_action(player,gui)
            self.done=True
        else:
            gui.prn(choice_if_list(self.failure_text))
            gui.prn('')
            self.failure_action(player,gui)
        player.redisplay = True
        return False
    def failure_action(self,player,gui):
        pass
    def success_action(self,player,gui):
        pass
    
class WaryReluctantAgent(ReluctantAgentWithHelp):
    def failure_action(self,player,gui):
        self.random_move(0)
        self.visible_on_map = False
        player.redisplay=True
        
class ViolentReluctantAgent(ReluctantAgentWithHelp):
    def failure_action(self,player,gui):
        player_damage = (random.randint(1,self.strength+((self.weapon and self.weapon.strength) or 0))+\
                        (self.weapon and self.weapon.get_special_damage(player) or 0))  
        if player_damage > 0:
            player_protection = player.armour and player.armour.get_protection(self,player_damage) or 0
            gui.prn('Perdi %d punti di corpo.\n' % (player_damage-player_protection))
            player.hp -= (player_damage-player_protection)
            player.long_hp -= (player_damage-player_protection)/2
            if self.sound:
                try:                
                    winsound.PlaySound(self.sound,0)
                except RuntimeError:
                    pass

class MalevolentReluctantAgent(ReluctantAgentWithHelp):
    def failure_action(self,player,gui):
        player_damage = random.randint(1,max(1,int(self.craft*self.craft_aid_off(player)/player.craft_aid_def(self))))
        if player_damage > 0:
            gui.prn('Perdi %d punti di spirito.\n' % player_damage)
            player.sp -= player_damage
            player.long_sp -= player_damage/2
            if self.sound:
                try:
                    winsound.PlaySound(self.sound,0)
                except RuntimeError:
                    pass

class ReluctantAgentWithGift: # Should be combined with other reluctant agent type
    def success_action(self,player,gui):
        if self.things:
            self.things[0].move(player)
        self.done=True
    
class ReluctantAgentOpeningDoor:  # Should be combined with other reluctant agent type
    code=''
    def success_action(self,player,gui):
        for row in self.place.game_map.grid:
            for pl in row:
                if isinstance(pl,gamemap.LockedDoor) and pl.code == self.code:
                    pl.lock_or_unlock(gui)
        self.done=True
        
class GuardingAgent(Enemy):
    initiative = 0
    tries = 1
    def encounter(self,player,gui):
        self.greeting(player,gui)
        result = self.challenge(player,gui,self.tries) 
        if result:
            gui.prn(choice_if_list(self.success_text))
        else:
            gui.prn(choice_if_list(self.failure_text))
            Enemy.encounter(self,player,gui)
        return False

class GuardingAgentOnce(GuardingAgent):
    def encounter(self,player,gui):
        if self.state == 0:
           GuardingAgent.encounter(self,player,gui)
            
