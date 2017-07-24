# -*- coding: cp1252 -*-

from prep import it_prep_noun

special_conj = dict()
eng_special_conj = dict()

def it_noun(noun,kind):
#    if noun[:3] not in ['il ','lo ','la '] and noun[:2] not in ["l'"]:
    if '_' in noun:
        post =  ' '+noun.split('_')[1]
        noun = noun.split('_')[0]
    else:
        post=''
    if noun[0].isupper():
        return noun+post
    noun, gender = noun_gender(noun)
    if kind == 'sd':
        return noun_sd(noun,gender)+post
    elif kind == 'si':
        return noun_si(noun,gender)+post
    elif kind == 's':
        return noun_s(noun,gender)+post
    elif kind == 'pd':
        return noun_pd(noun,gender)+post
    elif kind == 'pi' or kind == 'p':
        return noun_p(noun,gender)+post
    else:
        return '*error*'

def eng_noun(noun,kind):  # Add translation here later
    if '_' in noun:
        post =  ' '+noun.split('_')[1]
        noun = noun.split('_')[0]
    else:
        post=''
    if noun[0].isupper():
        return noun+post
    if kind == 'sd':
        return 'the '+noun+post
    elif kind == 'si':
        if noun[0] in 'aeiou':
            return 'an '+noun+post
        else:
            return 'a '+noun+post
    elif kind == 's':
        return noun+post
    elif kind == 'pd':
        return 'the '+eng_noun(noun,'p')+post
    elif kind == 'pi' or kind == 'p':
        if noun in eng_special_conj:
            return eng_special_conj[noun]+post
        elif noun[-1] in 'sz' or noun[-2:] in ['sh','ch']:
            return noun+'es'+post
        elif noun[-1] in 'f':
            return noun[:-1]+'ves'+post
        elif noun[-1] in 'y' and noun[-2] not in 'aeiou':
            return noun[:-1]+'ies'+post        
        else:
            return noun+'s'+post
    else:
        return '*error*'

def it_adj_noun(adj,noun,kind):
    if '_' in noun:
        post =  ' '+noun.split('_')[1]
        noun = noun.split('_')[0]
    else:
        post=''
    noun, gender = noun_gender(noun)
    if kind == 'sd':
        return adj_noun_sd(adj,noun,gender)+post
    elif kind == 'si':
        return adj_noun_si(adj,noun,gender)+post
    elif kind == 's':
        return adj_noun_s(adj,noun,gender)+post
    elif kind == 'pd':
        return adj_noun_pd(adj,noun,gender)+post
    elif kind == 'pi' or kind == 'p':
        return adj_noun_p(adj,noun,gender)+post
    else:
        return '*error*'

def eng_adj_noun(adj,noun,kind):
    if '_' in noun:
        post =  ' '+noun.split('_')[1]
        noun = noun.split('_')[0]
    else:
        post=''
    return eng_adj(adj,kind)+' '+eng_noun(noun,kind[0])+post

def it_adj(adj,noun,kind):
    noun, gender = noun_gender(noun)
    if kind == 'sd':
        return adj_sd(adj,gender)
    elif kind == 'si':
        return adj_si(adj,gender)
    elif kind == 's':
        return adj_s(adj,gender)
    elif kind == 'pd':
        return adj_pd(adj,gender)
    elif kind == 'pi' or kind == 'p':
        return adj_p(adj,gender)
    else:
        return '*error*'

def eng_adj(adj,kind):
    if kind[0] == 's':
        return eng_noun(adj,kind)
    elif kind == 'pd':
        return 'the '+adj
    else:
        return adj

def noun_s(noun,gender):
    if noun[:2] == "l'":
        return noun[2:]
    else:    
        return noun[3:]
    
def noun_sd(noun,gender):
    return noun

noun_si_pattern = { 'il': 'un', 'lo': 'uno', "l'": "un'", 'la': 'una' }

def noun_si(noun,gender):
    return noun_si_pattern[noun[0:2]]+noun[2:]


noun_pd_pattern = { 'il': 'i', 'lo': 'gli', "l'": "gli ", 'la': 'le' }

def plural_ending(word,gender):
    if word in special_conj:
        word = special_conj[word]
    elif (word,'p'+gender) in special_conj:
        word = special_conj[(word,'p'+gender)]        
    elif word[-1] in 'oa' and gender == 'f':
        if word[-2] in 'cg':
            word = word[:-1]+'he'
        else:    
            word = word[:-1]+'e'
    elif word[-1] in 'oe':
        if word[-1]=='o' and word[-2] in 'cg':
            word = word[:-1]+'hi'
        elif word[-2] == 'i':    
            word = word[:-1]
        else:
            word = word[:-1]+'i'
    return word            
    
def noun_pd(noun,gender):
    return noun_pd_pattern[noun[0:2]]+plural_ending(noun[2:],gender)

def noun_p(noun,gender):
    if noun[:2] == "l'":
        return plural_ending(noun[2:],gender)
    else:
        return plural_ending(noun[3:],gender)



def noun_gender(noun):
    if noun[-3:] in ['(m)','(f)']:
        gender = noun[-2]
        noun = noun[:-3]
    elif noun[-1] == 'a' or noun[:2] == 'la':
        gender='f'
    else:
        gender='m'
    return noun, gender

    
def adj_s(adj,gender,before=False):
    if adj in special_conj:
        adj = special_conj[adj]
    elif adj[-1] == 'o' and gender == 'f':
        adj = adj[:-1]+'a'
    return adj       
    
def adj_p(adj,gender,before=False):
    return plural_ending(adj,gender)       

def adj_noun_s(adj,noun,gender):
    if len(adj) > 4 and adj[-4:] == 'ello':
        return it_prep_noun(adj[:-3],noun)
    elif len(adj) > 3 and adj[-3:] == 'uno':
        return adj[:-3]+noun_si(noun,gender)
    elif len(adj) > 4 and adj[-4:] == 'uono':
        return adj[:-2]+noun_si(noun,gender)[1:]
    else:
        return adj_s(adj,gender,True)+' '+noun_s(noun,gender)

def adj_noun_p(adj,noun,gender):
    if len(adj) >= 4 and adj[-4:] == 'ello':
        return it_prep_noun(adj[:-3],noun_pd(noun,gender))        
    else:
        return adj_p(adj,gender,True)+' '+noun_p(noun,gender)
 
def adj_noun_sd(adj,noun,gender):
    return art_sd(adj,gender)+adj_noun_s(adj,noun,gender)

def adj_sd(adj,gender):
    return art_sd(adj,gender)+adj_s(adj,gender)

def art_sd(adj,gender):
    if adj[0] in 'aeiou':
        art="l'"
    elif gender == 'm':
        if adj[0] == 'z' or adj[0] == 's' and adj[1] not in 'aeiou':
            art='lo '
        else:
            art='il '
    else:
        art = 'la '
    return art

def adj_noun_si(adj,noun,gender):
    return art_si(adj,gender)+adj_noun_s(adj,noun,gender)

def adj_si(adj,gender):
    return art_si(adj,gender)+adj_s(adj,gender)

def art_si(adj,gender):
    if adj[0] in 'aeiou':
        art="un'"
    elif gender == 'm':
        if adj[0] == 'z' or adj[0] == 's' and adj[1] not in 'aeiou':
            art='uno '
        else:
            art='un '
    else:
        art = 'una '
    return art

def adj_noun_pd(adj,noun,gender):
    return art_pd(adj,gender)+adj_noun_p(adj,noun,gender)

def adj_pd(adj,gender):
    return art_pd(adj,gender)+adj_p(adj,gender)

def art_pd(adj,gender):
    if gender == 'm':
        if adj[0] in 'aeiouz' or adj[0] == 's' and adj[1] not in 'aeiou':
            art='gli '
        else:
            art='i '
    else:
        art = 'le '
    return art

      

      

