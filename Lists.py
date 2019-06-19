#Each race has the following stats, Strength (STR), Athletics (ATH), Wisdom (WIS), Charisma (CHAR), Base health (HP)
raceStats={
    'human': {
        'Name': 'Human',
        'Description':"TODO",
        'STR':6,
        'ATH':6,
        'WIS':6,
        'CHAR':6,
        'HP':60
    },
    'dwarf': {
        'Name': 'Dwarf',
        'Description':"TODO",
        'STR':9,
        'ATH':3,
        'WIS':4,
        'CHAR':5,
        'HP':90
    },
    'elf': {
        'Name': 'Elf',
        'Description':"TODO",
        'STR':4,
        'ATH':8,
        'WIS':6,
        'CHAR':7,
        'HP':50
    },
    'drow': {
        'Name': 'Drow',
        'Description':"TODO",
        'STR':4,
        'ATH':9,
        'WIS':7,
        'CHAR':4,
        'HP':60
    },
    'gnome': {
        'Name': 'Gnome',
        'Description':"TODO",
        'STR':2,
        'ATH':8,
        'WIS':9,
        'CHAR':7,
        'HP':40  
    },
}

classes=('STR','ATH','WIS','CHAR','HP')
classStats={
    'bard':{ #++CHAR,+ATH,HP+0,-WIS,--STR
        'Name':'Bard',
        'STR':-4,
        'ATH':2,
        'WIS':-2,
        'CHAR':4,
        'HP':0
    },
    'rogue':{ #++ATH,+CHAR,HP+0,-STR,--WIS
        'Name':'Rogue',
        'STR':-2,
        'ATH':4,
        'WIS':-4,
        'CHAR':2,
        'HP':0
    },
    'warrior':{ #++STR,+ATH,++HP,-CHAR,--WIS
        'Name':'Warrior',
        'STR':4,
        'ATH':2,
        'WIS':-4,
        'CHAR':-2,
        'HP':1
    },
    'mage':{ #++WIS,+CHAR,--HP,-ATH,--STR
        'Name':'Mage',
        'STR':-4,
        'ATH':-2,
        'WIS':4,
        'CHAR':2,
        'HP':-2
    },
    'tank':{#++STR,+HP,WIS,-CHAR,--ATH
        'Name':'Tank',
        'STR':4,
        'ATH':-4,
        'WIS':0,
        'CHAR':-2,
        'HP':3
    }
}

mainMenu={
    'My Character':'playerDetails',
    'Edit Character':'editPlayer',
    'Random Encounter':'error'
    }