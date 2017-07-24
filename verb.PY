# -*- coding: latin_1 -*-

from random import *
from pronoun import it_pronoun, eng_pronoun

verbs = \
{
    'essere': {'trans': 'be', 'strans': 'vara',
              'present': {'1s': 'sono', '2s': 'sei', '3s': 'è', '1p': 'siamo', '2p': 'siete', '3p': 'sono' },
              'imperfect': {'1s': 'ero', '2s': 'eri', '3s': 'era', '1p': 'eravamo', '2p': 'eravate', '3p': 'erano' },
              'future': {'1s': 'sarò', '2s': 'sarai', '3s': 'sarà', '1p': 'saremo', '2p': 'sarete', '3p': 'saranno' },
          #    'conditional': {'1s': 'sarei', '2s': 'saresti', '3s': 'sarebbe', '1p': 'saremmo', '2p': 'sareste', '3p': 'sarebbero' },
              'imperative': {'2s': 'sii', '3s': 'sia', '1p': 'siamo', '2p': 'siate', '3p': 'siano' },
              'subjunctive present': {'1s': 'sia', '2s': 'sia', '3s': 'sia', '1p': 'siamo', '2p': 'siate', '3p': 'siano' },
              'subjunctive imperfect': {'1s': 'fossi', '2s': 'fossi', '3s': 'fosse', '1p': 'fossimo', '2p': 'foste', '3p': 'fossero' },
              'perfect': 'stato', 'aux': 'essere' 
              },                          
    'avere': {'trans': 'have', 'strans': 'ha',
              'present': {'1s': 'ho', '2s': 'hai', '3s': 'ha', '1p': 'abbiamo', '2p': 'avete', '3p': 'hanno' },
              'future': {'1s': 'avrò', '2s': 'avrai', '3s': 'avrà', '1p': 'avremo', '2p': 'avrete', '3p': 'avranno' },
#              'conditional': {'1s': 'avrei', '2s': 'avresti', '3s': 'avrebbe', '1p': 'avremmo', '2p': 'avreste', '3p': 'avrebbero' },
              'imperative': {'2s': 'abbi', '3s': 'abbia', '1p': 'abbiamo', '2p': 'abbiate', '3p': 'abbiano' },
              'subjunctive present': {'1s': 'abbia', '2s': 'abbia', '3s': 'abbia', '1p': 'abbiamo', '2p': 'abbiate', '3p': 'abbiano' },
              'perfect': 'avuto' 
              },                          
    'dovere': {'trans': 'have_to', 'strans': 'vara_tvungen att',
              'present': {'1s': 'devo', '2s': 'devi', '3s': 'deve', '1p': 'dobbiamo', '2p': 'dovete', '3p': 'devono' },
              'future': {'1s': 'dovrò', '2s': 'dovrai', '3s': 'dovrà', '1p': 'dovremo', '2p': 'dovrete', '3p': 'dovranno' },
#              'conditional': {'1s': 'dovrei', '2s': 'dovresti', '3s': 'dovrebbe', '1p': 'dovremmo', '2p': 'dovreste', '3p': 'dovrebbero' },
              'perfect': 'dovuto', 'prep': '' 
              },                          
    'potere': {'trans': 'be able to', 'strans': 'kunna',
              'present': {'1s': 'posso', '2s': 'puoi', '3s': 'puo', '1p': 'possiamo', '2p': 'potete', '3p': 'possono' },
              'future': {'1s': 'potrò', '2s': 'potrai', '3s': 'potrà', '1p': 'potremo', '2p': 'potrete', '3p': 'potranno' },
#              'conditional': {'1s': 'potrei', '2s': 'potresti', '3s': 'potrebbe', '1p': 'potremmo', '2p': 'potreste', '3p': 'potrebbero' },
              'perfect': 'potuto',  'prep': ''
              },
    'sapere': {'trans': ('know', 'know_how to'),  'strans': 'veta',
              'present': {'1s': 'so', '2s': 'sai', '3s': 'sa', '1p': 'sappiamo', '2p': 'sapete', '3p': 'sanno' },
              'future': {'1s': 'saprò', '2s': 'saprai', '3s': 'saprà', '1p': 'sapremo', '2p': 'saprete', '3p': 'sapranno' },
#              'conditional': {'1s': 'saprei', '2s': 'sapresti', '3s': 'saprebbe', '1p': 'sapremmo', '2p': 'sapreste', '3p': 'saprebbero' },
              'imperative': {'2s': 'sappi', '3s': 'sappia', '1p': 'sappiamo', '2p': 'sappiate', '3p': 'sappiano' },
              'subjunctive present': {'1s': 'sappia', '2s': 'sappia', '3s': 'sappia', '1p': 'sappiamo', '2p': 'sappiate', '3p': 'sappiano' },
              'perfect': 'saputo','prep': '' 
              },                          
    'volere': {'trans': 'want', 'strans': 'vilja',
              'present': {'1s': 'voglio', '2s': 'vuoi', '3s': 'vuole', '1p': 'vogliamo', '2p': 'volete', '3p': 'vogliono' },
              'future': {'1s': 'vorrò', '2s': 'vorrai', '3s': 'vorrà', '1p': 'vorremo', '2p': 'vorrete', '3p': 'vorranno' },
#              'conditional': {'1s': 'vorrei', '2s': 'vorresti', '3s': 'vorrebbe', '1p': 'vorremmo', '2p': 'vorresti', '3p': 'vorrebbero' },
              'imperative': {'2s': 'vogli', '3s': 'voglia', '1p': 'vogliamo', '2p': 'vogliate', '3p': 'vogliano' },
              'perfect': 'voluto', 'prep': '' 
              },                          
    'dare': {'trans': 'give', 'strans': 'ge',
              'present': {'1s': 'do', '2s': 'dai', '3s': 'da', '1p': 'diamo', '2p': 'date', '3p': 'danno' },
              'future': {'1s': 'darò', '2s': 'darai', '3s': 'darà', '1p': 'daremo', '2p': 'darete', '3p': 'daranno' },
#              'conditional': {'1s': 'darei', '2s': 'daresti', '3s': 'darebbe', '1p': 'daremmo', '2p': 'dareste', '3p': 'darebbero' },
              'imperative': {'2s': 'dà', '3s': 'dia', '1p': 'diamo', '2p': 'date', '3p': 'diano' },
              'subjunctive present': {'1s': 'dia', '2s': 'dia', '3s': 'dia', '1p': 'diamo', '2p': 'diate', '3p': 'diano' },
              'subjunctive imperfect': {'1s': 'dessi', '2s': 'dessi', '3s': 'desse', '1p': 'dessimo', '2p': 'deste', '3p': 'dessero' },
               'perfect': 'dato' 
              },                          
    'stare': {'trans': 'stay', 'strans': 'befinna',
              'present': {'1s': 'sto', '2s': 'stai', '3s': 'sta', '1p': 'stiamo', '2p': 'state', '3p': 'stanno' },
              'future': {'1s': 'starò', '2s': 'starai', '3s': 'starà', '1p': 'staremo', '2p': 'starete', '3p': 'staranno' },
#              'conditional': {'1s': 'starei', '2s': 'staresti', '3s': 'starebbe', '1p': 'staremmo', '2p': 'stareste', '3p': 'starebbero' },
              'imperative': {'2s': 'stà', '3s': 'stia', '1p': 'stiamo', '2p': 'state', '3p': 'stiano' },
             'subjunctive present': {'1s': 'stia', '2s': 'stia', '3s': 'stia', '1p': 'stiamo', '2p': 'stiate', '3p': 'stiano' },
              'subjunctive imperfect': {'1s': 'stessi', '2s': 'stessi', '3s': 'stesse', '1p': 'stessimo', '2p': 'steste', '3p': 'stessero' },
               'perfect': 'stato', 'aux': 'essere', 'prep': 'a' 
              },                          
    'fare': { 'trans': ('do', 'make'), 'strans': 'göra',
              'present': {'1s': 'faccio', '2s': 'fai', '3s': 'fa', '1p': 'facciamo', '2p': 'fate', '3p': 'fanno' },
              'imperfect': {'1s': 'facevo', '2s': 'facevi', '3s': 'faceva', '1p': 'facevamo', '2p': 'facevate', '3p': 'facevano' },
              'future': {'1s': 'farò', '2s': 'farai', '3s': 'farà', '1p': 'faremo', '2p': 'farete', '3p': 'faranno' },
#              'conditional': {'1s': 'farei', '2s': 'faresti', '3s': 'farebbe', '1p': 'faremmo', '2p': 'fareste', '3p': 'farebbero' },
              'imperative': {'2s': 'fà', '3s': 'faccia', '1p': 'facciamo', '2p': 'fate', '3p': 'facciano' },
              'perfect': 'fatto', 'prep': '' 
              },                          
    'andare': {'trans': 'go', 'strans': 'gå',
              'present': {'1s': 'vado', '2s': 'vai', '3s': 'va', '1p': 'andiamo', '2p': 'andate', '3p': 'vanno' },
              'future': {'1s': 'andrò', '2s': 'andrai', '3s': 'andrà', '1p': 'andremo', '2p': 'andrete', '3p': 'andranno' },
#              'conditional': {'1s': 'andrei', '2s': 'andresti', '3s': 'andrebbe', '1p': 'andremmo', '2p': 'andreste', '3p': 'andrebbero' },
              'subjunctive present': {'1s': 'vada', '2s': 'vada', '3s': 'vada', '1p': 'andiamo', '2p': 'andiate', '3p': 'vadano' },
              'imperative': {'2s': 'và', '3s': 'vada', '1p': 'andiamo', '2p': 'andate', '3p': 'vadano' },
              'perfect': 'andato', 'aux': 'essere', 'prep': 'a' 
              },                          
    'dire': {'trans': ('say','tell'), 'strans': 'säga',
              'present': {'1s': 'dico', '2s': 'dici', '3s': 'dice', '1p': 'diciamo', '2p': 'dite', '3p': 'dicono' },
              'future': {'1s': 'dirò', '2s': 'dirai', '3s': 'dirà', '1p': 'diremo', '2p': 'direte', '3p': 'diranno' },
              'imperfect': {'1s': 'dicevo', '2s': 'dicevi', '3s': 'diceva', '1p': 'dicevamo', '2p': 'dicevate', '3p': 'dicevano' },
##              'conditional': {'1s': 'direi', '2s': 'diresti', '3s': 'direbbe', '1p': 'diremmo', '2p': 'direste', '3p': 'direbbero' },
              'imperative': {'2s': 'dì', '3s': 'dica', '1p': 'diciamo', '2p': 'dite', '3p': 'dicano' },
              'perfect': 'detto' 
              },                          
    'vedere': {'trans': 'see', 'strans': 'se',
              'future': {'1s': 'vedrò', '2s': 'vedrai', '3s': 'vedrà', '1p': 'vedremo', '2p': 'vedrete', '3p': 'vedranno' },
#              'conditional': {'1s': 'vedrei', '2s': 'vedresti', '3s': 'vedrebbe', '1p': 'vedremmo', '2p': 'vedreste', '3p': 'vedrebbero' },
              'perfect': 'visto', 'prep': '' 
              },
    'venire': {'trans': 'come', 'strans': 'komma',
              'present': {'1s': 'vengo', '2s': 'vieni', '3s': 'viene', '1p': 'veniamo', '2p': 'venite', '3p': 'vengono' },
              'future': {'1s': 'verrò', '2s': 'verrai', '3s': 'verrà', '1p': 'verremo', '2p': 'verrete', '3p': 'verranno' },
#              'conditional': {'1s': 'verrei', '2s': 'verresti', '3s': 'verrebbe', '1p': 'verremmo', '2p': 'verreste', '3p': 'verrebbero' },
              'imperative': {'2s': 'vieni', '3s': 'venga', '1p': 'veniamo', '2p': 'venite', '3p': 'vengano' },
              'perfect': 'venuto', 'aux': 'essere', 'prep': 'a' 
              },
    'bere': {'trans': 'drink', 'strans': 'dricka',
              'present': {'1s': 'bevo', '2s': 'bevi', '3s': 'beve', '1p': 'beviamo', '2p': 'bevete', '3p': 'bevono' },
              'imperfect': {'1s': 'bevevo', '2s': 'bevevi', '3s': 'beveva', '1p': 'bevevamo', '2p': 'bevevate', '3p': 'beverano' },
              'future': {'1s': 'berrò', '2s': 'berrai', '3s': 'berrà', '1p': 'berremo', '2p': 'berrete', '3p': 'berranno' },
#              'conditional': {'1s': 'berrei', '2s': 'berresti', '3s': 'berrebbe', '1p': 'berremmo', '2p': 'berreste', '3p': 'berrebbero' },
              'imperative': {'2s': 'bevi', '3s': 'beva', '1p': 'beviamo', '2p': 'bevete', '3p': 'bevano' },
              'perfect': 'bevuto',
             'subjunctive imperfect': {'1s': 'bevessi', '2s': 'bevessi', '3s': 'bevessi', '1p': 'bevessimo', '2p': 'beveste', '3p': 'bevessero' }
              },
    'cadere': {'trans': 'fall', 'strans': 'falla',
              'future': {'1s': 'cadrò', '2s': 'cadrai', '3s': 'cadrà', '1p': 'cadremo', '2p': 'cadrete', '3p': 'cadranno' },
#              'conditional': {'1s': 'cadrei', '2s': 'cadresti', '3s': 'cadrebbe', '1p': 'cadremmo', '2p': 'cadreste', '3p': 'cadrebbero' },
              'aux': 'essere'},
    'porre': {'trans': ('place','lay'), 'strans': 'lägga',
              'present': {'1s': 'pongo', '2s': 'poni', '3s': 'pone', '1p': 'poniamo', '2p': 'ponete', '3p': 'pongono' },
              'imperfect': {'1s': 'ponevo', '2s': 'ponevi', '3s': 'poneva', '1p': 'ponevamo', '2p': 'ponevate', '3p': 'ponevano' },
              'future': {'1s': 'porrò', '2s': 'porrai', '3s': 'porrà', '1p': 'porremo', '2p': 'porrete', '3p': 'porranno' },
#              'conditional': {'1s': 'porrei', '2s': 'porresti', '3s': 'porrebbe', '1p': 'porremmo', '2p': 'porreste', '3p': 'porrebbero' },
              'imperative': {'2s': 'poni', '3s': 'pona', '1p': 'poniamo', '2p': 'ponete', '3p': 'ponano' },
              'perfect': 'posto'
              },
    'trarre': {'trans': 'pull', 'strans': 'dra',
              'present': {'1s': 'traggo', '2s': 'trai', '3s': 'trae', '1p': 'traiamo', '2p': 'traete', '3p': 'traggono' },
              'imperfect': {'1s': 'traevo', '2s': 'traevi', '3s': 'traeva', '1p': 'traevamo', '2p': 'traevate', '3p': 'traevanno' },
              'future': {'1s': 'trarrò', '2s': 'trarrai', '3s': 'trarrà', '1p': 'trarremo', '2p': 'trarrete', '3p': 'trarranno' },
#              'conditional': {'1s': 'trarrei', '2s': 'trarresti', '3s': 'trarrebbe', '1p': 'trarremmo', '2p': 'trarreste', '3p': 'trarrebbero' },
              'imperative': {'2s': 'trai', '3s': 'traa', '1p': 'traiamo', '2p': 'traete', '3p': 'traggano' },
              'perfect': 'tratto'
              },
    'proporre' : { 'trans': 'propose', 'strans': 'föreslå', 'ref' : 'porre' },
    'suporre' : { 'trans': 'suppose', 'strans': 'antaga', 'ref' : 'porre' }, 
    'chiedere': { 'trans': 'ask', 'strans': 'fråga','perfect': 'chiesto' },
    'rispondere': { 'trans': 'answer', 'strans': 'svara','perfect': 'risposto' },
    'parlare': { 'trans': 'talk', 'strans': 'tala' },
    'chiamare': { 'trans': 'call', 'strans': 'kalla' },
    'ridere':  {'trans': 'laugh', 'strans': 'skratta', 'perfect': 'riso' },
    'piangere': {'trans': 'weep', 'strans': 'gråta', 'perfect': 'pianto' },
    'conoscere': { 'trans': 'know_about', 'strans': 'känna', 'perfect': 'conosciuto' },
    'credere': { 'trans': 'believe', 'strans': 'tro'},
    'pensare': { 'trans': 'think', 'strans': 'tänka' },
    'decidere': { 'trans': 'decide', 'strans': 'bestämma', 'perfect': 'deciso' },
    'ricordare': { 'trans': 'remember', 'strans': 'minnas'},    
    'dimenticare': { 'trans': 'forget+', 'strans': 'glömma'},
    'aiutare': { 'trans': 'help', 'strans': 'hjälpa', 'prep': ''},
    'insegnare': {'trans': 'teach', 'strans': 'undervisa','prep': '' },
    'imparare': {'trans': 'learn', 'strans': 'lära', 'prep': ''},    
    'capire' : {'trans': 'understand', 'strans': 'förstå','conj': 'isc' },
    'aprire':  {'trans': 'open', 'strans': 'öppna', 'perfect': 'aperto'  },
    'chiudere': { 'trans': 'close', 'strans': 'stänga', 'perfect': 'chiuso' },
    'coprire':  {'trans': 'cover', 'strans': 'täcka', 'perfect': 'coperto'  },
    'scoprire':  {'trans': 'uncover', 'strans': 'avtäcka', 'perfect': 'scoperto'  },
    'nascondere' : {'trans': 'hide', 'strans': 'gömma', 'perfect': 'nascosto' },
    'cercare': {'trans': 'search', 'strans': 'söka'},
    'trovare': {'trans': 'find', 'strans': 'hitta'},
    'provare': {'trans': 'try', 'strans': 'försöka' },
    'riuscire': {'trans': 'succeed', 'strans': 'lyckas', 'ref': 'uscire'},
    'fallire': {'trans': 'fail', 'strans': 'misslyckas', 'conj': 'isc'},
    'sedere': { 'trans': 'sit+', 'strans': 'sitta',
                'present': {'1s': 'siedo', '2s': 'siedi', '3s': 'siede', '1p': 'sediamo', '2p': 'sedete', '3p': 'siedono' },
                'imperative': {'2s': 'siedi', '3s': 'sieda', '1p': 'sediamo', '2p': 'sedete', '3p': 'siedano' }},
    'giacere': { 'trans': 'lie(place)', 'strans': 'ligga', 'perfect': 'giaciuto' },
    'correre': { 'trans': 'run+', 'strans': 'springa', 'perfect': 'corso', 'aux': 'essere', 'prep': ''},
    'camminare': { 'trans': 'walk', 'strans': 'gå_till fots'},
    'girare': {'trans': 'turn', 'strans': 'vända'  },
    'muovere':  {'trans': 'move', 'strans': 'flytta', 'perfect': 'mosso' },
    'spingere': {'trans': 'push', 'strans': 'knuffa', 'perfect': 'spinto' },
    'stringere': { 'trans': 'press', 'strans': 'trycka', 'perfect' : 'stretto' },
    'mettere':  {'trans': ('put+','wear'), 'strans': ('lägga','bära'), 'perfect': 'messo', 'prep': 'a' },
    'prendere': { 'trans': 'take', 'strans': 'ta', 'perfect' : 'preso'},
    'tenere': { 'trans': 'hold', 'strans': 'hålla',
                'present': {'1s': 'tengo', '2s': 'tieni', '3s': 'tiene',  '3p': 'tengono' },
                'future': {'1s': 'terrò', '2s': 'terrai', '3s': 'terrà', '1p': 'terremo', '2p': 'terrete', '3p': 'terranno' },
#                'conditional': {'1s': 'terrei', '2s': 'terresti', '3s': 'terrebbe', '1p': 'terremmo', '2p': 'terreste', '3p': 'terrebbero' },
                'imperative': {'2s': 'tieni', '3s': 'tiena',  '3p': 'tengano' } },
    'tirare':  { 'trans': 'throw', 'strans': 'kasta' },
    'levare': { 'trans': 'lift', 'strans': 'lyfta' },
    'portare' : { 'trans' : ('carry','bring'), 'strans': ('bära', 'hämta'),'prep': 'a' },
    'toccare': { 'trans': 'touch', 'strans': 'röra' },
    'lasciare': { 'trans': 'leave', 'strans': 'lämna','prep': '' },    
    'leggere': { 'trans': 'read', 'strans': 'läsa', 'perfect' : 'letto'},
    'scrivere': { 'trans': 'write', 'strans': 'skriva','perfect' : 'scritto'},
    'cominciare': { 'trans': 'begin', 'strans': 'börja', 'prep': 'a' },    
    'finire': { 'trans': 'end', 'strans': 'sluta','conj': 'isc' },
    'accendere': {'trans': ('switch_on','light'), 'strans': 'tända','perfect': 'acceso' },
    'spegnere': {'trans': ('switch_off','extinguish'), 'strans': 'släcka',
                  'present': {'1s': 'spengo', '3p': 'spengono'}, 'imperative': {'3p': 'spengano'},
                 'perfect': 'spento' },
    'mangiare':  {'trans': 'eat', 'strans': 'äta' },
    'lavorare': {'trans': 'work', 'strans': 'arbeta' },
    'dormire': {'trans': 'sleep', 'strans': 'sova'},    
    'morire':  {'trans': 'die',  'strans': 'dö',
              'present': {'1s': 'muoio', '2s': 'muori', '3s': 'muore', '1p': 'moriamo', '2p': 'morite', '3p': 'muoiono' },
              'imperative': {'2s': 'muori', '3s': 'muoia', '1p': 'moriamo', '2p': 'morite', '3p': 'muoiano' },
              'perfect': 'morto', 'aux': 'essere' 
              },      
    'vivere':  {'trans': 'live(bio)',  'strans': 'leva',
                'future': {'1s': 'vivrò', '2s': 'vivrai', '3s': 'vivrà', '1p': 'vivremo', '2p': 'vivrete', '3p': 'vivranno' },
#               'conditional': {'1s': 'vivrei', '2s': 'vivresti', '3s': 'vivrebbe', '1p': 'vivremmo', '2p': 'vivreste', '3p': 'vivrebbero' },
                'perfect': 'vissuto', 'aux': 'essere' },
    'nascere':  {'trans': 'be_born',  'strans': 'födas', 'perfect': 'nato', 'aux': 'essere' },
    'udire':  {'trans': 'hear',  'strans': 'höra',
                'present': {'1s': 'odo', '2s': 'odi', '3s': 'ode',  '3p': 'odono' },
                'imperative': {'2s': 'odi', '3s': 'oda', '3p': 'odano' }, 'prep': '' },
    'uscire':  {'trans': 'exit',  'strans': 'gå_ut',
                'present': {'1s': 'esco', '2s': 'esci', '3s': 'esce',  '3p': 'escono' },
                'imperative': {'2s': 'esci', '3s': 'esca', '3p': 'escano' },
                'aux': 'essere', 'prep': 'a' },
    'entrare' : {'trans': 'enter', 'aux': 'essere',  'strans': 'gå_in', 'prep': 'a' },
    'condurre': {'trans': 'lead',  'strans': 'leda',
                'present': {'1s': 'conduco', '2s': 'conduci', '3s': 'conduce', '1p': 'conduciamo', '2p': 'conducete', '3p': 'conducono' },
              'imperfect': {'1s': 'conducevo', '2s': 'conducevi', '3s': 'conduceve', '1p': 'conducevamo', '2p': 'conducevate', '3p': 'conducevanno' },
              'future': {'1s': 'condurrò', '2s': 'condurrai', '3s': 'condurrà', '1p': 'condurremo', '2p': 'condurrete', '3p': 'condurranno' },
#              'conditional': {'1s': 'condurrei', '2s': 'condurresti', '3s': 'condurrebbe', '1p': 'condurremmo', '2p': 'condurreste', '3p': 'condurrebbero' },
              'imperative': {'2s': 'conduci', '3s': 'conduca', '1p': 'conduciamo', '2p': 'conducete', '3p': 'conducano' },
              'perfect': 'condutto', 'prep': 'a'},
    'seguire' : {'trans': 'follow',  'strans': 'följa' },
    'fuggire' : {'trans': 'escape',  'strans': 'fly', 'aux': 'essere' },
    'inseguire' : {'trans': 'pursue',  'strans': 'förfölja' },
    'sentire' : {'trans': 'feel',  'strans': 'höra' },
    'vestire' : {'trans': 'dress',  'strans': 'kläda' },
    'servire' : {'trans': 'serve',  'strans': 'betjäna', 'prep': 'a' },
    'arrivare' : {'trans': 'arrive',  'strans': 'anlända', 'aux': 'essere', 'prep': 'a' },
    'partire' : {'trans': 'depart',  'strans': 'avresa', 'aux': 'essere' },
    'preferire' : {'trans': 'prefer+',  'strans': 'föredra', 'conj': 'isc' },
    'spedire' : {'trans': 'send',  'strans': 'skicka', 'conj': 'isc' },
    'ricevere' : {'trans': 'receive',  'strans': 'ta_emot' },
    'tornare' : {'trans': 'return',  'strans': 'återvända', 'aux': 'essere', 'prep': 'a' },
    'incontrare': {'trans': 'meet',  'strans': 'möta' },
    'aspettare': {'trans': 'wait',  'strans': 'vänta' },
    'vendere': {'trans': 'sell',  'strans': 'sälja' },
    'comprare': {'trans': 'buy',  'strans': 'köpa' },
    'pagare': {'trans': 'pay',  'strans': 'betala' },
    'costare': {'trans': 'cost',  'strans': 'kosta' },
    'amare': {'trans': 'love',  'strans': 'älska' },
    'odiare': {'trans': 'hate',  'strans': 'hata' },
    'piacere' : {'trans': 'please',  'strans': 'tilltala', 'present': {'1s': 'piaccio', '1p': 'piacciamo', '3p': 'piacciono' },
                 'imperative': {'1p': 'piacciamo', '3p': 'piacciano' },
                 'perfect': 'piaciuto', 'aux': 'essere' },
    'perdere': {'trans': 'lose',  'strans': 'förlora', 'perfect': 'perso' },
    'vincere': {'trans': 'win+',  'strans': 'vinna', 'perfect': 'vinto' },
    'permettere': {'trans': 'allow',  'strans': 'tillåta', 'ref': 'mettere' },
    'vietare': {'trans': 'forbid+',  'strans': 'förbjuda' },
    'fermare' : {'trans': 'stop+',  'strans': 'stoppa' },
    'cambiare' : {'trans' : 'change',  'strans': 'byta' },
    'diventare' : {'trans' : 'become',  'strans': 'bli', 'aux': 'essere' },
    'succedere':  {'trans': 'happen',  'strans': 'hända', 'perfect': 'successo' },
    'usare': {'trans': 'use',  'strans': 'använda' },
    'desiderare': {'trans': 'wish' }
    
    
}

eng_verbs = \
    {
    'be': { 'ongoing': 'being',
            'present': { '1s' : 'am', '2s': 'are', '3s' : 'is', '1p': 'are', '2p': 'are', '3p': 'are' },
            'imperfect': { '1s' : 'was', '2s': 'were', '3s' : 'was', '1p': 'were', '2p': 'were', '3p': 'were' },
            'perfect': 'been'},
    'have': {'present': { '1s': 'have', '2s': 'have', '3s' : 'has', '1p': 'have', '2p': 'have', '3p': 'have' },
            'imperfect': 'had', 'perfect': 'had'},
    'be able to': {'present': {'1s': 'can', '2s': 'can', '3s' : 'can', '1p': 'can', '2p': 'can', '3p': 'can'}, 
                    'imperfect': 'could', 'perfect': 'been able to', 'ongoing' : 'being able to'},
    'know': {'imperfect': 'knew', 'perfect': 'known'},
    'want': {}, 
    'give': {'imperfect': 'gave', 'perfect': 'given'},
    'stay': {},
    'do': { 'imperfect': 'did', 'perfect': 'done'},
    'make': { 'imperfect': 'made', 'perfect': 'made'},
    'feel': { 'imperfect': 'felt', 'perfect': 'felt'},
    'go': {'imperfect': 'went', 'perfect': 'gone'},
    'say': { 'imperfect': 'said', 'perfect': 'said'},
    'tell': { 'imperfect': 'told', 'perfect': 'told'},
    'run': { 'imperfect': 'ran', 'perfect': 'ran', 'ongoing' : 'running'},
    'see': { 'imperfect': 'saw', 'perfect': 'seen', 'ongoing': 'seeing'},
    'come': {'imperfect': 'came', 'perfect': 'come'},
    'leave': { 'imperfect': 'left', 'perfect': 'left'},
    'fall': {'imperfect': 'fell', 'perfect': 'fallen'},
    'drink': { 'imperfect': 'drank', 'perfect': 'drunk'},
    'eat': { 'imperfect': 'ate', 'perfect': 'eaten'}, 'read': { 'imperfect': 'read', 'perfect': 'read'},
    'sit': {'imperfect': 'sat', 'perfect': 'sat', 'ongoing': 'sitting' },
    'hold': { 'imperfect': 'held', 'perfect': 'held'},
    'put': { 'imperfect': 'put', 'perfect': 'put', 'ongoing': 'putting'},
    'take': {'imperfect': 'took', 'perfect': 'taken' },  'push': {}, 'pull': {},
    'press': {}, 'wear': {}, 'walk': {}, 'move': {}, 'lift': {},
    'bring': {'imperfect': 'brought', 'perfect': 'brought'}, 'carry': {},
    'write': {'imperfect': 'wrote', 'perfect': 'written' },
    'throw': {'imperfect': 'threw', 'perfect': 'thrown' }, 
    'ask': {}, 'answer': {'ongoing':'answering'}, 'close': {}, 'open': {}, 'talk': {}, 'end': {}, 'switch': {}, 'extinguish': {}, 'light': {},
    'suppose': {}, 'propose': {}, 'laugh': {}, 
    'lie(place)': {'imperfect': 'lay', 'perfect': 'lain', 'ongoing': 'lying' },
    'lay': {'imperfect': 'laid', 'perfect': 'laid' },
    'live(bio)':  {}, 'die': { 'ongoing': 'dying'}, 'exit' : {},
    'hear': { 'imperfect': 'heard', 'perfect': 'heard'},
    'decide' : {}, 'cover': {}, 'uncover': {}, 'offer': {}, 'suffer': {}, 'escape': {}, 'follow': {},
    'pursue': {}, 'serve': {}, 'understand': {'imperfect': 'understood', 'perfect': 'understood'},
    'send': {'imperfect': 'sent', 'perfect': 'sent'},  'prefer': {},
    'receive': {}, 'return': {}, 'arrive': {}, 'sell': {'imperfect': 'sold', 'perfect': 'sold' },
    'buy': {'imperfect': 'bought', 'perfect': 'bought' },
    'pay': {'imperfect': 'paid', 'perfect': 'paid' },
    'cost': {}, 'love': {}, 'hate': {}, 'please' : {},
    'meet': {'imperfect': 'met', 'perfect': 'met' }, 'wait': {}, 'hide': {'imperfect': 'hid', 'perfect': 'hidden' },
    'enter': {}, 'turn': {}, 'win': {'imperfect': 'won', 'perfect': 'won', 'ongoing' : 'winning' },
    'lose': {'imperfect': 'lost', 'perfect': 'lost' },
    'place': {}, 'weep': {'imperfect': 'wept', 'perfect': 'wept' },
    'begin': {'imperfect': 'began', 'perfect': 'begun' },
    'teach': {'imperfect': 'taught', 'perfect': 'taught' },
    'think': {'imperfect': 'thought', 'perfect': 'thought' },
    'learn': {}, 'remember': {}, 'forget': {'imperfect': 'forgot', 'perfect': 'forgotten' },
    'touch': {}, 'work': {}, 'sleep': {'imperfect': 'slept', 'perfect': 'slept'},
    'help': {}, 'search' : {}, 'find': {'imperfect': 'found', 'perfect': 'found'},
    'succeed': {}, 'fail': {}, 'allow': {}, 'forbid' : {'imperfect': 'forbid', 'perfect': 'forbidden'},
    'stop' : {'imperfect': 'stopped', 'perfect': 'stopped', 'ongoing':'stopping'},
    'change' : {}, 'become': {'imperfect': 'became', 'perfect': 'become'},
    'call' : {}, 'arrive': {}, 'depart': {}, 'happen': {}, 'use': {},
    'lead' : {'imperfect': 'led', 'perfect': 'led'}, 'try': {}, 'believe': {},
    'dress' : {},
    'wish' : {}

    }


swe_verbs = \
    {
    'vara': { 'present': 'är', 'imperfect':'var', 'perfect': 'varit'}, 
    'ha': { 'present': 'har', 'imperfect':'hade', 'perfect': 'haft' }, 
    'kunna': { 'present': 'kan', 'imperfect':'kunde', 'perfect': 'kunnat'}, 
    'veta': { 'present': 'vet', 'imperfect':'visste', 'perfect': 'vetat'}, 
    'vilja': { 'present': 'vill', 'imperfect':'ville', 'perfect': 'velat'},
    'känna': { 'present': 'känner', 'imperfect':'kände', 'perfect': 'känt'},
    'ge': {'imperfect': 'gav', 'perfect': 'givit'},
    'befinna': { 'present': 'befinner', 'imperfect':'befann', 'perfect': 'befunnit'}, 
    'göra': {'present': 'gör', 'imperfect': 'gjorde', 'perfect': 'gjort'},
    'tillverka': {},
    'gå': { 'imperfect':'gick', 'perfect': 'gått'}, 
    'säga': { 'present': 'säger', 'imperfect':'sade', 'perfect': 'sagt'}, 
    'berätta': { }, 
    'springa': { 'present': 'springer', 'imperfect':'sprang', 'perfect': 'sprungit'}, 
    'se': {  'imperfect':'såg', 'perfect': 'sett'}, 
    'komma': { 'present': 'kommer', 'imperfect':'kom', 'perfect': 'kommit'}, 
    'lämna': { },
    'falla': { 'present': 'faller', 'imperfect':'föll', 'perfect': 'fallit'}, 
    'dricka': { 'present': 'dricker', 'imperfect':'drack', 'perfect': 'druckit'},
    'äta': { 'present': 'äter', 'imperfect':'åt', 'perfect': 'ätit'}, 
    'sitta': { 'present': 'sitter', 'imperfect':'satt', 'perfect': 'suttit'}, 
    'hålla': { 'present': 'håller', 'imperfect':'höll', 'perfect': 'hållit'}, 
    'sätta': { 'present': 'sätter', 'imperfect':'satte', 'perfect': 'satt'}, 
    'ta': { 'present': 'tar', 'imperfect':'tog', 'perfect': 'tagit'}, 
    'flytta': {}, 
    'knuffa': { }, 
    'dra': {'present': 'drar', 'imperfect':'drog', 'perfect': 'dragit'},
    'lyfta': { 'present': 'lyfter', 'imperfect':'lyfte', 'perfect': 'lyft'}, 
    'trycka': { 'present': 'trycker', 'imperfect':'tryckte', 'perfect': 'tryckt'}, 
    'hämta': { } ,
    'bära': { 'present': 'bär', 'imperfect':'bar', 'perfect': 'burit'}, 
    'skriva': { 'present': 'skriver', 'imperfect':'skrev', 'perfect': 'skrivit'}, 
    'läsa': { 'present': 'läser', 'imperfect':'läste', 'perfect': 'läst'}, 
    'kasta': {}, 'fråga': {}, 'svara': {},
    'stänga': {'present': 'stänger', 'imperfect':'stängde', 'perfect': 'stängt'},
    'öppna': {}, 'tala': {}, 'sluta': {},
    'släcka': {'present': 'släcker', 'imperfect':'släckte', 'perfect': 'släckt'},
    'tända': {'present': 'tänder', 'imperfect':'tände', 'perfect': 'tänt'},
    'antaga': {'present': 'antager', 'imperfect':'antog', 'perfect': 'antagit'},
    'föreslå': {'present': 'föreslår', 'imperfect':'föreslog', 'perfect': 'föreslagit'},
    'skratta': {}, 
    'lägga': {'present': 'lägger', 'imperfect':'lagde', 'perfect': 'lagt'},
    'ligga': {'present': 'ligger', 'imperfect':'lade', 'perfect': 'legat'},
    'byta': {'present': 'byter', 'imperfect':'bytte', 'perfect': 'bytt'},
    'leva': {'present': 'lever', 'imperfect':'levde', 'perfect': 'levt' },
    'dö': {'present': 'dör', 'imperfect':'dog', 'perfect': 'dött' },
    'födas': {'present': 'föds', 'imperfect':'föddes', 'perfect': 'fötts' },
    'höra': { 'present': 'hör', 'imperfect':'hörde', 'perfect': 'hört'},
    'bestämma' : {'present': 'bestämmer', 'imperfect':'bestämde', 'perfect': 'bestämt'},
    'täcka': {'present': 'täcker', 'imperfect':'täckte', 'perfect': 'täckt'},
    'avtäcka': {'present': 'avtäcker', 'imperfect':'avtäckte', 'perfect': 'avtäckt'},
    'erbjuda': {'present': 'erbjuder', 'imperfect':'erbjöd', 'perfect': 'erbjudit'},
    'lida': {'present': 'lider', 'imperfect':'led', 'perfect': 'lidit'},
    'fly': {'present': 'flyr', 'imperfect':'flydde', 'perfect': 'flytt'},
    'följa': {'present': 'följer', 'imperfect':'följde', 'perfect': 'följt'},
    'förfölja': {'present': 'förföljer', 'imperfect':'förföljde', 'perfect': 'förföljt'},
    'betjäna': {}, 'förstå': {'present': 'förstår', 'imperfect':'förstådde', 'perfect': 'förstått'},
    'skicka': {},  'föredra': {'present': 'föredrar', 'imperfect':'föredrog', 'perfect': 'föredragit'},
    'återvända': {'present': 'återvänder', 'imperfect':'återvände', 'perfect': 'återvändit'},
    'anlända': {'present': 'anländer', 'imperfect':'anlände', 'perfect': 'anlänt'},
    'sälja': {'present': 'säljer', 'imperfect':'sålde', 'perfect': 'sålt'},
    'köpa': {'present': 'köper', 'imperfect':'köpte', 'perfect': 'köpt'},
    'betala': {},
    'kosta': {}, 'älska': {}, 'hata': {}, 'tilltala' : {},
    'möta': {'present': 'möter', 'imperfect':'mötte', 'perfect': 'mött'}, 'vänta': {},
    'gömma': {'present': 'gömmer', 'imperfect':'gömde', 'perfect': 'gömt'},
    'vända': {'present': 'vänder', 'imperfect':'vände', 'perfect': 'vänt'},
    'vinna': {'present': 'vinner', 'imperfect':'vann', 'perfect': 'vunnit' },
    'förlora': {},
    'placera': {}, 'gråta': {'present': 'gråter', 'imperfect':'grät', 'perfect': 'gråtit' },
    'börja': {},
    'lära': {'present': 'lär', 'imperfect':'lärde', 'perfect': 'lärt'},
    'tänka': {'present': 'tänker', 'imperfect':'tänkte', 'perfect': 'tänkt'},
    'undervisa': {}, 'minnas': {'present': 'minns', 'imperfect':'mindes', 'perfect': 'minnats'},
    'glömma': {'present': 'glömmer', 'imperfect':'glömde', 'perfect': 'glömt'},
    'röra': {'present': 'rör', 'imperfect':'rörde', 'perfect': 'rört'},
    'arbeta': {}, 'sova': {'present': 'sover', 'imperfect':'sov', 'perfect': 'sovt'},
    'hjälpa': {'present': 'hjälper', 'imperfect':'hjälpte', 'perfect': 'hjälpt'},
    'söka' : {'present': 'söker', 'imperfect':'sökte', 'perfect': 'sökt'},
    'hitta': {},
    'lyckas': {'present': 'lyckas', 'imperfect':'lyckades', 'perfect': 'lyckats'},
    'misslyckas': {'present': 'misslyckas', 'imperfect':'misslyckades', 'perfect': 'misslyckats'},
    'tillåta': {'present': 'tillåter', 'imperfect':'tillät', 'perfect': 'tillåtit'},
    'förbjuda' : {'present': 'förbjuder', 'imperfect':'förbjöd', 'perfect': 'förbjudit'},
    'stoppa' : {},
    'ändra' : {}, 'bli': {'present': 'blir', 'imperfect':'blev', 'perfect': 'blivit'},
    'kalla' : {}, 'avresa': {'present': 'avreser', 'imperfect':'avreste', 'perfect': 'avrest'},
    'hända': {'present': 'händer', 'imperfect':'hände', 'perfect': 'hänt'},
    'använda': {'present': 'använder', 'imperfect':'använde', 'perfect': 'använt'},
    'leda' : {'present': 'leder', 'imperfect':'ledde', 'perfect': 'lett'},
    'försöka' : {'present': 'försöker', 'imperfect':'försökte', 'perfect': 'försökt'},
    'tro': {'present': 'tror', 'imperfect':'trodde', 'perfect': 'trott'},
    'kläda': {'present': 'kläder', 'imperfect':'klädde', 'perfect': 'klätt'}
}        
            

general_verb_patterns = \
    {
        'present':
        {   '1s': { 'a': 'o', 'e': 'o', 'i': 'o', 'isc': 'isco' }, 
            '2s': { 'a': 'i', 'e': 'i', 'i': 'i', 'isc': 'isci' },
            '3s': { 'a': 'a', 'e': 'e', 'i': 'e', 'isc': 'isce' },
            '1p': 'iamo',
            '2p': { 'a': 'ate', 'e': 'ete', 'i': 'ite', 'isc': 'ite' },
            '3p': { 'a': 'ano', 'e': 'ono', 'i': 'ono', 'isc': 'iscono' }
        },
        'imperfect':
        {   '1s': { 'a': 'avo', 'e': 'evo', 'i': 'ivo', 'isc': 'ivo' }, 
            '2s': { 'a': 'avi', 'e': 'evi', 'i': 'ivi', 'isc': 'ivi' },
            '3s': { 'a': 'ava', 'e': 'eva', 'i': 'iva', 'isc': 'iva' },
            '1p': { 'a': 'avamo', 'e': 'evamo', 'i': 'ivamo', 'isc': 'ivamo' },
            '2p': { 'a': 'avate', 'e': 'evate', 'i': 'ivate', 'isc': 'ivate' },
            '3p': { 'a': 'avano', 'e': 'evano', 'i': 'ivano', 'isc': 'ivano' }
        },
        'future' : 
        {   '1s': { 'a': 'erò', 'e': 'erò', 'i': 'irò', 'isc': 'irò' }, 
            '2s': { 'a': 'erai', 'e': 'erai', 'i': 'irai', 'isc': 'irai' },
            '3s': { 'a': 'erà', 'e': 'erà', 'i': 'irà', 'isc': 'irà' },
            '1p': { 'a': 'eremo', 'e': 'eremo', 'i': 'iremo', 'isc': 'iremo' },
            '2p': { 'a': 'erete', 'e': 'erete', 'i': 'irete', 'isc': 'irete' },
            '3p': { 'a': 'eranno', 'e': 'eranno', 'i': 'iranno', 'isc': 'iranno' }
        },
        'conditional':
        {   '1s': 'ei', 
            '2s': 'esti', 
            '3s': 'ebbe', 
            '1p': 'emmo', 
            '2p': 'este',
            '3p': 'ebbero',
        },
        'imperative':
        {    
            '2s': { 'a': 'a', 'e': 'i', 'i': 'i', 'isc': 'isci' },
            '3s': { 'a': 'i', 'e': 'a', 'i': 'a', 'isc': 'isca' },
            '1p': 'iamo',
            '2p': { 'a': 'ate', 'e': 'ete', 'i': 'ite', 'isc': 'ite' },
            '3p': { 'a': 'ino', 'e': 'ano', 'i': 'ano', 'isc': 'iscano' }
        },
        'subjunctive present':
        {    
            '1s': { 'a': 'i', 'e': 'a', 'i': 'a', 'isc': 'a' },
            '2s': { 'a': 'i', 'e': 'a', 'i': 'a', 'isc': 'a' },
            '3s': { 'a': 'i', 'e': 'a', 'i': 'a', 'isc': 'a' },
            '1p': 'iamo',
            '2p': 'iate',
            '3p': { 'a': 'ino', 'e': 'ano', 'i': 'ano', 'isc': 'ano' }
        },
        'subjunctive imperfect':
        {    
            '1s': { 'a': 'ssi', 'e': 'ssi', 'i': 'ssi', 'isc': 'ssi' },
            '2s': { 'a': 'ssi', 'e': 'ssi', 'i': 'ssi', 'isc': 'ssi' },
            '3s': { 'a': 'sse', 'e': 'sse', 'i': 'sse', 'isc': 'sse' },
            '1p': { 'a': 'ssimo', 'e': 'ssimo', 'i': 'ssimo', 'isc': 'ssimo' },
            '2p': { 'a': 'ste', 'e': 'ste', 'i': 'ste', 'isc': 'ste' },
            '3p': { 'a': 'ssero', 'e': 'ssero', 'i': 'ssero', 'isc': 'ssero' }
        },
        'perfect': { 'a': 'ato', 'e': 'uto', 'i': 'ito', 'isc': 'ito' }
    }

composite_verb_patterns = { 'perfect' : 'present', 'pluskvamperfect': 'imperfect', 'conditional II': 'conditional',
                            'future exactum': 'future', 'subjunctive perfect': 'subjunctive present',
                            'subjunctive pluskvamperfect': 'subjunctive imperfect'}    

def it_verb(form,tempus,person,prep=False,neg=False,adverb=False):
    if '(' in form:
        form =  form[:form.index('(')]
    if '_' in form:
        form_split = form.split('_')
        form = form_split[0]
        add_on = ' '+form_split[1]
    else:
        add_on = ''
    reflexive = (form[-3:] in ['si0','si1','si2']) and person    
    if reflexive:
        form = form[:-3]+'e'
    if len(person) >= 3:
        gender=person[2]
        person = person[:2]
    else:
        gender='m'
    verb_entry = verbs[form]
    try:
        ref = verb_entry['ref']
        prefix = form[0:len(form)-len(ref)]
        form = ref
        verb_entry = verbs[form]        
    except KeyError:
        prefix = ''
    if prep:
        try:
            prep = verb_entry['prep']
            if prep:
                prep = ' '+prep
        except KeyError:
            prep = ' di'
    else:
        prep = ''
    if tempus == 'infinitive':
        if reflexive:
            form2 = prefix+form[:-1]+it_pronoun('reflexive',reflexive)
        else:
            form2 = prefix+form
    elif tempus in ['present', 'imperfect', 'future', 'subjunctive present', 'subjunctive imperfect']:
        try:
            form2 = prefix+verb_entry[tempus][person]        
        except KeyError:
            root = prefix+form[:-3]
            if tempus in ['subjunctive present'] and person in ['1s','2s','3s','3p']:
                root = prefix+it_verb(form,'present','1s')[:-1]
            elif tempus in ['subjunctive imperfect']:
                root = prefix+it_verb(form,'imperfect','1s')[:-2]
            try:
                conjugation = verb_entry['conj']
            except KeyError:            
                conjugation = form[-3]
            suffix = general_verb_patterns[tempus][person]
            if type(suffix) == dict:
                suffix = suffix[conjugation]
            if root[-1] == 'i' and conjugation == 'a' and suffix[0] in 'ei':
                root = root[:-1]
            elif root[-2:] in ['ci', 'gi'] and conjugation == 'a' and suffix[0] in 'ei': #check - actually 
                root += 'h'
            form2 = root+suffix
    elif tempus == 'conditional':
        suffix = general_verb_patterns[tempus][person]
        form2 = prefix+it_verb(form,'future','1s')[:-1]+suffix 
    elif tempus == 'imperative':
        try:
            form2 = prefix+verb_entry[tempus][person]        
        except KeyError:
            if person in ['3s','3p']:
                form2 = prefix+it_verb(form,'subjunctive present',person)
                if form[-3] == 'a' and person == '3s':
                    form2 = form2[:-1]+'i'
            else:
                form2 = prefix+it_verb(form,'present',person)
                if form[-3] == 'a' and person == '2s':
                    form2 = form2[:-1]+'a'                    
    else:
        # Some form of essere/avere + perfect participe
        # First get the perfect participe part,
        # and put it in the correct tempus
        try:
            form2 = prefix+verb_entry['perfect']        
        except KeyError:
            root = prefix+form[:-3]
            try:
                conjugation = verb_entry['conj']
            except KeyError:            
                conjugation = form[-3]
            form2 = root+general_verb_patterns['perfect'][conjugation]
        # Then figure out whether to use essere or avera
        try:
            aux = verb_entry['aux']
        except KeyError:
            aux = 'avere'
        # Put the essere/avere in the right tempus, according to
        # the table composite_verb_patterns
        aux2 = it_verb(aux,composite_verb_patterns[tempus],person)
        if aux == 'essere':
            if person[1] == 's' and gender == 'f':
                form2 = form2[:-1]+'a'
            elif person[1] == 'p' and gender == 'f':
                form2 = form2[:-1]+'e'
            elif person[1] == 'p':
                form2 = form2[:-1]+'i'
        form2 = aux2+' '+form2
    if reflexive and not tempus == 'infinitive':
        form2=it_pronoun('reflexive',reflexive)+' '+form2
    if neg:
        form2='non '+form2
    return form2+add_on+prep

def get_it_verb_basic_form(form):
    if '(' in form:
        form = form[:form.find('(')]
    if form[-3:-1] == 'si':
        form = form[:-3]+'e'
    return form

def it_verb_form_extract_info(form,person):
    if '(' in form and form[form.index('(')+1] in '0123456789':
        version = int(form[form.index('(')+1:-1])
        form = form[:form.index('(')]
    else:
        version = 0
    if '_' in form:
        form_split = form.split('_')
        form = form_split[0]
        add_on = '_'+form_split[1]
    else:
        add_on = ''
    silent_reflexive = (form[-3:]=='si0' and person)    
    reflexive = (form[-3:]=='si1' and person)
    mutual_reflexive = (form[-3:]=='si2' and person)
    if silent_reflexive or reflexive or mutual_reflexive:
        if not form+add_on in verbs:            
            form = form[:-3]+'e'
    return form,version,add_on,silent_reflexive,reflexive,mutual_reflexive    


def trans_verb_form_extract_info(trans,version):
    if type(trans) == tuple:
        if len(trans) <= version:
            version = 0
        trans = trans[version]
    if '_' in trans:
        trans_split = trans.split('_')
        trans = trans_split[0]
        suffix = ' '+trans_split[1]
    else:
        suffix = ''
    if trans[-1] == '+':
        trans=trans[:-1]
        double_ending = True
    else:
        double_ending = False        
    return trans,suffix,double_ending

def eng_verb(form,tempus,person,trans=False,version=0):
    if person in ['3sp','3pp']:
        person = '2'+person[1]
    orig_person = person
    person = person[:2]
    form,version,add_on,silent_reflexive,reflexive,mutual_reflexive = it_verb_form_extract_info(form,person)
    trans = trans or verbs[form+add_on]['trans']
    trans,suffix,double_ending= trans_verb_form_extract_info(trans,version)
    trans_info = eng_verbs[trans]
    if '(' in trans: # and trans[trans.index('(')+1] in '0123456789':
        trans = trans[:trans.index('(')]
    if reflexive:
        reflexive = ' '+eng_pronoun('reflexive',orig_person)
    elif mutual_reflexive:
        reflexive = ' '+eng_pronoun('mutual reflexive',orig_person)        
    else:
        reflexive = ''
    if tempus == 'infinitive':
         form2 = trans
    elif tempus == 'ongoing':
        try:
            form2 = trans_info['ongoing']
        except KeyError:
            form2 = trans
            if form2[-1] == 'e':
                form2 = form2[:-1]
            elif  double_ending: # len(form2) >= 3 and form2[-1] in 'bdglmnprstz' and form2[-2] in 'aeiou'\
                 # and not filter(lambda ch: ch not in form2[:-3], 'aeiou'):
                form2 += form2[-1]
            form2 = form2+'ing'
    elif tempus == 'present':
        try:
            form2 = trans_info[tempus]
            if type(form2) == dict:
                form2 = form2[person]
        except KeyError:
            form2 = trans
            if person == '3s':
                if form2[-1] in ['s','z','o','h']:
                    form2 += 'es'
                elif form2[-1] == 'y' and form2[-2] not in 'aeiou':
                    form2 = form2[:-1]+'ies'
                else:
                    form2 += 's'
    elif tempus in ['imperfect','perfect']:
        try:
            form2 = trans_info[tempus]
            if type(form2) == dict:
                form2 = form2[person]
        except KeyError:
            if trans[-1] == 'e':
                form2 = trans+'d'
            elif trans[-1] == 'y' and trans[-2] in 'r':
                form2 = trans[:-1]+'ied'                
            else:
                if double_ending: #len(trans) >= 3 and trans[-1] in 'bdglmnprstz' and trans[-2] in 'aeiou'\
                                   #and trans[-3] not in 'aeiou':
                    trans = trans+trans[-1]
                form2 = trans+'ed'
    else:
        form2 = trans
    return form2+suffix+reflexive
    

def eng_verb_corresponding(verb,tempus,person,neg=False,trans=False):
    if tempus in ['present','subjunctive present']:
        if neg:
            if verb in ['essere','potere']:
                ing= eng_verb(verb,'present',person,trans)+' not'
            else:
                ing = eng_verb('fare','present',person)+' not '+\
                      eng_verb(verb,'infinitive','1s',trans) 
        else:
            ing = eng_verb(verb,'present',person,trans)
    elif tempus == 'imperfect':
            ing = eng_verb('essere','imperfect',person)+(neg and ' not' or '')+\
                  ' '+eng_verb(verb,'ongoing',person,trans)
    elif tempus in ['perfect','subjunctive perfect']:
        if neg:
            if verb in ['essere','potere']:
                ing= eng_verb(verb,'imperfect',person,trans)+' not'
            else:
                ing = eng_verb('fare','imperfect',person)+' not '+\
                      eng_verb(verb,'infinitive','1s',trans) 
        else:
            ing = eng_verb(verb,'imperfect',person,trans)
    elif tempus in ['pluskvamperfect','subjunctive imperfect']:
        ing = 'had '+(neg and 'not ' or '')+eng_verb(verb,'perfect',person,trans)
    elif tempus == 'future':
        ing = 'will '+(neg and 'not ' or '')+eng_verb(verb,'infinitive',person,trans)
    elif tempus == 'conditional':
        ing = 'would '+(neg and 'not ' or '')+eng_verb(verb,'infinitive',person,trans)
    elif tempus == 'imperative':
        if neg:
            ing = eng_verb('fare','present',person)+' not '+\
                    eng_verb(verb,'infinitive','1s',trans)
        else:
            ing = eng_verb(verb,'present',person,trans)    
    elif tempus == 'infinitive':
        ing = (neg and 'not ' or '')+eng_verb(verb,'infinitive','1s',trans)    
    return ing
          

def swe_verb(form,tempus,person,trans=False,version=0):
    if person in ['3sp','3pp']:
        person = '2'+person[1]
    orig_person = person
    person = person[:2]
    form,version,add_on,silent_reflexive,reflexive,mutual_reflexive = it_verb_form_extract_info(form,person)
    trans = trans or verbs[form+add_on]['strans']
    trans,suffix,double_ending= trans_verb_form_extract_info(trans,version)
    if suffix[-3:]=='sig':
        suffix=suffix[:-4]
        reflexive=True
    try:
        trans_info = swe_verbs[trans]
    except KeyError:
        return "SAKNAS", ""
    if '(' in trans: # and trans[trans.index('(')+1] in '0123456789':
        trans = trans[:trans.index('(')]
    if reflexive:
        reflexive = ' '+eng_pronoun('reflexive',orig_person)
    elif mutual_reflexive:
        reflexive = ' '+eng_pronoun('mutual reflexive',orig_person)        
    else:
        reflexive = ''
    if tempus == 'infinitive':
         form2 = trans
    else:
        try:
            form2 = trans_info[tempus]
        except KeyError:
            if tempus=='present':
                form2 = trans+"r"
            elif tempus=='imperfect':
                form2 = trans+"de"
            else:
                form2 = trans+"t"
    return form2,suffix+reflexive
                
                
            


def swe_verb_corresponding(verb,tempus,person,neg=False,trans=False,subclause=False):
    if tempus in ['present','subjunctive present']:
        v,s= swe_verb(verb,'present',person,trans)
        swe= (neg and subclause and 'inte ' or '')+v+(neg and not subclause and ' inte' or '')+s
    elif tempus == 'imperfect':
        v,s=swe_verb(verb,'imperfect',person,trans)
        swe = (neg and subclause and 'inte ' or '')+v+(neg and not subclause and ' inte' or '')+s+" (pågående)"
    elif tempus in ['perfect','subjunctive perfect']:
        v,s=swe_verb(verb,'imperfect',person,trans)
        swe = (neg and subclause and 'inte ' or '')+v+(neg and not subclause and ' inte' or '')+s
    elif tempus == 'pluskvamperfect':
        v,s=swe_verb(verb,'perfect',person,trans)
        swe = (neg and subclause and 'inte ' or '')+'hade '+(neg and not subclause and ' inte ' or '')+v+s
    elif tempus == 'future':
        v,s = swe_verb(verb,'infinitive',person,trans)
        swe = (neg and subclause and 'inte ' or '')+'skall '+(neg and not subclause and ' inte ' or '')+v+s
    elif tempus == 'conditional':
        v,s=swe_verb(verb,'infinitive',person,trans)
        swe = (neg and subclause and 'inte ' or '')+'skulle '+(neg and not subclause and ' inte ' or '')+v+s
    elif tempus == 'imperative':
        v,s=swe_verb(verb,'present',person,trans)
        swe = (neg and subclause and 'inte ' or '')+v+(neg and not subclause and ' inte' or '')+s    
    elif tempus == 'infinitive':
        v,s=swe_verb(verb,'infinitive','1s',trans)
        swe = (neg and 'inte ' or '')+v+s    
    return swe


for i in []: #verbs:
    v1,s1=swe_verb(i,'infinitive','1s')
    v2,s2=swe_verb(i,'present','1s')    
    v3,s3=swe_verb(i,'imperfect','1s')
    v4,s4=swe_verb(i,'perfect','1s')
    print(i, v1+s1, v2+s2, v3+s3, v4+s4, sep=', ')
            
