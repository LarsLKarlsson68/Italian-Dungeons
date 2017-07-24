# -*- coding: latin_1 -*-

from prep import *
from noun import *
from verb import eng_verb, it_verb, eng_verb_corresponding, verbs, eng_verbs, get_it_verb_basic_form
from numbers import *
from pronoun import *
from conjunctions import *
from interrogatives import *
import random

adj_dict = {}
adverb_dict = { 'solo':'only','anche':'also'}
noun_dict = {}

def choice_if_list(alts):
    if isinstance(alts,list):
        return random.choice(alts)
    else:
        return alts

# Remove '(n)' from end of word
def get_it_word_basic_form(form):
    if '(' in form and form[form.rfind('(')+1] in '0123456789':
        form = form[:form.rfind('(')]
    return form

# Get all italian synomyms for an italian word, by taking English transation
# and searching for that among Italian words, in a given dictionary (table)
def get_synonyms(word,table,remove_uscore=False):
    if '/' in word:
        syn = get_it_parts(word)
    else:
        eng = get_eng_help(word,table)
        syn = [ get_it_word_basic_form(it) for it in table if type(table[it]) == str and eng == table[it] or \
            type(table[it]) == tuple and eng in table[it] ]
    if remove_uscore:
        return [ s.replace('_',' ') for s in syn ]
    else:
        return syn

# Get English translation for Italian word, removing '(n)'
def get_eng(word,table):
    eng = get_eng_part(word) or get_eng_help(word,table)
    if '(' in eng: # and eng[eng.index('(')+1] in '0123456789':
        eng = eng[:eng.index('(')]
    return eng


def get_eng_help(word,table):
    if '(' in word and word[word.index('(')+1] in '0123456789':
        index = int(word[word.index('(')+1:-1])
        word = word[:word.index('(')]
    else:
        index = 0
    eng = table[word]
    if type(eng) == tuple:
        eng = eng[index]    
    return eng

def it_verb_syn(form,tempus,person,prep=False,neg=False,adverb=False):
    return [ it_verb(form1,tempus,person,prep,neg,adverb) for form1 in get_it_parts(form) ]


# For using "it/eng" form of strings, combining Italian and English in one string.
# Alternatives in Italian: "it1|it2/eng"

def get_eng_part(word):
    if '/' in word:
        return word[word.find('/')+1:]
    else:
        return False

def get_it_parts(word):
    return word.split('/')[0].split('|')

# For extracting a vocabulary from phrases. Recursive
def extract_vocabularies(word,wclass,game):
    if not word:
        pass
    elif isinstance(word,(list,tuple)):
        # List or tuple
        for w in word:
            extract_vocabularies(w,wclass,game)
    elif isinstance(word,phrase_base_class):
        # Phrase
        word.extract_vocabularies(game)
    elif isinstance(word,str):
        #String
        update_vocabulary_lists(word,wclass,game)
        
    
def update_vocabulary_lists(word,wclass,game):
    if wclass == 'verb':
        update_verb_list(word,game)
    else:
        # Vocabulary, that is dictionary with translations
        voc_to_use = {'verb':verbs, 'noun': noun_dict, 'adj':adj_dict, 'adv':adverb_dict, 'prep': prepositions,
                      'conj': conjunction_dict, 'int': interrogative_dict}[wclass]
        # Vocabulary list, that is just list of italian words used
        voc_list_to_use = {'noun': game.noun_list, 'adj':game.adjective_list, 'adv':game.adverb_list, 'prep': game.preposition_list,
                           'conj': game.conjunction_list, 'int': game.interrogative_list}[wclass]
        e = get_eng_part(word)
        for w in get_it_parts(word):
            w2 = get_it_word_basic_form(w) # Get rid of '(number)' at end
            if w2 not in voc_to_use:
                if not e:
                    print('Warning: missing translation for '+w+'!')
                    e='*Missing*'
                voc_to_use[w2]= (e,)
            elif e:
                if isinstance(voc_to_use[w2],str):
                    voc_to_use[w2]=(voc_to_use[w2],)
                if e not in voc_to_use[w2]: 
                    voc_to_use[w2] += (e,)  
            if e:
                w = w2+'(%d)'%(list(voc_to_use[w2]).index(e))
            if w not in voc_list_to_use:
                voc_list_to_use += [w]
            
def update_verb_list(word,game):
    e = get_eng_part(word)
    for w in get_it_parts(word):
        w2=get_it_verb_basic_form(w)
        if w2 not in verbs:
            if not e:
                print('Warning: missing translation for '+w+'!')
                e='*Missing*'
            verbs[w2] = dict(trans=(e,))
            w=w+'(0)'
        elif e:
            try:
                trans = verbs[w2]['trans']
            except KeyError:
                trans=tuple()
                verbs[w2]['trans']=trans
            if isinstance(trans,str):
                trans=(trans,)
                verbs[w2]['trans'] = trans
            if e not in trans:
                verbs[w2]['trans']=trans+(e,)
            w = get_it_word_basic_form(w)+'(%d)'%(list(verbs[w2]['trans']).index(e))
        if w not in game.verb_list:
            game.verb_list += [w]
    if e:
        if '_' in e:
            e=e[:e.index('_')]
        if e[-1] == '+':
            e=e[:-1]
        if not (e in eng_verbs):
            eng_verbs[e]=dict()
     

class prep_phrase:
    person=False
    def __init__(self,prep,noun,adj1=[False],adj2=[False],poss=[False],demon=[False],
                 indef=[False],count=[False],kind=['sd'],post=[False],eng_no_prep=False):
        self.prep = prep
        self.eng_no_prep = eng_no_prep # To be used with verbs ending with prep in italian
        if noun:
            self.noun = noun_phrase(noun,adj1,adj2,poss,demon,indef,count,kind,post)
    def choice(self):
        new_stat = prep_phrase(choice_if_list(self.prep),False)
        new_stat.noun =  self.noun.choice()
        return new_stat
    def it(self):
        preps = get_synonyms(self.prep,prepositions)
        i = [ it_prep_noun(p,n)
            for p in preps for n in self.noun.it()  ]
        return i
    def eng(self):
        if self.eng_no_prep:
            return self.noun.eng()
        else:
            prep = get_eng(self.prep,prepositions)
            return prep+' '+self.noun.eng()
    def extract_vocabularies(self,game):
        extract_vocabularies(self.prep,'prep',game)
        if self.noun:
            self.noun.extract_vocabularies(game)
    def weak_pronoun(self):
        return False

class phrase_base_class:
    pass

class rel_pronoun_phrase(phrase_base_class):
    def __init__(self,person,eng_form,prep=False,obj_noun=False,obj_kind=False):
        self.person = person
        self.eng_form = eng_form  # "who", "which", "that", "whom" or "whose"
        self.prep = prep
        self.obj_noun = obj_noun  # only with "whose", then also obj_person is needed
        self.obj_kind = obj_kind # 's' or 'p'
        
    def choice(self):
        return rel_pronoun_phrase(choice_if_list(self.person),self.eng_form,choice_if_list(self.prep),choice_if_list(self.obj_noun),choice_if_list(self.obj_kind))
    def it(self):
        if self.eng_form == "whose":
            nouns = get_synonyms(self.obj_noun,noun_dict)
            obj_noun,gender = noun_gender(nouns[0])
            obj_noun= it_noun(nouns[0],self.obj_kind)
            obj_person = "3"+self.obj_kind+gender
            if obj_person=="3sm":
                return [ "il cui "+obj_noun ]
            if obj_person=="3sf":
                return [ "la cui "+obj_noun ]
            if obj_person=="3pm":
                return [ "i cui "+obj_noun ]
            if obj_person=="3pf":
                return [ "le cui "+obj_noun ]       
        elif not self.prep:
            return [ "che" ]
        else:
            return [ self.prep+" cui" ]
    def eng(self):
        if self.eng_form == "whose":
            obj_noun = get_eng(self.obj_noun,noun_dict)
            return "whose "+eng_noun(obj_noun,self.obj_kind)    
        elif not self.prep:
            return self.eng_form
        else:
            prep = get_eng(self.prep,prepositions)
            return prep+" "+self.eng_form

    def get_person(self):
        return self.person
    def weak_pronoun(self):
        return True
    def extract_vocabularies(self,game):
        pass

class subj_pronoun_phrase(phrase_base_class):
    def __init__(self,person):
        self.person = person
    def choice(self):
        return subj_pronoun_phrase(choice_if_list(self.person))
    def it(self):
        return [ it_pronoun('subject',self.person) ]
    def eng(self):
        return '*'+eng_pronoun('subject',self.person)+'*'
    def get_person(self):
        return self.person
    def weak_pronoun(self):
        return True
    def extract_vocabularies(self,game):
        pass

class dir_pronoun_phrase(phrase_base_class):
    def __init__(self,person,modifier=[False],person2=[False]):
        self.person = person
        self.modifier = modifier
        self.person2=person2
    def choice(self):
        return dir_pronoun_phrase(choice_if_list(self.person),choice_if_list(self.modifier),
                                  choice_if_list(self.person2))
    def it(self):
        form = it_pronoun((self.weak_pronoun() and 'dirobj') or 'obj disjunctive',self.person)
        if self.modifier:
            form = self.modifier+' '+form
        if self.person2:
            form = form+' e '+it_pronoun('obj disjunctive',self.person2)            
        return [ form ]
    def eng(self):
        form = eng_pronoun('dirobj',self.person)
        if self.modifier:
            form = get_eng(self.modifier,adverb_dict)+' '+form
        if self.person2:
            form = form+' and '+eng_pronoun('dirobj',self.person2)
        return form
    def get_person(self):
        return self.person
    def weak_pronoun(self):
        return not (self.modifier or self.person2)
    def extract_vocabularies(self,game):
        pass

class indir_pronoun_phrase(phrase_base_class):
    def __init__(self,prep,person,eng_no_prep=False):
        self.person = person
        self.prep = prep
        self.eng_no_prep = eng_no_prep
    def choice(self):
        return indir_pronoun_phrase(choice_if_list(self.prep),choice_if_list(self.person),self.eng_no_prep)
    def it(self):
        if self.prep == 'a':
            return [ it_pronoun('indirobj',self.person) ]
        else:
            return [  self.prep+' '+it_pronoun('obj disjunctive',self.person) ]
    def eng(self):
        if self.eng_no_prep:
            return eng_pronoun('obj disjunctive',self.person)
        else:
            return get_eng(self.prep,prepositions)+' '+eng_pronoun('obj disjunctive',self.person)
    def get_person(self):
        return self.person
    def weak_pronoun(self):
        return self.prep == 'a' and not self.person[:2]=='3p'  
    def extract_vocabularies(self,game):
        pass
    

class indef_pronoun_phrase(phrase_base_class):
    def __init__(self,pron,noun=['(m)'],num=['sa']):
        self.pron = pron
        self.noun = noun
        self.num = num
    def choice(self):
        return indef_pronoun_phrase(choice_if_list(self.pron),choice_if_list(self.noun),
                                   choice_if_list(self.num))
    def it(self):
        return [ it_indef_pron(i,self.noun,self.num) for i in indef_pron_get_synonyms(self.pron) ]
    def eng(self):
        return eng_indef_pron(self.pron,self.num)
    def weak_pronoun(self):
        return False
    def extract_vocabularies(self,game):
        pass
    
class demon_pronoun_phrase(phrase_base_class):
    def __init__(self,pron,noun=['(m)'],num=['s']):
        self.pron = pron
        self.noun = noun
        self.num = num
    def choice(self):
        return demon_pronoun_phrase(choice_if_list(self.pron),choice_if_list(self.noun),
                                   choice_if_list(self.num))
    def it(self):
        return [ it_demon_pron(self.pron,self.noun,self.num) ]
    def eng(self):
        return eng_demon_pron(self.pron,self.num)
    def weak_pronoun(self):
        return False
    def extract_vocabularies(self,game):
        pass
    
class noun_phrase(phrase_base_class):
    def __init__(self,noun,adj1=[False],adj2=[False],poss=[False],demon=[False],
                 indef=[False],count=[False],kind=['sd'],post=[False]):
        self.noun = noun
        self.adj1 = adj1
        self.adj2 = adj2
        self.poss = poss
        self.demon = demon
        self.indef = indef
        self.count = count
        self.kind = kind
        self.post = post
        self.person = False
    def choice(self):
        new_stat = noun_phrase(choice_if_list(self.noun),
                                  choice_if_list(self.adj1),
                                  choice_if_list(self.adj2),
                                  choice_if_list(self.poss),
                                  choice_if_list(self.demon),
                                  choice_if_list(self.indef),
                                  choice_if_list(self.count),
                                  choice_if_list(self.kind),
                                  choice_if_list(self.post))
        if new_stat.count:
            if new_stat.count > 1:
                new_stat.kind = 'p'+new_stat.kind[1] 
            else:
                new_stat.kind = 's'+new_stat.kind[1] 
        if new_stat.post and not isinstance(new_stat.post, (str,list)):
            new_stat.post = new_stat.post.choice()
        return new_stat
    def it(self):
        nouns = get_synonyms(self.noun,noun_dict)
        if self.adj1:
            adjs = get_synonyms(self.adj1,adj_dict)
            i = [it_adj_noun(a,n,self.kind) for n in nouns for a in adjs ]
        elif self.demon:
            i = [it_demon_pron_noun(self.demon,n,self.kind[0]) for n in nouns ]
        elif self.indef:
            i = [it_indef_pron_noun(i,n,self.kind[0]) for i in indef_pron_get_synonyms(self.indef) for n in nouns ]
        elif self.poss:
            i = [it_poss_pronoun(self.poss,n,self.kind[0])+' '+
                 it_noun(n,self.kind[0]) for n in nouns ]
        elif self.count and self.count > 1:
            i = [it_adj_noun(it_number(self.count),n,self.kind) for n in nouns ]            
        else:
             i = [ it_noun(n,self.kind) for n in nouns  ]
        if self.adj2:
            adjs = get_synonyms(self.adj2,adj_dict)
            i = [ i2+' '+it_adj(a,n,self.kind[0]) for n in nouns for a in adjs for i2 in i  \
                                    if i2.find(it_noun(n,self.kind[0])) > -1]
        if self.post:
            if type(self.post) == str:
                i = concat_combine(i,' ',get_synonyms(self.post,adverb_dict,True))
            else:
                i = concat_combine(i,' ',self.post.it())
        return i    
    def eng(self):
        e = ''
        noun = get_eng(self.noun,noun_dict)
        if self.adj1:
            adj = get_eng(self.adj1,adj_dict)
            e = eng_adj(adj,self.kind)+' '
        elif self.demon:
            e = eng_demon_pron(self.demon,self.kind[0])+' '
        elif self.indef:
            e = eng_indef_pron(self.indef,self.kind[0])+' '
        elif self.poss:
            e = eng_poss_pronoun(self.poss,self.kind[0])+' '
        elif self.count and self.count > 1:
            e = eng_adj(eng_number(self.count),self.kind[0])+' '             
        if self.adj2:
            adj = get_eng(self.adj2,adj_dict)
            e = e+eng_adj(adj,e and self.kind[0] or self.kind)+' ' 
        e = e+eng_noun(noun,e and self.kind[0] or self.kind)
        if self.post:
            if type(self.post) == str:
                e = e+' '+get_eng(self.post,adverb_dict)
            else:
                e = e+' '+self.post.eng()
        return e   
    def get_person(self):
        n,gender = noun_gender(self.noun)
        if 's' in self.kind:
            return '3s'+gender
        else:
            return '3p'+gender
    def weak_pronoun():
        return False
    def extract_vocabularies(self,game):
        extract_vocabularies(self.noun,'noun',game)
        extract_vocabularies(self.adj1,'adj',game)
        extract_vocabularies(self.adj2,'adj',game)
        extract_vocabularies(self.post,'adv',game)

def get_person(noun_st):
    if type(noun_st) == str:
        n,gender = noun_gender(noun_st)
        return '3s'+gender
    else:
        return noun_st.get_person()

class phrase(phrase_base_class):
    def __init__(self,verb,aux_verb=[False],adverb1=[False],adverb2=[False],
                 subject=[False],dobj=[False],iobj=[False],
                 pred=[False],tempus=['present'],person=[False],
                 pre=[False],post=[False],conj=[False],neg=[False],eng_help=''):
        self.verb = verb
        self.aux_verb = aux_verb
        self.adverb1 = adverb1
        self.adverb2 = adverb2
        self.subject = subject
        self.dobj = dobj
        self.iobj = iobj        
        self.pred = pred        
        self.tempus = tempus
        self.person = person
        self.pre = pre
        self.post = post
        self.conj=conj
        self.neg=neg
        self.eng_help = eng_help
    def choice(self):
        while True:            
            tempus = choice_if_list(self.tempus)
            person = choice_if_list(self.person)
            if (tempus,person) not in [('imperative','1s')]:
                break
        new_stat = phrase(choice_if_list(self.verb),
                          choice_if_list(self.aux_verb),
                          choice_if_list(self.adverb1),
                          choice_if_list(self.adverb2),
                          choice_if_list(self.subject),
                          choice_if_list(self.dobj),
                          choice_if_list(self.iobj),
                          choice_if_list(self.pred),
                          tempus,
                          person,
                          choice_if_list(self.pre),
                          choice_if_list(self.post),
                          choice_if_list(self.conj),
                          choice_if_list(self.neg),
                          choice_if_list(self.eng_help)
                          )
        if new_stat.subject and not type(new_stat.subject) in [str, list]:
            new_stat.subject = new_stat.subject.choice()
        if not new_stat.person and new_stat.subject:
            new_stat.person = get_person(new_stat.subject)
            #Careful - with synonyms for persons, one should be able to get several
            #alteratives here!
        if new_stat.iobj and not type(new_stat.iobj) in [str, list]:
            ok = False
            while not ok:                
                iobj = new_stat.iobj.choice()
                ok = not new_stat.person or not iobj.person or not new_stat.person[0] in '12' or not new_stat.person[0] == iobj.person[0]  
            new_stat.iobj = iobj
        if new_stat.dobj and not type(new_stat.dobj) in [str, list]:
            ok = False
            while not ok:
                dobj = new_stat.dobj.choice()
                ok = not new_stat.person or not dobj.person or not new_stat.person[0] in '12' or not new_stat.person[0] == dobj.person[0]
            new_stat.dobj = dobj
        if new_stat.pre and not type(new_stat.pre) in [str, list]:
            new_stat.pre = new_stat.pre.choice()
        if new_stat.post and not type(new_stat.post) in [str, list]:
            new_stat.post = new_stat.post.choice()
        return new_stat
    def it(self):
        i1 = ['']
        i2 = ['']
        if self.conj:
            i1=[ conj+' ' for conj in get_synonyms(self.conj,conjunction_dict,True) ]
        if self.pre:
            if type(self.pre) == str:
                i1 = concat_combine(get_synonyms(self.pre,adverb_dict,True),' ')
            else:
                i1 = concat_combine(self.pre.it(),' ')
        if self.subject:
            if type(self.subject) == str:
                i1 = concat_combine(i1,get_synonyms(self.subject,noun_dict,True),' ')
            else:
                i1 = concat_combine(i1,self.subject.it(),' ')
        elif (self.tempus in ['subjunctive present','subjunctive perfect'] and self.person[1]=='s'):
            i1 = concat_combine(i1,it_pronoun('subject',self.person),' ')
        if self.aux_verb:
            v = [aux+' '+vb for aux in it_verb_syn(self.aux_verb,self.tempus,self.person,prep=True,neg=self.neg) for vb in it_verb_syn(self.verb,'infinitive',self.person)]
        else:
            v = [ vb for vb in it_verb_syn(self.verb,self.tempus,self.person,neg=self.neg)]
        if self.adverb1:
            if len(self.adverb1) > 5 and self.adverb1[:4] == 'non ':
                i1 = concat_combine(i1,['non '])
                i2 = concat_combine(i2,' ',[ a[4:] for a in get_synonyms(self.adverb1,adverb_dict,True)])
            else:
                i2 = concat_combine(i2,' ',get_synonyms(self.adverb1,adverb_dict,True))
        if self.adverb2:
            i2 = concat_combine(i2,' ',get_synonyms(self.adverb2,adverb_dict,True))
        weak_pron = ''
        if self.dobj:
            if type(self.dobj) == str:
                i2 = concat_combine(i2,' ',get_synonyms(self.dobj,noun_dict,True))                
            else:
                do = self.dobj.it()
                if self.dobj.weak_pronoun():
                    weak_pron = do[0]
                elif len(do[0]) > 5 and do[0][:4] == 'non ':
                    i1 = concat_combine(i1,['non '])
                    i2 = concat_combine(i2,' ',[ d[4:] for d in do])
                else:
                    i2 = concat_combine(i2,' ',do) 
        if self.pred:
            if self.dobj:
                person = get_person(self.dobj)
            else:
                person = self.person
            if len(person) > 2:
                gender = person[2]
            else:
                gender='m'
            kind = person[1]
            i2 = concat_combine(i2,' ',[ it_adj(a,'('+gender+')',kind)
                                        for a in get_synonyms(self.pred,adj_dict,True)])
        if self.iobj:
            if type(self.iobj) == str:
                i2 = concat_combine(i2,' ',self.iobj)
            else:
                io = self.iobj.it()
                if self.iobj.weak_pronoun():
                    if weak_pron:
                        weak_pron = it_combine_dir_and_indir(io[0],weak_pron)
                    else:
                        weak_pron = io[0]
                else:
                   i2 = concat_combine(i2,' ',io) 
        if weak_pron:
            if self.aux_verb:  # put at end of verb
                v = [ v[0][:-1]+weak_pron.replace(' ','') ]
            else:
                v = [ weak_pron+' '+v[0] ]                
        if self.post:
            if type(self.post) == str:
                i2 = concat_combine(i2,' ',get_synonyms(self.post,adverb_dict,True))
            else:
                i2 = concat_combine(i2,' ',self.post.it())
        return concat_combine(i1,v,i2)
    def eng(self):
        e = ''
        if self.conj:
            e = conjunction_dict[self.conj]+' '
        if self.pre:
            if type(self.pre) == str:
                e = get_eng(self.pre,adverb_dict)+' '
            else:
                e = self.pre.eng()+' '
        if self.tempus == 'infinitive':
            e=e+'to '
        elif self.subject:
            if type(self.subject) == str:
                e = e+eng_noun(get_eng(self.subject,noun_dict),'sd')+' '
            else:
                e = e+self.subject.eng()+' '
        else:
            e = e+eng_pronoun('subject',self.person)+' '
        if self.adverb1:
            e = e + get_eng(self.adverb1,adverb_dict)+' '
        if self.aux_verb:
            aux = eng_verb_corresponding(self.aux_verb,self.tempus,self.person,neg=self.neg)
            if not (aux in ['can','must'] or aux[-3:] == ' to'):
                aux += ' to'
            e = e+aux+' '+eng_verb(get_it_parts(self.verb)[0],'infinitive',self.person,trans=get_eng_part(self.verb))
        else:
            e = e+eng_verb_corresponding(get_it_parts(self.verb)[0],self.tempus,self.person,neg=self.neg,trans=get_eng_part(self.verb))
        if self.adverb2:
            e = e+' '+get_eng(self.adverb2,adverb_dict)
        if self.dobj:
            if type(self.dobj) == str:
                e = e+' '+eng_noun(get_eng(self.dobj,noun_dict),'sd')
            else:
                e = e+' '+self.dobj.eng()
        if self.pred:
            e = e+' '+get_eng(self.pred,adj_dict)
        if self.iobj:
            e = e+' '+self.iobj.eng()  
        if self.post:
            if type(self.post) == str:
                e = e+' '+get_eng(self.post,adverb_dict)
            else:
                e = e+' '+self.post.eng()
        if self.tempus == 'imperative':
            e = e+'!'
        return self.eng_help+e  
    def extract_vocabularies(self,game):
        extract_vocabularies(self.verb,'verb',game)
        extract_vocabularies(self.conj,'conj',game)
        extract_vocabularies(self.aux_verb,'verb',game)
        extract_vocabularies(self.adverb1,'adv',game)
        extract_vocabularies(self.adverb2,'adv',game)
        extract_vocabularies(self.subject,'noun',game)
        extract_vocabularies(self.dobj,'noun',game)
        extract_vocabularies(self.iobj,'prep',game)        
        extract_vocabularies(self.pred,'adj',game)        
        extract_vocabularies(self.pre,'adv',game)
        extract_vocabularies(self.post,'adv',game)


#---------- New ---------------------------


class query_phrase(phrase_base_class):
    # Only tempus present, imperfect, future
    def __init__(self,verb,interrogative=[False],int_prep=[False],int_obj=[False],int_kind='s',aux_verb=[False],
                 subject=[False],dobj=[False],iobj=[False],
                 pred=[False],tempus=['present'],person=False,
                 neg=[False],eng_help='', person_in_query=False):
        self.interrogative = interrogative
        self.int_obj = int_obj        # For instance: Quanti mele
        self.int_prep = int_prep      # For instance: Di quale città ..   
        self.int_kind = int_kind      # For instance: Quali mele .. (s or p for mele)   
        self.verb = verb
        self.aux_verb = aux_verb
        self.subject = subject
        self.dobj = dobj
        self.iobj = iobj        
        self.pred = pred        
        self.tempus = tempus
        self.person = person 
        self.neg=neg
        self.eng_help = eng_help
        self.person_in_query = person_in_query  # For e.g. 'chi viene', 'who comes'

    def choice(self):
        tempus = choice_if_list(self.tempus)
        person = choice_if_list(self.person)
        new_stat = query_phrase(choice_if_list(self.verb),
                          choice_if_list(self.interrogative),
                          choice_if_list(self.int_prep),
                          choice_if_list(self.int_obj),
                          choice_if_list(self.int_kind),
                          choice_if_list(self.aux_verb),
                          choice_if_list(self.subject),
                          choice_if_list(self.dobj),
                          choice_if_list(self.iobj),
                          choice_if_list(self.pred),
                          tempus,
                          person,
                          choice_if_list(self.neg),
                          choice_if_list(self.eng_help),
                          self.person_in_query
                          )
        if not new_stat.person and new_stat.subject:
            new_stat.person = get_person(new_stat.subject)
        elif not new_stat.person:
            new_stat.person = '3sm'
            new_stat.person_in_query = True
        if new_stat.int_obj and not type(new_stat.int_obj) in [str, list]:
            new_stat.int_obj = new_stat.int_obj.choice()
        if new_stat.subject and not type(new_stat.subject) in [str, list]:
            new_stat.subject = new_stat.subject.choice()
        if new_stat.iobj and not type(new_stat.iobj) in [str, list]:
            ok = False
            while not ok:                
                iobj = new_stat.iobj.choice()
                ok = not new_stat.person or not iobj.person or not new_stat.person[0] in '12' or not new_stat.person[0] == iobj.person[0]  
            new_stat.iobj = iobj
        if new_stat.dobj and not type(new_stat.dobj) in [str, list]:
            ok = False
            while not ok:
                dobj = new_stat.dobj.choice()
                ok = not new_stat.person or not dobj.person or not new_stat.person[0] in '12' or not new_stat.person[0] == dobj.person[0]
            new_stat.dobj = dobj
        return new_stat
    def it(self):
        i1 = ['']
        i2 = ['']
        if self.interrogative:
            inter = get_synonyms(self.interrogative,interrogative_dict,True)
            if self.int_obj:
                nouns = get_synonyms(self.int_obj,noun_dict,True)
                i1 = [it_adj_noun(j,n,self.int_kind)+' ' for n in nouns for j in inter ]
            else:
                i1=[j+' ' for j in inter ]                
            if self.int_prep:
                i1 = concat_combine(self.int_prep,' ',i1)
                  # Old version
##                if type(self.int_obj) == str:
##                    i1 = concat_combine(i1,[ it_noun(n,self.int_kind) for n in get_synonyms(self.int_obj,noun_dict,True)],' ')
##                else:
##                    i1 = concat_combine(i1,self.int_obj.it(),' ')               
        if self.subject:
            if type(self.subject) == str:
                i2 = concat_combine(i2,' ',get_synonyms(self.subject,noun_dict,True))
            else:
                i2 = concat_combine(i2,' ',self.subject.it())
        if self.aux_verb:
            v = [aux+' '+vb for aux in it_verb_syn(self.aux_verb,self.tempus,self.person,prep=True,neg=self.neg) for vb in it_verb_syn(self.verb,'infinitive',self.person)]
        else:
            v = [ vb for vb in it_verb_syn(self.verb,self.tempus,self.person,neg=self.neg)]
        weak_pron = ''
        if self.dobj:
            if type(self.dobj) == str:
                i2 = concat_combine(i2,' ',get_synonyms(self.dobj,noun_dict,True))                
            else:
                do = self.dobj.it()
                if self.dobj.weak_pronoun():
                    weak_pron = do[0]
                elif len(do[0]) > 5 and do[0][:4] == 'non ':
                    i1 = concat_combine(i1,['non '])
                    i2 = concat_combine(i2,' ',[ d[4:] for d in do])
                else:
                    i2 = concat_combine(i2,' ',do) 
        if self.pred:
            if self.dobj:
                person = get_person(self.dobj)
            else:
                person = self.person
            if len(person) > 2:
                gender = person[2]
            else:
                gender='m'
            kind = person[1]
            i2 = concat_combine(i2,' ',[ it_adj(a,'('+gender+')',kind)
                                        for a in get_synonyms(self.pred,adj_dict,True)])
        if self.iobj:
            if type(self.iobj) == str:
                i2 = concat_combine(i2,' ',self.iobj)
            else:
                io = self.iobj.it()
                if self.iobj.weak_pronoun():
                    if weak_pron:
                        weak_pron = it_combine_dir_and_indir(io[0],weak_pron)
                    else:
                        weak_pron = io[0]
                else:
                   i2 = concat_combine(i2,' ',io) 
        if weak_pron:
            if self.aux_verb:  # put at end of verb
                v = [ v[0][:-1]+weak_pron.replace(' ','') ]
            else:
                v = [ weak_pron+' '+v[0] ]
        i = concat_combine(i1,v,i2)
        if self.verb == 'essere' and self.interrogative == 'dove':
            i_add = [ "dov'è"+s[6:] for s in i if s[:6] == "dove è" ]
            i = i+i_add
        return i
    def eng(self):
        e = ''
        if self.interrogative:
            e = get_eng(self.interrogative,interrogative_dict)+' '
        if self.int_prep:
            prep = get_eng(self.int_prep,prepositions)
            e = prep+' '+e
        if self.int_obj:
            if type(self.int_obj) == str:
                e = e+eng_noun(get_eng(self.int_obj,noun_dict),self.int_kind)+' '
            else:
                e = e+self.int_obj.eng()+' '
        if self.aux_verb:
            aux = eng_verb_corresponding(self.aux_verb,self.tempus,self.person,neg=self.neg)
            if not (aux in ['can','must'] or aux[-3:] == ' to'):
                aux += ' to'
            v1 = aux
            v2 = eng_verb(get_it_parts(self.verb)[0],'infinitive',self.person,trans=get_eng_part(self.verb))
        elif (self.verb=='essere' and self.tempus in ['present','perfect']) or self.person_in_query:
            v1 = eng_verb_corresponding(get_it_parts(self.verb)[0],self.tempus,self.person,neg=self.neg,trans=get_eng_part(self.verb))                
            v2 = ''
        else:
            if self.tempus == 'present':
                if not self.person or self.person[:2] == '3s':
                    v1 = "does"
                else:
                    v1 = "do"
            elif self.tempus == 'perfect':
                v1 = "did"
            elif self.tempus == 'future':
                v1 = "will"                   
            v2 = eng_verb_corresponding(get_it_parts(self.verb)[0],'infinitive',self.person,neg=self.neg,trans=get_eng_part(self.verb))
        if v1 !='':
            e = e+v1+' '
        if self.subject:
            if type(self.subject) == str:
                e = e+eng_noun(get_eng(self.subject,noun_dict),'sd')+' '
            else:
                e = e+self.subject.eng()+' '
        elif not self.person_in_query:
            e = e+eng_pronoun('subject',self.person)+' '
        if v2 != '':
            e = e+v2+' '
        if self.dobj:
            if type(self.dobj) == str:
                e = e+eng_noun(get_eng(self.dobj,noun_dict),'sd')+' '
            else:
                e = e+self.dobj.eng()+' '
        if self.pred:
            e = e+get_eng(self.pred,adj_dict)+' '
        if self.iobj:
            e = e+self.iobj.eng()+' '  
        e = e[:-1]+'?'
        return self.eng_help+e  
    def extract_vocabularies(self,game):
        # TODO: Add new elements
        extract_vocabularies(self.verb,'verb',game)
        extract_vocabularies(self.aux_verb,'verb',game)
        extract_vocabularies(self.subject,'noun',game)
        extract_vocabularies(self.dobj,'noun',game)
        extract_vocabularies(self.iobj,'prep',game)        
        extract_vocabularies(self.pred,'adj',game)        
        extract_vocabularies(self.interrogative,'int',game)        
        extract_vocabularies(self.int_obj,'noun',game)
        extract_vocabularies(self.int_prep,'prep',game)        
       

        
def concat_combine(*args):
    return concat_combine_help(args)

def concat_combine_help(args):
    if not args:
        return ['']
    elif type(args[0]) == str:
        return [ args[0]+rest for rest in concat_combine_help(args[1:]) ]
    else:
        return [ first+rest for first in args[0] for rest in concat_combine_help(args[1:]) ]
        
   


