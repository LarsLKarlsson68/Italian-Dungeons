# -*- coding: latin_1 -*-

# Run this file to run game

import italian_dungeons, gameinterface
import sys, pickle
import _thread, time

import mice, bandits, vampires, ogres, tower, house, temple, city, trolls

adventures=[(mice.RatGame,mice.Hero),
            (bandits.BanditGame,bandits.Hero),
            (vampires.SmallVampireGame,vampires.Hero),
            (vampires.SmallWolfGame,vampires.Hero),
            (vampires.SmallSpectreGame,vampires.Hero),
            (vampires.SmallVampireDemonGame,vampires.Hero),
            (vampires.VampireGame,vampires.Hero),
            (ogres.OgreGame,ogres.Hero),
            (tower.TowerGame,tower.Hero),
            (tower.ForestGame,tower.Hero),
            (house.HouseGame, house.Hero),
            (temple.TempleGame,temple.Hero),
            (city.CityGame,city.Hero),
            (trolls.TrollGame,trolls.Hero)
            ]

class MainGame(italian_dungeons.Game):

    def __init__(self):
        self.gui = None

    def gui_thread_start(self):
        self.gui = gameinterface.GameInterface(11,11,40)
        self.gui.mainloop()
    
    def play(self):
        gui_thread = _thread.start_new_thread(self.gui_thread_start,tuple())
        print("Thread started")
        while(self.gui == None):
            time.sleep(1)
        time_to_quit=False
        self.gui.prn('<bf>','Welcome to Italian Dungeons!')
        self.gui.prn('<bf>','============================')
        while not time_to_quit:
            self.gui.prn('Select a game to play')
            for i in range(len(adventures)):
                self.gui.pr("[%d]"%(i+1), adventures[i][0].name,'-')
                self.gui.prn('<it>', adventures[i][0].learning_goal)
            self.gui.prn('[l]oad saved game')
            self.gui.prn('[q]uit')
            self.gui.prn('Please enter your choice in the text field below.')
            reply = self.gui.get_input()
            reply = reply.strip().split(' ')[0]
            if reply in 'Ll':
                filename = self.gui.ask_for_load_file()
                if filename:
                    new_game = self.load(filename,self.gui)
                    if new_game:
                        new_game.play(self.gui)
            elif reply.isdigit() and 1 <= int(reply) <= len(adventures):
                # print('You selected '+reply)
                g_class,h_class = adventures[int(reply)-1]
                g_class(h_class()).play(self.gui)
            elif  reply in 'Qq':
                time_to_quit=True
            self.gui.prn('')
        self.gui.quit()    
                
    def load(self,filename,gui):
        f = open(filename,mode='rb')
        if f:
            try:
                # name = f.readline()[:-1]
                name = pickle.load(f)
                if [ a for a, h in adventures if a.__name__ == name ]:
                    g = pickle.load(f)
                else:
                    gui.prn('This is not the right type of file!')
                    g = False
                f.close()
                return g
            except pickle.PickleError:
                gui.prn('Could not load file!')
                return False
        else:
            gui.prn('Could not load file!')
            return False
            
MainGame().play()
