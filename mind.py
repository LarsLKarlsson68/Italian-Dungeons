# -*- coding: cp1252 -*-

from verb import verbs, eng_verbs
from phrase import *

mind_verbs= {\
    'sperare': {'trans':'hope'},
    'avere_paura': {'trans':'fear'},
    'rimpiangere': {'trans':'regret', 'perfect':'rimpianto'},
    'sospettare':{'trans':'suspect'},
    'dubitare':{'trans':'doubt'},
    'concludere':{'trans':'conclude', 'perfect':'concluso'},
    'spiegare':{'trans':'explain'},
    'mentire':{'trans':'lie(untruth)'},
    'ingannare':{'trans':'deceive'},
    'incoraggiare':{'trans':'encourage'},
    'scoraggiare':{'trans':'discourage'},
    'fidare':{'trans':'trust'}, #si di    
    'dare_la colpa':{'trans':'blame'}, #di
    'perdonare':{'trans':'forgive'},
    'spaventare':{'trans':'scare'},
    'inventare':{'trans':'invent'},
    'domandare':{'trans':('request','wonder')}, # wonder with 'si'
    'preoccupare':{'trans':'worry'}, # si
    'lamentare':{'trans': 'complain'}, # si
    'apprezzare':{'trans': 'appreciate'},
    'desiderare':{'trans': 'wish_for'},
    "sognare":{'trans':'dream'},
    'piangere':{'trans':('weep','mourn'), 'perfect': 'pianto'},
    'interessare':{'trans':'care_about'}, #si di
    'imbrogliare':{'trans':'confuse(sb)'}, # to confuse somebody
    'confondere':{'trans':'confuse(mistake)', 'perfect':'confuso'},  #confuse x and y
    'imaginare':{'trans':'imagine'},
    'dispiacere':{'trans':'displease'},
    "scegliere":{'trans': 'choose', 'present': {'1s': 'sceglo', '3p': 'sceglono'}, 'perfect': 'scelto' }    

}

verbs.update(mind_verbs)

eng_mind_verbs= {\
    'displease': {},
    'request': {},
    'hope': {},
    'fear':{},
    'regret':{},
    'suspect':{},
    'doubt':{},
    'conclude':{},
    'explain':{},
    'lie(untruth)':{},
    'deceive':{},
    'encourage':{},
    'discourage':{},
    'trust':{},
    'blame':{},
    'forgive':{},
    'scare':{},
    'invent':{},
    'wonder':{},
    'worry':{},
    'complain':{},
    'appreciate':{},
    'wish':{},
    'dream':{},
    'weep':{'imperfect':'wept','perfect':'wept'},
    'mourn':{},
    'care':{},
    'confuse(sb)':{},
    'confuse(mistake)':{},
    'imagine': {},
    'choose': {'imperfect':'chose','perfect':'chosen'}, 
}

eng_verbs.update(eng_mind_verbs)

mind_nouns= {\
    'lo speranza': 'hope',
    'la paura': 'fear',
    'il rimpianto': 'regret',
    'il dubbio': 'doubt',
    'la certezza':'certainty',
    'la prova':'proof',
    'la preoccupazione':'worry',
    'la conclusione':'conclusion',
    'la fiducia': 'trust',
    "l'amore": 'love',
    "l'odio":'hate',
    "il sogno":'dream',
    'il dolore':'sorrow',
    'la felicità':'happiness',
    'la fantasia':'fantasy',
    'la immaginazione':'imagination',
    'la gioia':'joy',
    'la rabbia':'anger',
    'la colpevolezza':'guilt',
    'la bugia': 'lie',
    'la verità': 'truth',
    'la consapevolezza':'knowledge',
    'la ignoranza':'ingorance',
    'la confusione':'confusion',
    'la mente':'mind',
    'il pensiero':'thought',
    "l'idea":'idea',
    'la ragione':'reason',
    'il piacere':'pleasure',
    "l'anima":"soul"
    
}

noun_dict.update(mind_nouns)

extra_nouns={\
    'il amico':'friend',
    'la amica':'friend',
    'il sconosciuto':'stranger',
    'la sconosciuta':'stranger',
    'il conoscente':'acquaintance',
    'la conoscente':'acquaintance',    
    'il nemico':'enemy',
    'la nemica':'enemy'
                }
noun_dict.update(extra_nouns)


mind_adjs={\
    'felice':'happy',
    'triste':'sad',
    'buono':'good',
    'cattivo':'bad',
    'gentile':'kind',
    'spiacente':'sorry',
    'lieto':'glad',
    'arrabbiato':'angry',
    'furioso':'angry',
    'intelligente':'intelligent',
    'stupido':'stupid',
    'saggio':'wise',
    'ignorante':'ignorant',
    'spasso':'fun',
    'divertimento':'fun',
    'noioso':'boring',
    'vero':'true',
    'falso':'false',
    'calmo':'calm',
    'nervoso':'nervous',
    'onesto':'honest',
    'sincero':'honest',
    "annoiato":"bored",
    "fiducioso":"confident",
    "fiero":"proud",
    "timido":"shy",
    "turbato":"upset"
}

adj_dict.update(mind_adjs)

mind_nouns_keys = list(mind_nouns.keys())
extra_nouns_keys = list(extra_nouns.keys())
mind_adjs_keys = list(mind_adjs.keys())

q1 = phrase(['amare','odiare','conoscere','perdonare','ingannare',
           'incoraggiare','scoraggiare','imbrogliare'],
              neg=[True,False,False,False],
             person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],
        dobj=[dir_pronoun_phrase(['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3p'])])

q2 = phrase(['fidarsi0','dare_la colpa','interessarsi0'],
              neg=[True,False,False,False],
             person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],
            iobj=[indir_pronoun_phrase('di',['1s','2s','3sm','3sf', '1p','2p','3p','3p'],True)])

q3 = noun_phrase(mind_nouns_keys)

q3b = phrase(conj='che',verb="essere",person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],pred=mind_adjs_keys,
             tempus=['subjunctive present'], eng_help='[I believe] ')

q4 = phrase(conj='che',verb=['andare','venire','parlare','capire','sapere','piangere(1)'],
                                  neg=[True,False,False,False],
                                  person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],
                                 tempus=['subjunctive present','subjunctive present','subjunctive perfect'], eng_help='[I believe] ')



q5 = phrase(['sperare','desiderare','preferire','preoccuparsi0','credere','pensare',
             'dubitare','sospettare','avere_paura','piangere(1)', 'lamentarsi0',
             'apprezzare','rimpiangere'],
                     neg=[True,False,False,False],
                     person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],
                     post=[phrase(conj='che',verb=['essere'],pred=mind_adjs_keys,
                                  neg=[True,False,False,False],
                                  person=['1s','2s','3sm','3sf','1p','2p','3p','3p'],
                                  tempus=['subjunctive present','subjunctive perfect','future'])]+\
                          [phrase(conj='che',verb=['andare','venire','parlare','capire','sapere','piangere(1)'],
                                  neg=[True,False,False,False],
                                  person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],
                                 tempus=['subjunctive present','subjunctive perfect','future'])                                 
                            ])

q6 = phrase(['sapere','concludere','spiegare','capire','ricordare',
                 'dimenticare','inventare'],
                 neg=[True,False,False,False],
                 person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],
                 post=[phrase(conj='che',verb=['essere'],pred=mind_adjs_keys,
                              neg=[True,False,False,False],
                              person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],
                              tempus=['present','perfect','future']),
                      phrase(conj='che',verb=['andare','venire','parlare','capire','sapere','piangere(1)'],
                                          neg=[True,False,False,False],
                                          person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],
                                         tempus=['present','perfect','future'])])

q7 = phrase(['domandarsi0(1)'],
              neg=[True,False,False,False],
              person=['1s','2s','3sm','3sf','1p','2p','3p','3p'],
              post=[phrase(conj='se',verb=['essere'],pred=mind_adjs_keys,
                                  neg=[True,False,False,False],
                                  person=['1s','2s','3sm','3sf','1p','2p','3p','3p'],
                                  tempus=['subjunctive present','subjunctive perfect','future']),
            phrase(conj='se',verb=['andare','venire','parlare','capire','sapere','piangere(0)'],
                                      neg=[True,False,False,False],
                                      person=['1s','2s','3sm','3sf','3sp', '1p','2p','3p','3p'],
                                     tempus=['subjunctive present','subjunctive perfect','future']) ])

q8 = phrase(['piacere','dispiacere'],
                  neg=[True,False,False,False],
                  person=['3smn'],
                  iobj=[ indir_pronoun_phrase('a',person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],eng_no_prep=True) ],
                  post=[phrase(conj='che',verb=['andare','venire','parlare','capire','sapere'],
                                          neg=[True,False,False,False],
                                          person=['1s','2s','3sm','3sf', '1p','2p','3p','3p'],
                                         tempus=['subjunctive present','subjunctive perfect','future']) ])

