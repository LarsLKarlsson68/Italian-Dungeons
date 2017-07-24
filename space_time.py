# -*- coding: cp1252 -*-

from verb import verbs, eng_verbs
from phrase import adj_dict, noun_dict, adverb_dict

space_adverbs = \
    {'fuori': 'outside',
     'dentro': 'inside',
     'a sinistra': 'to the left',
     'a destra': 'to the right',
     'su': 'up',
     'giù': 'down',
     'soprosotta': 'upside down',
     'in mezzo': 'between',
     'dietro':'behind',
     'avanti': ('ahead','forwards'),
     'indietro':'backwards',
     'vicino': 'near',
     'lontano': 'far',
     'attraverso': ('through','across'),
     'dove': 'where',
     'altrove': 'elsewhere',
     'da qualche parte': 'somewhere',
     'da qualsiasi parte': 'anywhere',
     'dovunque': 'anywhere',
     'dappertutto' : 'everywhere',
     'in ogni luogo': 'everywhere',
     'da nessuna parte': 'nowhere',
     'qui': 'here',
     'qua': 'here',
     'lì': 'there',
     'là': 'there',
     'in macchina':'by car',
     'in auto':'by car',
     'in treno':'by train',
     'in autobus':'by bus',
     'in barca':'by boat',
     'in bicicletta':'by bicycle',   
     'in barca':'by boat',
     'a piedi':'by foot',
     'a cavallo':'by horse',
     'rapido':'fast',
     'svelto':'fast',
     'veloce':'fast',
     'lento':'slowly'
     }
     
     
space_adjs = {
    'vicino':'near',
    'lontano':'distant',
    'alto':'high',
    'basso':'low',
    'lungo':'long',  
    'corto':'short',
    'largo':'wide',
    'stretto':'narrow',
    'profondo':'deep',
    'poco profondo':'shallow',
    'grande':'large',
    'piccolo':'small',
    'rapido':'fast',
    'svelto':'fast',
    'veloce':'fast',
    'lento':'slow',
    'interno':'inner',
    'esterno':'outer',
    'superiore':'upper',
    'inferiore':'lower'
    }
     
space_nouns = { "l'esterno":'outside',
                "l'interno":'inside',
                'la sopra':'top',
                'il fondo':'bottom',
                'la superfice':'surface',
                'la lungezza':'length',
                "l'altezza":'height',
                'la largezza':'width',
                'i dimensioni':'size',
                'la profondità':'depth',
                'la distanza':'distance',
                'la velocità':'speed',
                'il lato':'side',
                "l'orlo":('border','rim'),  
                'il margine':'border',
                'la frontiera':'border',
                'il centro':'center',
                'il mezzo':'middle',
                "l'incrocio":'crossing',
                'la via':('way','road'), 
                'la strada':('street'),
                'il passagio':'passage',
                'il sentiero':'path',
                'la parte':'direction',
                'la terra':'ground',
                'il suolo':'ground',
                'il terreno':'terrain',  
                'il cielo':'sky',
                "l'aria":'air',
                "l'acqua":'water',
                'il mare':'sea',
                'il lago':'lake',  
                'il fiume':'river',
                "l'isola":'island',
                'la montagna':'mountain',
                'la collina':'hill',
                'la valle':'valley',
                'la pianura':'plain',
                'la foresta':'forest',
                'la costa':'coast',
                'la spiagga':'beach',
                'la terra':'land',
                'il deserto':'desert',
                'la prateria':'grassland',
                'la città':'town',
                'la campagna':'countryside',
                'il paese':'country',
                'la casa': 'house',
                'lo spazio': 'space',
                'il pianeta(m)':'planet',
                'la stella':'star',
                'il sole':'sun',
                'la luna':'moon',
                'il viaggo':'journey',
                "l'itinerario":'route',
                'il posto':'place',
                'il luogo':'place',
                "l'area":'area',
                'la zona':'zone',
                "l'angelo":'corner',
                'la curva':'curve',
                'il ponte':'bridge',
                'la stanza':'room',
                'la camera':'room',
                'il cinema':'cinema',
                'la chiesa':'church',
                "l'ufficio":'office',
                "l'ospitale(m)":'hospital',
                'la piazza':'square'

             } 

space_verbs = \
{   'volare': {'trans':'fly'},
    'decollare':{'trans':'take_off'},
    'atterrare':{'trans':'land'},
    'nuotare':{'trans':'swim'},
    'tuffarsi0':{'trans':'dive'},
    'tuffare':{'trans':'plunge'},
    'galleggiare':{'trans':'float'},
    'affondare':{'trans':'sink'},
    'navigare':{'trans':'sail'},
    'salire':{'trans':('climb','go_up'), 'present':{'1s':'salgo', '3p':'salgono'}},
    'scalare':{'trans':'climb'},
    'saltare':{'trans':'jump','perfect':'salto'}, #CHECK!
    'scendere':{'trans':'go_down', 'perfect':'sceso'},
    'rotolare':{'trans':'roll'},
    'avvicinarsi0':{'trans':'approach'},
    'avvicinare':{'trans': 'approach'},
    'cavalcare':{'trans':'ride'},
    'guidare':{'trans':'drive'},
    'viaggare':{'trans':'travel'},
    'attraversare':{'trans':'cross'},
    'passare':{'trans':'pass'},
    'esplorare':{'trans':'explore'},
    'strisciare':{'trans':'crawl'}
}

eng_space_verbs={'fly':{'imperfect':'flew','perfect':'flown'},
                 'land':{}, 'swim':{'imperfect':'swam','perfect':'swum'},
                 'dive':{}, 'plunge':{},'float':{}, 'sink':{},'sail':{},
                 'climb':{}, 'roll':{}, 'approach':{}, 'ride':{}, 'drive':{},
                 'travel':{}, 'cross':{}, 'pass':{}, 'explore': {},
                 'crawl':{} }

    
time_adverbs = \
    {'sempre': 'always',
     'non mai': 'never',
     'mai':'ever',
     'qualche volta': 'sometimes',
     'spesso': 'often',
     'raramente': 'seldom',
     'una volta': 'once',
     'due volte': 'twice',
     'ancora':('again','still','yet'),
     'non ancora':'not yet',
     'già':'already',
     'piu':'still',
     'non piu':'no more',
     'ora': 'now',
     'adesso': 'now',
     'quando': 'when',
     'tardi': 'late',
     'piu tardi': 'later',
     'prima': ('before','earlier'),
     'dopo': 'after',
     'allo stesso tempo': 'at the same time',
     'presto': ('soon','early'),
     'fra poco': 'soon',
     'appena': 'just',
     'di solito': 'usually',
     'finalmente': 'eventually',
     'per ultimo': 'last',
     'per sempre': 'forever',
     'oggi' : 'today',
     'ieri': 'yesterday',
     'domani' : 'tomorrow',
     'stanotte': 'tonight',
     'stasera': 'this evening',
     'stamattina': 'this morning',
     'fa':'ago'
     }
time_adjs = {
    'primo': 'first',
    'secondo': 'second',
    'ultimo': 'last',
    'precoce': 'early',
    'anticipato': 'early',
    'in ritardo': 'late',
    'tardo': 'late',
    'passato': 'past',
    'presente': 'present',
    'futuro': 'future',
    'precedente':'previous',
    'prossimo':'next'
    }
time_nouns= {
    'il passato': 'past',
    'il presente': 'present',
    'il futuro': 'future',
    'il giorno':'day',
    'la notte':'night',
    'la sera': 'evening',
    'la mattina': 'morning',
    'il mezzogiorno':'midday',
    'la mezzanotte':'midnight',    
    "l'ora": 'hour',
    'il minuto': 'minute',
    'la settimana': 'week',
    'il mese': 'month',
    'la stagione': 'season',
    "l'estate(f)": 'summer',
    "l'autumno": 'autumn',
    "l'inverno": 'winter',
    'la primavera': 'spring',
    "l'anno": 'year',
    'il secolo': 'century',
    'il tempo': ('time','weather'),
    'la data': 'date'
    }
time_verbs= {
    'cominciare': {'trans': 'begin' },
    'riposare': {'trans': 'rest' },
    'svegliare': {'trans': 'wake_up'},
    'addormentare': {'trans': 'fall_asleep'}
    }

eng_time_verbs = {
    'begin': {'imperfect':'began', 'perfect': 'begun', 'ongoing': 'beginning'},
    'wake': {'imperfect':'woke', 'perfect': 'woken'},
    'rest':{}
    }

space_time_names = \
                 { 'Paolo': ('Paolo',"Paolo's"),
                   'Maria': ('Maria',"Maria's"),
                   'Roma': 'Rome',
                   'Capri': 'Capri',
                   'Milano':'Milan',
                   'Italia':'Italy',
                   'Sicilia':'Sicily' }

adj_dict.update(space_adjs)
adj_dict.update(time_adjs)
adverb_dict.update(space_adverbs)
adverb_dict.update(time_adverbs)
noun_dict.update(space_nouns)
noun_dict.update(time_nouns)
noun_dict.update(space_time_names)
verbs.update(space_verbs)
eng_verbs.update(eng_space_verbs)
verbs.update(time_verbs)
eng_verbs.update(eng_time_verbs)
