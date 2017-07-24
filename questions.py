# -*- coding: utf_8 -*-

import random
import sys
import phrase

def phrase_question(phrase_list,gui,multiple_choice=False,tries=1):
    for i in range(tries):
        if multiple_choice:
            res,question = phrase_question_choice(phrase_list,multiple_choice,gui)
        else:
            res,question = phrase_question_write(phrase_list,gui)
        if res == 0:
            return 0, question
    return 1,False

def phrase_question_write(phrase_list,gui):
    ph = phrase.choice_if_list(phrase_list).choice()
    return ask_eng_write(ph.eng(), ph.it(), gui)

def phrase_question_choice(phrase_list, number_of_alts,gui):
    ph1 = phrase.choice_if_list(phrase_list).choice()
    alts = []
    tries = 0
    while len(alts) < number_of_alts and tries < 20:
        ph2 = ph1.choice()
        e = ph2.eng()
        print(e,ph2.it())
        if not (e in [ a[0] for a in alts ]): # filter(lambda a: e == a[0], alts):
            alts.append((e, ph2.it()))
        else:
            tries += 1
    q = random.randint(0,len(alts)-1)
    return ask_it_choice(alts[q][1][0],alts[q][0],alts,gui)
            


def ask_eng_write(ing,it,gui):
    if type(it) == str:
        it = [it]
    gui.pr('Tradurre:')
    gui.prn("<it>",ing)
    reply = gui.get_input().strip()
    gui.prn("<bf>",reply)
    if reply and (reply in it):
        gui.prn('Sei corretto!')
        if len(it) > 1:
            gui.pr('Anche:')
            it_alts = it[:]
            it_alts.remove(reply)
            for it_alt in it_alts:
                gui.pr('<bf>',it_alt)
                if not it_alt == it_alts[-1]:
                    gui.pr('o: ')
            gui.prn('')
        return (1,None)
    else:
        gui.pr('Hai sbagliato! É:')
        for it_alt in it:
            gui.pr('<bf>',it_alt)
            if not it_alt == it[-1]:
                gui.pr('o: ')
        gui.prn('')
        return (0, (ask_eng_write,(ing,it)))

def ask_it_choice(it,ing,alts,gui):
    gui.pr('Tradurre:')
    gui.prn("<bf>",it)
    for i in range(len(alts)):
        gui.prn('<it>',i+1, alts[i][0])
    try:
        reply = int(gui.get_input())
    except ValueError:
        return (0,(ask_it_choice, (it,ing,alts)))
    if reply  < 1 or reply > len(alts):
        return (0,(ask_it_choice, (it,ing,alts)))
    elif it in alts[reply-1][1]:
        gui.prn(reply, 'Sei corretto!')
        return (1,None)
    else:
        gui.prn(reply, 'Hai sbagliato! É:', ing)
        return (0, (ask_it_choice, (it,ing,alts)))

