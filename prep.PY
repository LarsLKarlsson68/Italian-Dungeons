# -*- coding: latin_1 -*-

prepositions = \
    {
        'in' : ('in(0)','to(0)','into'),
        'su' : ('on','over','up'),
        'a': ('to(1)', 'at','in(1)'),
        'da': ('from','by','off','at(1)','to(2)','since'),
        'di': ('of','about','from(1)'),
        'con': 'with',
        'per': 'for',
        'contro': 'against',
        'dentro' : 'into',
        'fuori_di': 'out of',
        'sopra': ('above','over'),
        'sotto': ('under','below'),
        'giù per': 'down',
        'accanto_a': 'beside',
        'tra': ('between','among','in(2)'),
        'fra': ('between','among','in(2)'),
        'davanti_a': 'in front of',
        'dietro':'behind',
        'vicino_a': 'near',
        'attraverso': ('through','across'),
        'verso': 'towards',
        'lungo': 'along',
        'oltre': 'past',
        'intorno_a': 'around',
        'prima_di': 'before',
        'dopo': 'after',
        'durante': 'during',
        'nel corso di': 'during',
        'fino_a': 'until'
 } 

    
prep_patterns = { 'il': 'l', 'lo': 'llo', "l'": "ll'", 'i ':'i ', 'gli':'gli',
                  'la': 'lla', 'le': 'lle' }  
prep_change = {'in':'ne', 'di':'de' }
                
        
def it_prep_noun(pre,noun):
    if '_' in pre:
        prefix = pre.split('_')[0]+' '
        pre = pre.split('_')[1]
    else:
        prefix = ''
    if pre in ['su','a','da','di','in','be','que']:
        if noun[:2] in prep_patterns:
            if pre in prep_change:
                pre = prep_change[pre]
            return prefix+pre+prep_patterns[noun[:2]]+noun[2:]
        elif noun[:3] in prep_patterns:
            if pre in prep_change:
                pre = prep_change[pre]
            return prefix+pre+prep_patterns[noun[:3]]+noun[3:]
    return prefix+pre+' '+noun

