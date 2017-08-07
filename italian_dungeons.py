# -*- coding: latin_1 -*-
# The main game object, with the play method for the main game loop.
# the game object contains the current maps, player and vocabularies.

import sys
import time
import random
import operator
import gamemap
import agents
import things
from gameinterface import *
from phrase import choice_if_list, extract_vocabularies
from questions import phrase_question
import winsound
import copy
import dictionary_help
import pickle

class Game:
    #User supplied fields
    map_pattern = False
    map_patterns= {}  # Dict of names and patterns
    pattern_table = False
    pattern_tables = {}  # 
    startmap=False
    startx=1
    starty=1
    intro_text=''
    name=''
    learning_goal=''
    #Private fields
    player = False
    phrase_list=[]
    
    def __init__(self,player):
        self.maps=dict()
        if self.map_pattern:
            self.map_patterns = dict(main=self.map_pattern)            
        for k in self.map_patterns:
            if self.pattern_table:
                pattern_table = self.pattern_table
            elif '_' in k:
                pattern_table = self.pattern_tables[k[:k.find('_')]]
            else:
                pattern_table = self.pattern_tables[k]
            gamemap.Map(self.map_patterns[k],pattern_table,k,self.maps)
        player.move(self.maps[self.startmap or 'main'].get_place(self.startx,self.starty))
        self.player=player
        player.game=self
        player.place.game_map.all_things.extend(player.things)
        # Take away unnecessary data
        map_pattern = None
        map_patterns= None
        pattern_table = None
        pattern_tables = None
        # For user help
        self.verb_list=[]
        self.noun_list=[]
        self.adjective_list=[]
        self.adverb_list=[]
        self.preposition_list=[]
        self.conjunction_list=[]
        self.interrogative_list=[]
        self.pronouns_used = False
        extract_vocabularies(self.phrase_list,'',self)
        self.setup()
        
    def setup(self):
        pass

    def goal(self,gui,requested_help=False):
        return False

    
    def play(self,gui=False):
        player = self.player
        game_map = player.place.game_map
        game_map.active=True
        if not gui:
            print("No gui, starting one")
            gui = GameInterface(11,11,40)
            gui_thread = thread.start_new_thread(gui.mainloop,tuple())
        player.failed_questions = []
        player.redisplay = True
        self.goal_achieved = self.goal(gui)        
        game_map.redraw_map(gui)
        gui.add_update(('center',player.place.coords[0],player.place.coords[1]))
        if self.intro_text:
            gui.prn('')
            gui.prn(self.intro_text)
            gui.prn('')
            gui.prn('[carica] [salva] [esce] [?]aiuto')
            gui.prn('')
        while True:
            if player.redisplay:
                player.place.prn_name(gui)
                if not player.place.described:
                    player.place.describe(gui)
                    player.place.__class__.described = True
                player.place.redisplay=False
            player.place.events(player,gui)
            if player.dead:
                return False
            other_agents = player.place.agents[:]
            other_agents.remove(player)
            for a in other_agents:
                a.encounter(player,gui)
                if player.dead:
                    return False
            for a in game_map.all_agents:
                if a.random_move() and a.place == player.place:
                    game_map.show_place(player.place,gui)
                    gui.prn('Ecco,', a.name, 'arriva.')                
                    a.encounter(player,gui)
                    if player.dead:
                        return False
                    player.redisplay = True  
            if True:
                game_map.show_place(player.place,gui)
                player.place.visited=True
            if player.redisplay:
                player.place.make_inventory(player,gui)
                player.redisplay = False
            player.print_status(gui)
            gui.prn('Che cosa fai?')
            gui.pr('[n]ord [s]ud [o]vest [e]st',)
            if player.place.gateway and player.place.gateway.direction not in ['[n]','[s]','[o]', '[e]']:
                gui.pr(player.place.gateway.direction)
            gui.pr('[r]imani')
            if len(player.place.agents) > 1:
                gui.pr('[pa]rli #num')
            if len(player.place.things) > 0:
                gui.prn()
                gui.pr('[pr]endi #num [v]edi #num [u]si #num ')
            gui.prn('[a]ttrezature [?]aiuto')
            reply = gui.get_input().strip().split(' ')
            if reply[0] and not reply[0][0]=='?':
                try:
                    numbers = [ int(s)-1 for s in reply[1:] ]  # map(lambda s: int(s)-1, reply[1:])
                except ValueError:
                    gui.prn('Errore!')
                    numbers = []
            if player.place.gateway and reply[0] == player.place.gateway.direction[1:player.place.gateway.direction.find(']')]:
                if not player.place.can_leave(player,player.place.gateway,gui):
                    pass
                else:
                    game_map.active=False
                    player.place.gateway.enter(player,gui)
                    game_map = player.place.game_map
                    game_map.active=True
                    game_map.redraw_map(gui)
                    gui.add_update(('center',player.place.coords[0],player.place.coords[1]))
                    game_map.show_place(player.place,gui)
                    player.redisplay = True
                    player.place.enter_events(player,player.place.gateway,gui)
            elif reply[0] in 'nsoe':
                dest = game_map.place_in_direction(player.place,reply[0])
                if dest and not player.place.can_leave(player,dest,gui):
                    pass
                elif dest and dest.can_enter(player):
                    from_place=player.place
                    player.move(dest)
                    gui.add_update(('center',dest.coords[0],dest.coords[1]))
                    game_map.show_place(dest,gui)
                    gui.prn('Vadi', {'s': 'al sud', 'n': 'al nord', 'e': "al'est", 'o': "al'ovest"}[reply[0]])
                    player.redisplay = True
                    dest.enter_events(player,from_place,gui)
                elif dest:
                    gui.prn(dest.cannot_enter_text)
                else:
                    gui.prn('Non poui!')
            elif reply[0] in 'aA':
                player.inventory(gui)
            elif reply[0] in ['pa','PA']:
                for j in numbers:
                    if 0 <= j < len(player.place.inventory) and \
                    (player.place.inventory[j] in player.place.agents):
                        player.place.inventory[j].talk_with(player,gui)
            elif reply[0] in ['pr','PR']:
                if numbers:
                    gui.pr('Prendi:')
                    something_taken = False
                    for j in numbers:
                        if 0 <= j < len(player.place.inventory) and \
                        (player.place.inventory[j] in player.place.things):
                            player.place.inventory[j].move(player)
                            gui.pr(player.place.inventory[j].name+(j!=numbers[-1] and ',' or '.\n')) 
                            something_taken = True
                    if not something_taken:
                        gui.prn('niente.')
                player.redisplay = True
            elif reply[0] in 'uU':
                if numbers:
                    for j in numbers:
                        if 0 <= j < len(player.place.inventory) and \
                        (player.place.inventory[j] in player.place.things):
                            player.place.inventory[j].use(player,gui)
                player.redisplay = True
            elif reply[0] in 'vV':
                if numbers:
                    for j in numbers:
                        if 0 <= j < len(player.place.inventory):
                            player.place.inventory[j].look_at(player,gui)
                else:
                    player.redisplay = True                
            elif reply[0] in 'rR':
                gui.prn('Ti ricupero.')
                if player.failed_questions:
                    question = player.failed_questions.pop()
                    res, f = question[0](*question[1]+(gui,))
                    if len(player.failed_questions) < 10:
                        player.failed_questions.append(question)
                else:
                    res = 1
                if res:
                    player.hp = player.long_hp
                    player.sp = player.long_sp
                    gui.prn('Ti senti meglio.')
            elif reply[0] == 'esce':
                return True
            elif reply[0] == 'salva':
                filename = gui.ask_for_save_file()
                if filename:
                    self.save(filename,gui)
            elif reply[0] == 'carica':
                filename = gui.ask_for_load_file()
                if filename:
                    new_game = self.load(filename,gui)
                if new_game:
                    new_game.play(gui)
                    return True
            elif reply[0] == 'T':
                if 0 <= numbers[0] < game_map.max_x and 0 <= numbers[1] < game_map.max_y:
                    player.move(game_map.get_place(numbers[0],numbers[1]))
                    game_map.redraw_map(gui)
                    gui.add_update(('center',player.place.coords[0],player.place.coords[1]))
                    game_map.show_place(player.place,gui)
                player.redisplay = True                
            elif reply[0][0] == '?':
                if reply[0] == '?':
                    gui.prn('[carica] [salva] [esce]')
                dictionary_help.dictionary_help_dialogue(reply,self,gui)
            else:
                gui.prn('Non è una alternativa')
            self.goal_achieved = self.goal(gui) 
            time.sleep(1)

    def save(self,filename,gui):
        f = open(filename,mode='wb')
        if f:
            try:
                # f.write(self.__class__.__name__+'\n')
                pickle.dump(self.__class__.__name__,f,3)
                pickle.dump(self,f,3)
                f.close()
            except pickle.PickleError:
                gui.prn('Could not save file!')
        else:
            gui.prn('Could not save file!')

    def load(self,filename,gui):
        f = open(filename,mode='rb')
        if f:
            try:
                # name = f.readline()[:-1]
                name = pickle.load(f)
                if self.__class__.__name__ == name:
                    g = pickle.load(f)
                else:
                    gui.prn('Sorry, wrong adventure: "%s"'%name)
                    g =  False
                f.close()
                return g
            except pickle.PickleError:
                gui.prn('Could not load file!')
                return False
        else:
            gui.prn('Could not load file!')
            return False

class FakeGame(Game):
    def __init__(self,phrase_list):
        # For user help
        self.phrase_list = phrase_list
        self.verb_list=[]
        self.noun_list=[]
        self.adjective_list=[]
        self.adverb_list=[]
        self.preposition_list=[]
        extract_vocabularies(self.phrase_list,'',self)
    
def arena(hero,opp_classes):
    gui = GameInterface(11,11,40)
    gui_thread = thread.start_new_thread(gui.mainloop,tuple())
    ready = False
    while not ready:
        gui.prn('Select an opponent:')
        for i in range(len(opp_classes)):
            if type(opp_classes[i]) == tuple:
                gui.pr(i+1)
                for j in opp_classes[i]:
                    if j and issubclass(j,(agents.Agent,things.Thing,gamemap.MapItem)):
                        gui.pr(j.name)
                gui.prn('')
            else:
                gui.prn(i+1,opp_classes[i].name)
        gui.prn('Q quit')
        try:
            i=int(gui.get_input())
        except ValueError:
            return False           
        arena=gamemap.Map(['######','#    #','######'],{},'arena',{})
        hero.visible_on_map = True
        hero.move(arena.get_place(1,1))
        try:
            opp_class = opp_classes[i-1]
        except KeyError:
            print('Wrong opponent')
            return False
        if not type(opp_class) == tuple:
            opp_class= (opp_class,)
        xpos=2
        for i in opp_class:
            if not i:
                xpos+=1
            elif issubclass(i,gamemap.MapItem):
                arena.set_place(xpos,1,i())
            elif issubclass(i,(agents.Agent,things.Thing)):
                i().move(arena.get_place(xpos,1))

        play_game(arena,hero,gui)
        
def every(fn,item_list):
    for i in item_list:
        if not fn(i):
            return False
    return True

def some(fn,item_list):
    for i in item_list:
        if fn(i):
            return True
    return False

