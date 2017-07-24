import verb, noun, prep, pronoun, interrogatives, conjunctions, phrase
    
def dictionary_help_dialogue(reply,game,gui):
    if reply == ['?']:
        gui.pr('[?')
        gui.pr('<it>','word')
        gui.prn('] -  ask for word')
        gui.pr('[?*')
        gui.pr('<it>','verb')
        gui.prn('] -  ask for only irregular forms of a verb')
        if game.verb_list:
            gui.pr('[?v]erbs')
        if game.noun_list:
            gui.pr('[?n]ouns')
        if game.adjective_list:
            gui.pr('[?a]djectives')
        if game.adverb_list:
            gui.pr('[?adv]erbs')
        if game.preposition_list:
            gui.pr('[?p]repositions')
        if game.conjunction_list:
            gui.pr('[?c]onjunctions')
        if game.interrogative_list:
            gui.pr('[?i]nterrogatives')
        if game.pronouns_used:
            gui.pr('[?pro]nouns')            
        gui.prn('')
        return True
    reply=' '.join(reply)[1:].strip()
    if reply == 'v':
        print_verb_vocabulary(gui,game.verb_list)
    elif reply == 'n':
        print_vocabulary(gui,game.noun_list,phrase.noun_dict)
    elif reply == 'a':
        print_vocabulary(gui,game.adjective_list,phrase.adj_dict)
    elif reply == 'adv':
        print_vocabulary(gui,game.adverb_list,phrase.adverb_dict)
    elif reply == 'p':
        print_vocabulary(gui,game.preposition_list,prep.prepositions)
    elif reply == 'c':
        print_vocabulary(gui,game.conjunction_list,conjunctions.conjunction_dict)
    elif reply == 'i':
        print_vocabulary(gui,game.interrogative_list,interrogatives.interrogative_dict)
    elif reply == 'pro':
        gui.prn('<bf>','Personal pronouns')
        print_pronoun_vocabulary(gui)
        gui.prn('<bf>','Indefinite pronouns')
        print_indef_pronoun_vocabulary(gui)
        gui.prn('<bf>','Demonstrative pronouns')
        print_demon_pronoun_vocabulary(gui)
        gui.prn('<bf>','Use [?poss] for possessive pronouns')
    elif reply == 'poss':
        prinf_possessive_pronoun_vocabulary(gui)
    else:
        print_word_info(reply,gui,game.verb_list,game.noun_list,game.adjective_list,game.adverb_list)
        

def word_matches(word,word_in_dict):
    return word == word_in_dict or\
        ( len(word) < len(word_in_dict) and word == word_in_dict[:len(word)] and \
          word_in_dict[len(word)] in '(012' )

def print_word_info(word,gui,vl,nl,adjl,advl):
    if word[0] == '*':
        word = word[1:]
        only_irreg = True
    else:
        only_irreg = False
    for v in vl:
        if word_matches(word,v):
            print_verb_info(v,gui,False,only_irreg)
    for wclass in [ (nl, phrase.noun_dict), (adjl, phrase.adj_dict), (advl, phrase.adverb_dict) ]:
        for w in wclass[0]:
            if word_matches(word,w):
                gui.prn('')
                gui.prn(word+': '+phrase.get_eng(w,wclass[1]))
            
def print_verb_info(form,gui,tempus=False,only_irreg=False):
    try:
        if not tempus:
            all_tempus = ['present','imperfect','future', 'perfect','conditional','imperative', 'subjunctive present','subjunctive imperfect']
            verbinfo = verb.verbs[phrase.get_it_word_basic_form(form)]
            if 'ref' in verbinfo:
                verbinfo = verb.verbs[verbinfo['ref']]
            tempus = [ x for x in all_tempus if not only_irreg or x in verbinfo ]
        gui.prn('')
        gui.pr('<bf>',verb.it_verb(form,'infinitive','1s'))
        gui.prn('<it>',' '+verb.eng_verb(form,'infinitive','3s'))
        # gui.prn(str(tempus))
        for temp in tempus:
            temp_shown = temp[:3]
            if ' ' in temp:
                i=temp.find(' ')+1
                temp_shown+=temp[i:i+3]
            if temp == 'imperative':
                persons = ['2s', '3sm', '1p', '2p', '3p']
                temp_shown='imv'
            else:
                persons = ['1s', '2s', '3sm', '1p', '2p', '3p']
            gui.pr('<it>',temp_shown+': ')
            for pers in persons:
                gui.pr(pronoun.it_pronoun('subject',pers)+' '+verb.it_verb(form,temp,pers)+(not pers == '3p' and ',' or '')) 
            gui.prn('')
        gui.prn('')
    except Exception as e:
        print ('In print_verb_info(%s,gui)'%(form,), e)
        gui.prn('Non conosco!')

def print_verb_vocabulary(gui,verb_list=False):
    gui.prn('')
    verb_list.sort()
    for v in verb_list:
        gui.prn(verb.it_verb(v,'infinitive','3s')+': '+verb.eng_verb(v,'infinitive','3s'))
    gui.prn('')
    
def print_vocabulary(gui,word_list,word_dict):
    gui.prn('')
    word_list.sort()
    for w in word_list:
        if '(' in w: # and eng[eng.index('(')+1] in '0123456789':
            w2 = w[:w.index('(')].replace('_',' ')
        else:
            w2 = w.replace('_',' ')
        gui.prn(w2+': '+phrase.get_eng(w,word_dict))
    gui.prn('')
        
def print_pronoun_vocabulary(gui):
    pers_pronoun_types=[('subject','As subject'),('dirobj','As direct object'),
                        ('indirobj','As indirect object (prep "a")'),
                        ('obj disjunctive','As indirect object (other preps)'),
                        ('reflexive','As reflexive')]
    for ptype in pers_pronoun_types:
        gui.pr('<bf>',ptype[1]+': ')
        for pers in pronoun.pronoun_persons:
            gui.pr(pronoun.it_pronoun(ptype[0],pers))
            gui.pr('<it>',pronoun.eng_pronoun(ptype[0],pers)+'  ')
        gui.prn('')       
    gui.prn('<bf>','Combination indirect + direct object')
    gui.prn('Indirect part changed:', '<it>', 'mi => me, ti => te, ci => ce, vi => ve, si => se')
    gui.prn('Direct part unchanged:', '<it>', 'lo la li le ne')
    gui.prn('Special case indirect 3rd person single:', '<it>', 'gli, le, Le + direct part => glielo, gliela, glieli, gliele, gliene')

def prinf_possessive_pronoun_vocabulary(gui):
    for pers in ['1s', '2s', '3sm', '1p', '2p', '3pm', 'proprio','altrui' ]:
        gui.pr('<it>',pronoun.eng_poss_pronoun(pers)+': ')
        for noun in ['libro','borsa']:
            for number in ['s','p']:
                gui.pr(pronoun.it_poss_pronoun(pers,noun,number))
        gui.prn('')

def print_indef_pronoun_vocabulary(gui):
    pro_list=[ k for k in pronoun.indef_pronouns ]
    pro_list.sort()
    for pro in pro_list:
        gui.pr(pronoun.it_indef_pron(pro,'il libro','s')+':')
        gui.prn('<it>',pronoun.eng_indef_pron(pro,'s'))

def print_demon_pronoun_vocabulary(gui):
    pro_list=[ k for k in pronoun.demon_pronouns ]
    pro_list.sort()
    for pro in pro_list:
        gui.pr(pronoun.it_demon_pron(pro,'il libro','s')+':')
        gui.prn('<it>',pronoun.eng_demon_pron(pro,'s'))
                
    
class FakeGUI:
    def prn(self,*args):
        for i in args:
            print(i,end="")
        print()
    def pr(self,*args):
        for i in args:
            print(i,end="")

    
