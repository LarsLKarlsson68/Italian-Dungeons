# -*- coding: cp1252 -*-

import phrase, verb, noun

persons=['1s','2s','3sm','3sf', '1p','2p','3pm','3pf']

houses= [
    "l'appartamento/apartment",
    "la casa/house",
    "il caseggiato/block_of flats",
    "la villa/villa"
    ]

rooms= [\
    "la stanza/room",
    "il salotto/living room",
    "lo studio/study",
    "la sala_da pranzo/dining room",
    "la cucina/kitchen",
    "la camera_da letto/bedroom",
    "il bagno/bathroom",
    "la camera_dei bambini/nursery",
    "la lavanderia/utility room",
    "il laboratorio/workshop",
    "l'entrata/hallway",
    "il garage/garage",
    "l'attico/attic",
    "il seminterrato/basement"

    ]
house_parts=[\
    "il muro/wall",
    "la finestra/window",
    "il tetto/roof",
    "il camino/chimney",
    "la tegola/tile",
    "il portone/front door",
    "il portico/porch",
    "il balcone/balcony",
    "la cassetta_per le lettere/letterbox",
    "la scala/staircase",
    "l'ingresso/entrance",
    "il campanello/doorbell",
    "la serratura/lock",
    "la maniglia/handle",
    "l'ascensore/lift",
    "il piano/floor level",
    "il pavimento/floor",
    "il soffitto/ceiling",
    "il caminetto/fireplace",
    "la tappezzeria/wallpaper"    
    ]

house_verbs=[
    "affitare/rent",
    "abitare/live"
    ]


q1 = 20*[ phrase.noun_phrase(rooms+house_parts,kind=['sd','sd','si','pd']) ]+\
     [ phrase.phrase(["affitare/rent","possedere/own"],person=persons,tempus='present',dobj=houses),
       phrase.phrase("abitare/live",person=persons,tempus='present',iobj=phrase.prep_phrase(prep='in',noun=houses) )]

    
systems= [
    "il calorifero/radiator",
    "lo scaldaacqua/bolier",
    "l'acquaio/sink",
    "il rubinetto/tap",
    "la leva/lever",
    "lo scolo/drain",
    "il tappo/plug",
    "la vasca/bathtub",
    "la doccia/shower",
    "il lavandino/sink",
    "il water/water closet",
    "la lampadina/light bulb",
    "la presa/socket",
    "l'interruttore/switch",
    "l'elettricità/electricity",
    "la spina/plug",
    "il filo/wire",
    "il tubo/pipe"       
    ]

furniture = [
    "il quadro/painting",
    "la lampada/lamp",
    "lo specchio/mirror",
    "il vaso/vase",
    "il divano/sofa",
    "la tenda/curtain",
    "la veneziana/venetian blind",
    "il tavolino/coffee table",
    "la poltrona/armchair",
    "il tappeto/carpet",
    "la sedia/chair",
    "il tavolo/table",
    "la tovaglia/table cloth",
    "la libreria/bookshelf",
    "la mensola/shelf",
    "il cassetto/drawer",
    "l'armadio/wardrobe",
    "il cassettone/chest_of drawers",
    "il letto/bed",
    "il materasso/mattress",
    "il copriletto/bedspread",
    "il guanciale/pillow",
    "la gruccia/coat hanger",
    "la sveglia/alarm clock",
    "l'orologio/clock",
    "la federa/pillowcase",
    "il lenzuolo/sheet",
    "la corpetta/blanket",
    "il cuscino/cushion",
    "il lettino/cot",
    "il vasino/potty"    
     ]

appliances= [
    "il forno/oven",
    "la piastra/hob",
    "il forno_a microonde/microwave oven",
    "il tostapane/toaster",
    "la lavastoviglie/dishwasher",
    "il frigorifero/refrigerator",
    "il congelatore/freezer",
    "la lavatrice/washing machine",
    "l'asciugabiancheria/dry tumbler",
    "il ferro_da stiro/iron",
    "l'aspirapolvere/vacuum cleaner",
    "la macchina_da cucire/sewing machine",
    "il televisore/television",
    "il lettore_di DVD/DVD player",
    "il lettore_di CD/CD player",
    "il videoregistratore/video recorder",
    "il telefono/telephone"    
]

q2 = [ phrase.noun_phrase(systems+furniture+appliances,kind=['sd','sd','si','pd']) ]

cleaning_tools=[
    "il secchio/bucket",
    "la scopa_di spugna/mop",
    "la paletta/dust pan",
    "la spazzola/brush",
    "il detergente/detergent",
    "la scopa/broom"
    ]

workshop_tools=[
    "la sega/saw",
    "il trapano/drill",
    "il martello/hammer",
    "il metro/tape measure",
    "il cacciavite/screw driver",
    "il chiodo/nail",
    "la vite/screw",
    "il dado/nut",
    "il penello/brush",
    "la vernice/paint",
    "il paio_di forbici/pair_of scissors",
    "l'ago/needle",
    "il filo/thread",
    "la colla/glue"
    ]

cooking_tools=[
    "la tazza/cup",
    "il piatto/plate",
    "la ciotola/bowl",
    "il bicchiere/glass",
    "il calice_da vino/wine glass",
    "la forchetta/fork",
    "il cucchiaio/spoon",
    "il coltello/knife",
    "la padella/frying pan",
    "la pentola/sauce pan",
    "il tagliere/chopping board",
    "l'apribottiglie/bottle opener",
    "l'apriscatole/can opener",
    "la scodella/mixing bowl",
    "il cavatappi/cork screw",
    "la bottiglia/bottle",
    "la scatola/can"
  ]

hygene_tools=[
    "la spunga/sponge",
    "il sapone/soap",
    "lo spazzolino_da denti/tothbrush",
    "il dentifricio/toothpaste",
    "l'asciugamano/towel",
    "la carta_igienica/toilet roll",
    "il rasio/razor",
    "lo shampoo/shampoo",
    "il pettine/comb"
    ]
    

q3 = [ phrase.noun_phrase(workshop_tools+cooking_tools+hygene_tools,kind=['sd','sd','si','pd']) ]

garden = [
    "il giardino/garden",
    "l'orto/vegetable garden",
    "il prato/lawn",
    "il recinto/fence",
    "la siepe/hedge",
    "il sentiero/path",
    "l'aiuola/flower bed",
    "il cancello/gate",
    "l'erba/grass",
    "la pianta_da vaso/potted plant",
    "l'albero/tree",
    "la vanga/spade",
    "il rastrello/rake",
    "il tosaerba/lawn mower",
    "la carriola/wheel barrow",
    "la pompa_di giardino/water hose",
    "l'annaffiatoio/watering can",
    "la pala/showel",
    "la scala/ladder"
    ]



misc=[
    "la biancheria/laundry",
    "l'affitta/rent"
    ]
q4 = [ phrase.noun_phrase(garden+misc,kind=['sd','sd','si','pd']) ]


cooking_verbs= [
    "apparecchiare/lay_the table",
    "servire/serve",
    "affettare/slice",
    "mescolare/mix",
    "bollire/boil",
    "friggere/fry",
    "cuocere_al forno/bake",
    "arrostire/roast",
    "congelare/freeze",
    "scongelare/defrost",
    "tagliare/cut",
    "cucinare|cuocere/cook"
    ]


hygene_verbs=[
    "farsi0_la doccia/take_a shower",
    "farsi0_il bagno/take_a bath",
    "radersi0|farsi0_la barba/shave",
    "pettinare/comb"
    ]

cleaning_verbs=[
    "fare_il bucato/do_the laundry"
    "caricare/load", #dish washer etc
    "scaricare/unload",
    "pulire/clean",
    "lavare/wash",
    "asciugare/wipe",
    "spazzare/sweep",
    "spolverare/dust",
    "spazzolare/brush",
    ]

tool_verbs=[
    "aggiustare|riparare/mend",
    "segare/saw",
    "forare/drill",
    "martellare/hammer",
    "avvitare/screw",
    "dipingere/paint"
    ]

garden_verbs=[
    "tagliare_l'erba/mowe_the lawn",
    "scavare/dig",
    "seminare/sow",
    "annafiare/water",
    "spuntare/trim",
    "cogliere/pick",
    "coltivare|fare_crescere/grow"
    ]

q5= [ phrase.phrase(verb=cleaning_verbs[3:]+["dipingere/paint"],person=persons,tempus='present',
        dobj=["il portico/porch", "il balcone/balcony", "il pavimento/floor"]+rooms),
      phrase.phrase(verb=hygene_verbs+["fare_il bucato/do_the laundry","tagliare_l'erba/mow_the lawn"],person=persons,tempus='present'),
      phrase.phrase(verb=['caricare/load',"scaricare/unload","aggiustare|riparare/mend"],
                    person=persons,tempus='present',
                    dobj=["la lavastoviglie/dishwasher","la lavatrice/washing machine","l'asciugabiancheria/dry tumbler"]),
      phrase.phrase(verb=tool_verbs[1:]+["scavare/dig"],person=persons,tempus='present'),
      phrase.phrase(verb=garden_verbs[2:],person=persons,tempus='present',
                    dobj=["la siepe/hedge", "la pianta_da vaso/potted plant","l'albero/tree","il fiore/flower", "la verdura/vegetable"]),
       phrase.phrase(verb=cooking_verbs,person=persons,tempus='present')
    ]
      

house_adjectives = [
    "rotto/broken",
    "sporco/dirty",
    "pulito/clean",
    "polveroso/dusty",
    "disordinato/messy",
    "in ordine/orderly",
    "umido|bagnato/wet",
    "secco|asciutto/dry"
    ]

q6 = [phrase.phrase(verb='essere',subject=rooms,pred=house_adjectives,tempus='present')]    
    
##import italian_dungeons
##
##g = italian_dungeons.FakeGame([q1,q2,q3,q4,q5,q6])
##
##for q in [q1,q2,q3,q4,q5,q6]:        
##    for i in range(10):
##        qx = phrase.choice_if_list(q).choice()
##        print(qx.it(), qx.eng())
##    print('-----------------------------')
##    
                            
