# -*- coding: latin_1 -*-

from noun import *

#pronoun_persons=['1s','2s','3sm','3sf','3smn','3sfn','3sp','1p','2p','3pm','3pf','3pmn','3pfn','3pp']

pronouns = {
    'subject': { '1s': ('io','I'), '2s': ('tu','you'),  '3sm': ('lui','he'), '3sf': ('lei','she'),
              '3smn': ('esso','it(m)'), '3sfn': ('essa','it(f)'),  '3sp': ('Lei','You'),
              '1p': ('noi','we'), '2p': ('voi','you(pl)'), '3p': ('loro','they'),'3pm': ('loro','they'), '3pf': ('loro','they(f)'),
              '3pmn': ('essi','they(m,things)'), '3pfn':  ('esse','they(f,things)'), '3pp':  ('Loro','You(pl)') },

    'dirobj': { '1s': ('mi','me'), '2s': ('ti','you'),  '3sm': ('lo','him'), '3sf': ('la','her'),
              '3smn': ('lo','it(m)'), '3sfn': ('la','it(f)'),  '3sp': ('La','You'),
              '1p': ('ci','us'), '2p': ('vi','you(pl)'), '3p': ('li','them(m)'),'3pm': ('li','them(m)'),
              '3pmn': ('li','them(m,things)'), '3pf':  ('le','them(f)'), '3pfn':  ('le','them(f,things)'),
                     '3pp':  ('Le','You(pl)'), '4s': ('ne','some of it'), '4p': ('ne','some of them') },   # Loro after verb!

   'indirobj': { '1s': ('mi','to me'), '2s': ('ti','to you'),  '3sm': ('gli','to him'), '3sf': ('le','to her'),
              '3smn': ('gli','to it(m)'), '3sfn': ('le','to it(f)'),  '3sp': ('Le','to You'),
              '1p': ('ci','to us'), '2p': ('vi','to you(pl)'),  '3p': ('loro','to them'),'3pm': ('loro','to them(m)'),
              '3pmn': ('loro','to them(m,things)'), '3pf':  ('loro','to them(f)'), '3pfn':  ('loro','to them(f,things)'),
                     '3pp':  ('Loro','to You(pl)'), },  # Loro after verb!
    
    'obj disjunctive': { '1s': ('me','me'), '2s': ('te','you'),  '3sm': ('lui','him'), '3sf': ('lei','her'),
              '3smn': ('esso','it(m)'), '3sfn': ('essa','it(f)'),  '3sp': ('Lei','You'),
              '1p': ('noi','us'), '2p': ('voi','you(pl)'), '3p': ('loro','them'),'3pm': ('loro','them'), '3pf': ('loro','them'),
              '3pmn': ('essi','them(m,things)'), '3pfn':  ('esse','them(f,things)'), '3pp':  ('Loro','You(pl)') },


    'reflexive': { '1s': ('mi','myself'), '2s': ('ti','yourself'),  '3s': ('si','himself'), '3sm': ('si','himself'), '3sf': ('si','herself'),
              '3smn': ('si','itself(m)'), '3sfn': ('si','itself(f)'),  '3sp': ('Si','Yourself'),
              '1p': ('ci','ourselves'), '2p': ('vi','yourselves'), '3p': ('si','themselves'),'3pm': ('si','themselves'),
              '3pmn': ('si','themselves'), '3pf':  ('si','themselves'), '3pfn':  ('si','themselves'),
                     '3pp':  ('Si','Yourselves(pl)') },   

    'mutual reflexive': { '1s': ('mi','myself'), '2s': ('ti','yourself'),  '3s': ('si','himself'), '3sm': ('si','himself'), '3sf': ('si','herself'),
              '3smn': ('si','itself(m)'), '3sfn': ('si','itself(f)'),  '3sp': ('Si','Yourself'),
              '1p': ('ci','eachother'), '2p': ('vi','eachother'), '3p': ('si','eachother'),'3pm': ('si','eachother'),
              '3pmn': ('si','eachother'), '3pf':  ('si','eachother'), '3pfn':  ('si','eachother'),
                     '3pp':  ('Si','Eachother(pl)') },   

    'reflexive disjunctive': { '1s': ('me','myself'), '2s': ('te','yourself'),  '3sm': ('sè','himself'), '3sf': ('sè','herself'),
              '3smn': ('sè','itself'), '3sfn': ('sè','itself'),  '3sp': ('Sè','Yourself'),
              '1p': ('noi','ourselves'), '2p': ('voi','yourselves'), '3p': ('sè','themselves'),'3pm': ('sè','themselves'),
              '3pmn': ('sè','themselves'), '3pf':  ('sè','themselves'), '3pfn':  ('sè','themselves'),
                     '3pp':  ('Sè','Yourselves(pl)') },

    
}                           
                                                                                          


def it_pronoun(kind,person,obj=False):
    if obj:
        return pronouns[kind][person][0][obj]
    else:
        return pronouns[kind][person][0]

def eng_pronoun(kind,person,obj_present=False):
    if obj_present:
        return pronouns[kind][person][2]
    else:
        return pronouns[kind][person][1]

def it_combine_dir_and_indir(indirect_pronoun,direct_pronoun):
    if indirect_pronoun[1] == 'i' and direct_pronoun in ['lo','la','La','li','le','Le','ne']:
        return indirect_pronoun[0]+'e '+ direct_pronoun
    elif indirect_pronoun in ['gli','le'] and direct_pronoun in ['lo','la','La','li','le','Le','ne']:
        return 'glie'+ direct_pronoun
    elif indirect_pronoun in ['Le'] and direct_pronoun in ['lo','la','li','le','ne']:
        return 'Glie'+ direct_pronoun
    else:
        return indirect_pronoun+' '+direct_pronoun
 
pronoun_persons = ['1s', '2s', '3sm', '3sf', '3smn', '3sfn','3sp', '1p', '2p', '3pm', '3pf', '3pmn', '3pfn','3pp' ]

pronoun_persons_human = ['1s', '2s', '3sm', '3sf','3sp', '1p', '2p', '3pm', '3pf', '3pp' ]

pronoun_persons_things = [ '3smn', '3sfn','3pmn', '3pfn' ]
                 
special_conj[('mio','pm')] = 'miei'
special_conj[('tuo','pm')] = 'tuoi'
special_conj[('suo','pm')] = 'suoi'
special_conj[('Suo','pm')] = 'Suoi'
special_conj['loro'] = 'loro'
special_conj['Loro'] = 'Loro'

poss_pronouns = \
              { '1s': ('mio','mine','my'),
                '2s': ('tuo', 'yours','your'),
                '3sm': ('suo', 'his','his'), 
                '3sf': ('suo', 'hers','her'), 
                '3smn': ('suo','its(m)','its(m)'), 
                '3sfn': ('suo', 'its(f)','its(f)'), 
                '3sp': ('Suo','Yours','Your'),
                '1p': ('nostro','ours','our'),
                '2p': ('vostro', 'yours(pl)','your(pl)'),
                '3pm': ('loro', 'theirs','their'),
                '3pf': ('loro', 'theirs','their'),
                '3pmn': ('loro', 'theirs','their'),
                '3pfn': ('loro','theirs','their'),
                '3pp': ('Loro', 'Yours(pl)','Your(pl)'),
                'proprio': ('proprio','own','own'),
                'altrui': ('altrui','somebody elses','somebody elses')                    
                    }

def it_poss_pronoun(person,noun,number):  
    return it_adj(poss_pronouns[person][0],noun,number+'d')

def eng_poss_pronoun(person,alone=False):  
    return poss_pronouns[person][alone and 2 or 1]

indef_pronouns = \
    {   'poco': {'s':'a little', 'p':'a few', 'prop':['noun']},
        'tanto': {'s': 'so much', 'p':'so many', 'prop':['noun'] },
        'troppo': {'s': 'too much', 'p':'too many', 'prop':['noun'] },
        'tutto': {'s': 'all the','su': 'all the', 'p':'all', 'prop': ['noun','art_on_noun'] }, 
        'ciascuno': {'s':'each', 'prop': ['noun'] },
        'qualche': {'s': 'some', 'prop': ['noun'] },
        'ogni': {'s': 'every', 'prop': ['noun'] },
        'ognuno': {'s': 'everybody', 'prop': [] },
        'nessuno': {'s':'no', 'sa': 'none', 'prop': ['noun']},
        'qualcuno':{'s':'someone', 'prop': [] },
        'niente':{'s':'nothing', 'prop': ['non'] },
        'nulla':{'s':'nothing', 'prop': ['non'] },
        'qualcosa':{'s':'something', 'prop': [] }
    }
# Note: su = singular uncountable, sa - singular alone (no noun)

def indef_pron_get_synonyms(pro):
    if pro in ['nulla','niente']:
        return ['nulla','niente']
    else:
        return [ pro ]
    
def indef_pron_can_take_noun(pro):
    return 'noun' in indef_pronouns[pro]['prop']

def indef_pron_has_p(pro):
    return 'p' in indef_pronouns[pro]

def indef_pron_needs_non(pro):
    return 'non' in indef_pronouns[pro]['prop']

def it_indef_pron(pro,noun,num):
    return it_adj(pro,noun,num[0])

def eng_indef_pron(pro,num):
    if num in indef_pronouns[pro]:
        return indef_pronouns[pro][num]
    else:
        return indef_pronouns[pro]['s']        
    
def it_indef_pron_noun(pro,nou,num):
    if 'art_on_noun' in indef_pronouns[pro]['prop']:
        return it_adj(pro,nou,num[0])+' '+it_noun(nou,num[0]+'d')
    else:
        return it_adj_noun(pro,nou,num[0])

def eng_indef_pron_noun(pro,noun,num):
    return indef_pronouns[pro][num]+' '+eng_noun(noun,num[0])

demon_pronouns = \
    { 'questo': {'s': 'this', 'p': 'these','prop':[]},
      'quello': {'s': 'that', 'p': 'those','prop':[]},
      'stesso': {'s': 'same', 'p': 'same','prop':['d']},
      'altro': {'s': 'other', 'p': 'other','prop':['d']},
      'certo': {'s': 'certain', 'p': 'certain','prop':['i']},
      'tale': {'s': 'such', 'p': 'such','prop':['eng_indef_art_on_noun']}
    }

def it_demon_pron(pro,noun,num):
    if 'i' in demon_pronouns[pro]['prop']:
         num = num+'i'
    elif 'd' in demon_pronouns[pro]['prop']:
        num = num+'d'
    return it_adj(pro,noun,num)

def eng_demon_pron(pro,num):
    if 'i' in demon_pronouns[pro]['prop']:
         num = num+'i'
    elif 'd' in demon_pronouns[pro]['prop']:
        num = num+'d'
    return eng_adj(demon_pronouns[pro][num[0]],num)

def it_demon_pron_noun(pro,noun,num):
    if 'i' in demon_pronouns[pro]['prop']:
        num = num+'i'
    elif 'd' in demon_pronouns[pro]['prop']:
        num = num+'d'
    return it_adj_noun(pro,noun,num)

def eng_demon_pron_noun(pro,noun,num):
    if 'eng_indef_art_on_noun' in demon_pronouns[pro]['prop'] and num == 's':
        return eng_adj(demon_pronouns[pro][num],num)+' '+eng_noun(noun,'si')
    if 'i' in demon_pronouns[pro]['prop']:
        num = num+'i'
    elif 'd' in demon_pronouns[pro]['prop']:
        num = num+'d'
    return eng_adj_noun(demon_pronouns[pro][num[0]],noun,num)

      

    
