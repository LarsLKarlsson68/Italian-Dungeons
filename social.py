# -*- coding: cp1252 -*-S
import phrase, verb, noun

#verb

#subjunctive




subj_verbs=\
["comandare/command",
"ordinare/order",
"domandare/request",
"impedire/prevent",
"permettere/permit",
"proibire/prohibit",
"proporre/propose",
"suggerire/suggest",
"pregare/beg"
]

intrans_verbs=[
"chiacchiere/gossip",
"mentire|dire_bugie/lie(false)",
"essere_d'accordo/agree",
"discordare/disagree",
"urlare|gridare/shout",
"bisbigliare|sussurrare/whisper",
"ridere/laugh",
"cantare/sing",
"scherzare/joke",
"vincere/win",
"perdere/lose",
"ribattere/answer_back",
"lavorare/work",
"scusarsi0/apologize"
]

plural_verbs=[
"litigare/quarrel",
"cooperare|collaborare/cooperate",
"sposarsi0/marry",
"ballare/dance",
"giocare/play",
"radunare|raccogliere/gather",
"incontrare/meet"
]

special_trans_verbs=[
"allevare/raise", #children
"raccontare/tell", #story
"accettare/accept",
"declinare|rifiutare/decline"
]

trans_verbs=[
"ubbidire/obey",
"chiedere/ask",
"rispondere/answer",
"promettere/promise",
"tradire/betray",
"perdonare/forgive",
"consolare/console",
"deludere/disappoint",
"consigliare/advice",
"punire/punish",
"ricompensare/reward",
"opporre/oppose",
"salutare/greet",
"insultare/insult",
"elogiare|lodare/praise",
"criticare/criticize",
"ringraziare/thank",
"chiamare/call",
"ascoltare/listen_to",
"invitare/invite",
"conoscere/know",
"evitare/avoid",
"combattere/fight",
"aiutare/help",
"dominare/rule",
"baciare/kiss",
"abbracciare/hug"
]



#verb.verbs['proporre']={'ref':'porre'}
verb.verbs['opporre']={'ref':'porre'}
verb.verbs['impedire']={'conj': 'isc'}
verb.verbs['ubbidire']={'conj': 'isc'}
#verb.verbs['permettere']={'ref':'mettere'}
verb.verbs['proibire']={'conj': 'isc'}
verb.verbs['tradire']={'conj': 'isc'}
verb.verbs['deludere']={'perfect': 'deluso'}

verb.eng_verbs['choose'] = {'imperfect':'chose', 'perfect': 'chosen' }
verb.eng_verbs['sing'] = {'imperfect':'sang', 'perfect': 'sung' }

#noun

conversation=[
"la domanda/question",
"la risposta/answer",
"la promessa/promise",
"il tradimento/betrayal",
"la bugia|la menzogna/lie",
"la lite/quarrel",
"la storia|il racconto/story",
"l'insulto|l'affronto/insult",
"l'elogio|il lode/praise",
"la critica/criticism",
"l'urlo|il grido/shout",
"il bisbiglio|il sussurro/whisper",
"il segreto/secret",
"lo scherzo/joke",
"lo scandalo/scandal",
"la voce/rumour"
]

events=[
"la visita/visit",
"l'incontro/meeting",
"il ricevimento|la serata|la festa/party",
"il compleanno/birthday",
"il matrimonio/wedding",
"il matrimonio/marriage",          
"il battesimo/baptism",
"il funerale/funeral",
"l'accoglienza|il benvenuto/welcome",
"l'addio/farewell"

]

relatives= [
"la famiglia/family",
"il padre/father",
"la madre/mother",
"il figlio/son",
"la figlia/daughter",
"il fratello/brother",
"la sorella/sister",
"il nipote/grandson",
"la nipote/granddaughter",
"il nonno/grandfather",
"la nonna/grandmother",
"lo zio/uncle",
"la zia/aunt",
"il cugino/cousin",
"il marito/husband",
"la moglie/wife",
"il genero/son-in-law",
"la nuora/daughter-in-law",
"il suocero/father-in-law",
"la suocera/mother-in-law",
"il cognato/brother-in-law",
"la cognata/sister-in-law",
"il parento/relative",
"il genitoro/parent",
"il gemello/twin",
"la coppia/couple"
]

other_people=[
"il capo/boss",
"l'amico|l'amica/friend",
"il conoscente/acquaintance",
"lo sconosciuto/stranger",
"lo straniero/outsider",
"la paria/outcast",
"il vicino|la vicina/neighbour",
"la coppia/couple",
"il capo/boss",
"il collega/collegue",
"il bambino|la bambina/child",
"il ragazzo/boy",
"la ragazza/girl",
"l'adolescente/teenager",
"l'adulto/adult",
"l'uomo/man",
"la donna/woman"
]

misc_nouns=[
"la zuffa|la rissa/fight",
"l'avversario/opponent",
"il nemico/enemy",
"il lavoro/work",
"il gruppo/group",
"la squadra/team",
"il membro/member",
"la compagnia/company",
"la regola/rule",
"il bacio/kiss"
]

noun.eng_special_conj['man']='men'
noun.eng_special_conj['woman']='women'

#adjective
adjs=[
"cortese/polite",
"scortese|rozzo/rude",
"amichevole/friendly",
"ostile/hostile",
"popolare/popular",
"famoso/famous",
"infame/infamous",
"importante/important",
"timido/shy",
"loquace|ciarliero/talkative",
"solitario/lonely",
"solo/alone",
"simpatico|gentile/nice",
"occupato/busy",
"fidato/reliable",
"imparentato/related"

]





#verb.eng_verbs['raise'] = {'imperfect':'rose', 'perfect': 'risen' }

persons=['1s','2s','3sm','3sf', '1p','2p','3pm','3pf']
subjv_q = phrase.phrase(subj_verbs,person=persons,tempus=['present','perfect'],\
                  post=[phrase.phrase(['parlare','lavorare/work',"combattere/fight","rispondere/answer","ubbidire/obey","mentire|dire_bugie/lie(false)"],\
                                     conj='che',subject=other_people,tempus='subjunctive present'),
                        phrase.phrase(['parlare','lavorare/work',"combattere/fight","rispondere/answer","ubbidire/obey","mentire|dire_bugie/lie(false)"],\
                                     conj='che',person=persons,tempus='subjunctive present')])


intransv_q= phrase.phrase(intrans_verbs,subject=relatives,\
                  tempus=['present','perfect','future','conditional','imperfect'])

pluralv_q= phrase.phrase(plural_verbs,person=['1p','2p','3p'],\
                  tempus=['present','perfect','future','conditional','imperfect'])

transv_q=phrase.phrase(trans_verbs,tempus=['present','perfect','future','conditional','imperfect'],\
                 person=persons,dobj=relatives)

specialv_q =\
    [phrase.phrase("raccontare/tell",tempus=['present','perfect','future','conditional','imperfect'],
                      person=persons,dobj=["la storia|il racconto/story","lo scandalo/scandal","il segreto/secret",]),
    phrase.phrase("allevare/raise",tempus=['present','perfect','future','conditional','imperfect'],
                  person=persons,dobj=["il figlio/son","la figlia/daughter","il bambino|la bambina/child","il ragazzo/boy","la ragazza/girl"]),
    phrase.phrase(["declinare|rifiutare/decline","accettare/accept"],tempus=['present','perfect','future','conditional','imperfect'],
                  person=persons,dobj=[ "l'invito/invitation","l'aiuto/help"])
    ]

nouns_q=phrase.noun_phrase(2*misc_nouns+2*conversation+2*events+other_people+relatives,kind=['sd','si','pd','pi'])

adjs_q=phrase.phrase('essere',person=persons,pred=adjs,tempus=['present'])                 

