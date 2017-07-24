# -*- coding: cp1252 -*-

from noun import special_conj

number_dict = \
            { 1: ('uno','prima','one','first'),
              2: ('due','secondo','two','second'),
              3: ('tre','terso','three','third') }

for n in number_dict:
    special_conj[number_dict[n][0]] = number_dict[n][0]
    
def it_number(n):
    return number_dict[n][0]

def it_ordinal(n):
    return number_dict[n][1]

def eng_number(n):
    return number_dict[n][2]

def eng_ordinal(n):
    return number_dict[n][3]
