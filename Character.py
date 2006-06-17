# Character.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

__all__ = [
  'AllBonusList', 'ClassList', 'RaceList', 'Races', 'Realms', 
]

from tuple2 import * 
from dict2 import * 

Realms = t2(('Albion', 'Hibernia', 'Midgard'))

AllBonusList = { 

  'Albion' : {

    'Armsman' : {
        'All Melee Weapon Skills' : ('Crush', 'Slash', 'Thrust', 'Polearm', 'Two Handed',),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre', 'Highlander', 'Inconnu', 'Saracen',)),
    },

    'Cabalist' : {
        'All Spell Lines' : ('Body Magic', 'Matter Magic', 'Spirit Magic',), 
        'All Magic Skills' : ('Body Magic', 'Matter Magic', 'Spirit Magic',),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre', 'Inconnu', 'Saracen',)),
        'Acuity' : ('Intelligence',),
    },

    'Cleric' : {
        'All Magic Skills' : ('Rejuvenation', 'Enhancement', 'Smite',),
        'Races' : t2(('Avalonian', 'Briton', 'Highlander',)),
        'Acuity' : ('Piety',),
    },

    'Friar' : {
        'All Magic Skills' : ('Rejuvenation', 'Enhancement',),
        'All Melee Weapon Skills' : ('Staff',),
        'Other Skills' : ('Parry',),
        'Races' : t2(('Briton',)),
        'Acuity' : ('Piety',),
    },

    'Heretic' : {
        'All Magic Skills' : ('Rejuvenation', 'Enhancement',),
        'All Melee Weapon Skills' : ('Crush', 'Flexible',),
        'Other Skills' : ('Shield',),
        'Races' : t2(('Avalonian', 'Briton', 'Inconnu',)),
        'Acuity' : ('Piety',),
    },

    'Infiltrator' : {
        'All Melee Weapon Skills' : ('Slash', 'Thrust',),
        'All Dual Wield Skills' : ('Dual Wield',),
        'Other Skills' : ('Critical Strike', 'Envenom', 'Stealth',),
        'Races' : t2(('Briton', 'Inconnu', 'Saracen',)),
    },

    'Mercenary' : {
        'All Melee Weapon Skills' : ('Crush', 'Slash', 'Thrust',),
        'All Dual Wield Skills' : ('Dual Wield',),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre', 'Highlander', 'Inconnu', 'Saracen',)),
    },

    'Minstrel' : {
        'All Magic Skills' : ('Instruments',),
        'All Melee Weapon Skills' : ('Slash', 'Thrust',),
        'Other Skills' : ('Stealth',),
        'Races' : t2(('Briton', 'Highlander', 'Saracen',)),
        'Acuity' : ('Charisma',),
    },

    'Necromancer' : {
        'All Spell Lines' : ('Deathsight', 'Death Servant', 'Painworking',), 
        'All Magic Skills' : ('Deathsight', 'Death Servant', 'Painworking',),
        'Races' : t2(('Briton', 'Inconnu', 'Saracen',)),
        'Acuity' : ('Intelligence',),
    },

    'Paladin' : {
        'All Melee Weapon Skills' : ('Crush', 'Slash', 'Thrust', 'Two Handed',),
        'Other Skills' : ('Parry', 'Shield',),
        'No Skill Effect' : ('Chants',),
        'Races' : t2(('Avalonian', 'Briton', 'Highlander', 'Saracen',)),
        'Acuity' : ('Piety',),
    },

    'Reaver' : {
        'All Magic Skills' : ('Soulrending',),
        'All Melee Weapon Skills' : ('Crush', 'Flexible', 'Slash', 'Thrust',),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Briton', 'Inconnu', 'Saracen',)),
        'Acuity' : ('Piety',),
    },

    'Scout' : {
        'All Melee Weapon Skills' : ('Slash', 'Thrust',),
        'All Archery Skills' : ('Longbow',),
        'Other Skills' : ('Stealth', 'Shield',),
        'Races' : t2(('Briton', 'Highlander', 'Inconnu', 'Saracen',)),
    },

    'Sorcerer' : {
        'All Spell Lines' : ('Body Magic', 'Mind Magic', 'Matter Magic',),
        'All Magic Skills' : ('Body Magic', 'Mind Magic', 'Matter Magic',),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre', 'Inconnu', 'Saracen',)),
        'Acuity' : ('Intelligence',),
    },

    'Theurgist' : {
        'All Spell Lines' : ('Earth Magic', 'Cold Magic', 'Wind Magic',),
        'All Magic Skills' : ('Earth Magic', 'Cold Magic', 'Wind Magic',),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre',)),
        'Acuity' : ('Intelligence',),
    },

    'Wizard' : {
        'All Spell Lines' : ('Earth Magic', 'Cold Magic', 'Fire Magic',),
        'All Magic Skills' : ('Earth Magic', 'Cold Magic', 'Fire Magic',),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre',)),
        'Acuity' : ('Intelligence',),
    },
  },

  'Hibernia' : {

    'Animist' : {
        'All Spell Lines' : ('Arboreal Path', 'Creeping Path', 'Verdant Path',),
        'All Magic Skills' : ('Arboreal Path', 'Creeping Path', 'Verdant Path',),
        'Races' : t2(('Celt', 'Firbolg', 'Sylvan',)),
        'Acuity' : ('Intelligence',),
    },

    'Bainshee' : {
        'All Spell Lines' : ('Ethereal Shriek', 'Phantasmal Wail', 'Spectral Guard',),
        'All Magic Skills' : ('Ethereal Shriek', 'Phantasmal Wail', 'Spectral Guard',),
        'Races' : t2(('Celt', 'Elf', 'Lurikeen',)),
        'Acuity' : ('Intelligence',),
    },

    'Bard' : {
        'All Magic Skills' : ('Regrowth', 'Nurture', 'Music',),
        'All Melee Weapon Skills' : ('Blades', 'Blunt',),
        'Races' : t2(('Celt', 'Firbolg',)),
        'Acuity' : ('Charisma',),
    },

    'Blademaster' : {
        'All Melee Weapon Skills' : ('Blades', 'Blunt', 'Piercing',),
        'All Dual Wield Skills' : ('Celtic Dual',),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Celt', 'Elf', 'Firbolg', 'Shar',)),
    },

    'Champion' : {
        'All Magic Skills' : ('Valor',),
        'All Melee Weapon Skills' : ('Blades', 'Blunt', 'Piercing', 'Large Weaponry',),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Celt', 'Elf', 'Lurikeen', 'Shar',)),
        'Acuity' : ('Intelligence',),
    },

    'Druid' : {
        'All Magic Skills' : ('Regrowth', 'Nature', 'Nurture',),
        'Races' : t2(('Celt', 'Firbolg', 'Sylvan',)),
        'Acuity' : ('Empathy',),
    },

    'Eldritch' : {
        'All Spell Lines' : ('Light', 'Mana', 'Void',),
        'All Magic Skills' : ('Light', 'Mana', 'Void',),
        'Races' : t2(('Elf', 'Lurikeen',)),
        'Acuity' : ('Intelligence',),
    },

    'Enchanter' : {
        'All Spell Lines' : ('Light', 'Mana', 'Enchantments',),
        'All Magic Skills' : ('Light', 'Mana', 'Enchantments',),
        'Races' : t2(('Elf', 'Lurikeen',)),
        'Acuity' : ('Intelligence',),
    },

    'Mentalist' : {
        'All Spell Lines' : ('Light', 'Mana', 'Mentalism',),
        'All Magic Skills' : ('Light', 'Mana', 'Mentalism',),
        'Races' : t2(('Celt', 'Elf', 'Lurikeen', 'Shar',)),
        'Acuity' : ('Intelligence',),
    },

    'Hero' : {
        'All Melee Weapon Skills' : ('Blades', 'Blunt', 'Celtic Spear', 'Large Weaponry', 'Piercing',),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Celt', 'Firbolg', 'Lurikeen', 'Shar', 'Sylvan',)),
    },

    'Nightshade' : {
        'All Melee Weapon Skills' : ('Blades', 'Piercing',),
        'All Dual Wield Skills' : ('Celtic Dual',),
        'Other Skills' : ('Critical Strike', 'Envenom', 'Stealth',),
        'Races' : t2(('Elf', 'Lurikeen',)),
    },

    'Ranger' : {
        'All Melee Weapon Skills' : ('Blades', 'Piercing',),
        'All Dual Wield Skills' : ('Celtic Dual',),
        'All Archery Skills' : ('Recurve Bow',),
        'Other Skills' : ('Stealth','Pathfinding',),
        'Races' : t2(('Celt', 'Elf', 'Lurikeen', 'Shar',)),
    },

    'Valewalker' : {
        'All Magic Skills' : ('Arboreal Path',),
        'All Melee Weapon Skills' : ('Scythe',),
        'Other Skills' : ('Parry',),
        'Races' : t2(('Celt', 'Firbolg', 'Sylvan',)),
        'Acuity' : ('Intelligence',),
    },

    'Vampiir' : {
        'All Magic Skills' : ('Dementia', 'Shadow Mastery', 'Vampiiric Embrace',),
        'All Melee Weapon Skills' : ('Piercing',),
        'Races' : t2(('Celt', 'Lurikeen', 'Shar',)),
    },

    'Warden' : {
        'All Magic Skills' : ('Nurture', 'Regrowth',),
        'All Melee Weapon Skills' : ('Blades', 'Blunt',),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Celt', 'Firbolg', 'Sylvan',)),
        'Acuity' : ('Empathy',),
    },
  },

  'Midgard' : {

    'Berserker' : {
        'All Melee Weapon Skills' : ('Axe', 'Hammer', 'Sword',),
        'All Dual Wield Skills' : ('Left Axe',),
        'Other Skills' : ('Parry',),
        'Races' : t2(('Dwarf', 'Norseman', 'Troll', 'Valkyn',)),
    },

    'Bonedancer' : {
        'All Spell Lines' : ('Darkness', 'Suppression', 'Bone Army',),
        'All Magic Skills' : ('Darkness', 'Suppression', 'Bone Army',),
        'Races' : t2(('Kobold', 'Troll', 'Valkyn',)),
        'Acuity' : ('Piety',),
    },

    'Healer' : {
        'All Magic Skills' : ('Augmentation', 'Mending',),
        'No Skill Effect' : ('Pacification',),
        'Races' : t2(('Dwarf', 'Frostalf', 'Norseman',)),
        'Acuity' : ('Piety',),
    },

    'Hunter' : {
        'All Magic Skills' : ('Beastcraft',),
        'All Melee Weapon Skills' : ('Spear', 'Sword',),
        'All Archery Skills' : ('Composite Bow',),
        'Other Skills' : ('Stealth',),
        'Races' : t2(('Dwarf', 'Frostalf', 'Kobold', 'Norseman', 'Valkyn',)),
    },

    'Runemaster' : {
        'All Spell Lines' : ('Darkness', 'Suppression', 'Runecarving',),
        'All Magic Skills' : ('Darkness', 'Suppression', 'Runecarving',),
        'Races' : t2(('Dwarf', 'Frostalf', 'Kobold', 'Norseman',)),
        'Acuity' : ('Piety',),
    },

    'Savage' : {
        'All Melee Weapon Skills' : ('Sword', 'Axe', 'Hammer', 'Hand To Hand',),
        'Other Skills' : ('Parry',),
        'No Skill Effect' : ('Savagery',),
        'Races' : t2(('Dwarf', 'Kobold', 'Norseman', 'Troll', 'Valkyn',)),
    },

    'Shadowblade' : {
        'All Melee Weapon Skills' : ('Sword', 'Axe',),
        'All Dual Wield Skills' : ('Left Axe',),
        'Other Skills' : ('Critical Strike', 'Envenom', 'Stealth',),
        'Races' : t2(('Kobold', 'Norseman', 'Valkyn',)),
    },

    'Shaman' : {
        'All Magic Skills' : ('Augmentation', 'Cave Magic', 'Mending',),
        'Races' : t2(('Frostalf', 'Kobold', 'Troll',)),
        'Acuity' : ('Piety',),
    },

    'Skald' : {
        'All Magic Skills' : ('Battlesongs',),
        'All Melee Weapon Skills' : ('Sword', 'Hammer', 'Axe',),
        'Other Skills' : ('Parry',),
        'Races' : t2(('Dwarf', 'Kobold', 'Norseman', 'Troll',)),
        'Acuity' : ('Charisma',),
    },

    'Spiritmaster' : {
        'All Spell Lines' : ('Darkness', 'Suppression', 'Summoning',),
        'All Magic Skills' : ('Darkness', 'Suppression', 'Summoning',),
        'Races' : t2(('Frostalf', 'Kobold', 'Norseman',)),
        'Acuity' : ('Piety',),
    },

    'Thane' : {
        'All Magic Skills' : ('Stormcalling',),
        'All Melee Weapon Skills' : ('Sword', 'Hammer', 'Axe',),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Dwarf', 'Frostalf', 'Norseman', 'Troll',)),
        'Acuity' : ('Piety',),
    },

    'Valkyrie' : {
        'All Magic Skills' : ('Odin\'s Will',),
        'All Melee Weapon Skills' : ('Spear', 'Sword',),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Dwarf', 'Frostalf', 'Norseman',)),
        'Acuity' : ('Piety',),
    },

    'Warlock' : {
        'All Spell Lines' : ('Cursing',),
        'All Magic Skills' : ('Cursing', 'Hexing',),
        'No Skill Effect' : ('Witchcraft',),
        'Races' : t2(('Frostalf', 'Kobold', 'Norseman',)),
        'Acuity' : ('Piety',),
    },

    'Warrior' : {
        'All Melee Weapon Skills' : ('Sword', 'Hammer', 'Axe',),
        'Other Skills' : ('Parry', 'Shield',),
        'No Skill Effect' : ('Thrown Weapons',),
        'Races' : t2(('Dwarf', 'Kobold', 'Norseman', 'Troll', 'Valkyn',)),
    },
  }, 
}


# Make ClassList[realm] from AllBonusList[realm] class names
#
# Make AllBonusList['All']['class'] combined all-realms list
#
# Make AllBonusList['Hash']{'class'} dictionary for each class
#
ClassList = {}
ClassList['All'] = []

AllBonusList['All'] = {}

for realm in Realms:
  classes = AllBonusList[realm].keys()
  classes.sort()
  ClassList[realm] = t2(classes)
  for charclass in AllBonusList[realm]:
    skills = []
    for listname in ('All Magic Skills', 'All Melee Weapon Skills',
                     'All Dual Wield Skills', 'All Archery Skills', 
                     'Other Skills', ):
        if not AllBonusList[realm][charclass].has_key(listname):
            AllBonusList[realm][charclass][listname] = ()
        skills.extend(AllBonusList[realm][charclass][listname])

    AllBonusList[realm][charclass]['Skills Hash'] = d2(dict.fromkeys(skills))

    for listname in ('All Spell Lines', 'No Skill Effect', 'Acuity', ):
        if not AllBonusList[realm][charclass].has_key(listname):
            AllBonusList[realm][charclass][listname] = ()

    AllBonusList[realm][charclass]['Focus Hash'] \
        = d2(dict.fromkeys(AllBonusList[realm][charclass]['All Spell Lines']))

    if len(AllBonusList[realm][charclass]['All Spell Lines']):
      AllBonusList[realm][charclass]['All Focus'] = t2(('All Spell Lines',) +
                         AllBonusList[realm][charclass]['All Spell Lines'])
    else:
      AllBonusList[realm][charclass]['All Focus'] = t2()

    skills.sort()
    if len(AllBonusList[realm][charclass]['All Melee Weapon Skills']) > 0:
      skills.insert(0, 'All Melee Weapon Skills')
    if len(AllBonusList[realm][charclass]['All Magic Skills']) > 0:
      skills.insert(0, 'All Magic Skills')
    AllBonusList[realm][charclass]['All Skills'] = t2(skills)
    AllBonusList[realm][charclass] = d2(AllBonusList[realm][charclass])
  AllBonusList[realm] = d2(AllBonusList[realm])
  AllBonusList['All'].update(AllBonusList[realm])
  ClassList['All'].extend(ClassList[realm])
ClassList['All'].sort()

ClassList['All'] = t2(ClassList['All'])
ClassList = d2(ClassList)

AllBonusList['All'] = d2(AllBonusList['All'])
AllBonusList = d2(AllBonusList)


Races = {

  'Albion' : d2({
    'Avalonian' : d2({
      'Resists' : d2({'Slash'  : 3, 'Crush'  : 2, 'Spirit' : 5}),
      'Stats' :   (45, 45, 60, 70, 80, 60, 60, 60),
    }),
    'Briton' : d2({
      'Resists' : d2({'Slash'  : 3, 'Crush'  : 2, 'Spirit' : 5}),
      'Stats' :   (60, 60, 60, 60, 60, 60, 60, 60),
    }),
    'Half Ogre' : d2({
      'Resists' : d2({'Slash'  : 3, 'Thrust' : 2, 'Matter' : 5}),
      'Stats' :   (90, 70, 40, 40, 60, 60, 60, 60),
    }),
    'Highlander' : d2({
      'Resists' : d2({'Crush'  : 3, 'Slash'  : 2, 'Cold'   : 5}),
      'Stats' :   (70, 70, 50, 50, 60, 60, 60, 60),
    }),
    'Inconnu' : d2({
      'Resists' : d2({'Thrust' : 3, 'Crush'  : 2, 'Heat'   : 5, 'Spirit' : 5}),
      'Stats' :   (50, 60, 70, 50, 70, 60, 60, 60),
    }),
    'Saracen' : d2({
      'Resists' : d2({'Thrust' : 3, 'Slash'  : 2, 'Heat'   : 5}),
      'Stats' :   (50, 50, 80, 60, 60, 60, 60, 60),
    }),
  }),

  'Hibernia' : d2({
    'Celt' : d2({
      'Resists' : d2({'Slash'  : 3, 'Crush'  : 2, 'Spirit' : 5}),
      'Stats' :   (60, 60, 60, 60, 60, 60, 60, 60),
    }),
    'Elf' : d2({
      'Resists' : d2({'Thrust' : 3, 'Slash'  : 2, 'Spirit' : 5}),
      'Stats' :   (40, 40, 75, 75, 70, 60, 60, 60),
    }),
    'Firbolg' : d2({
      'Resists' : d2({'Crush'  : 3, 'Slash'  : 2, 'Heat'   : 5}),
      'Stats' :   (90, 60, 40, 40, 60, 60, 70, 60),
    }),
    'Lurikeen' : d2({
      'Resists' : d2({'Crush'  : 5, 'Energy' : 5}),
      'Stats' :   (40, 40, 80, 80, 60, 60, 60, 60),
    }),
    'Shar' : d2({
      'Resists' : d2({'Crush'  : 5, 'Energy' : 5}),
      'Stats' :   (60, 80, 50, 50, 60, 60, 60, 60),
    }),
    'Sylvan' : d2({
      'Resists' : d2({'Crush'  : 3, 'Thrust' : 2, 'Energy' : 5, 'Matter' : 5}),
      'Stats' :   (70, 60, 55, 45, 70, 60, 60, 60),
    }),
  }),

  'Midgard' : d2({
    'Dwarf' : d2({
      'Resists' : d2({'Thrust' : 3, 'Slash'  : 2, 'Body'   : 5}),
      'Stats' :   (60, 80, 50, 50, 60, 60, 60, 60),
    }),
    'Frostalf' : d2({
      'Resists' : d2({'Thrust' : 3, 'Slash'  : 2, 'Spirit' : 5}),
      'Stats' :   (55, 55, 55, 60, 60, 75, 60, 60),
    }),
    'Kobold' : d2({
      'Resists' : d2({'Crush'  : 5, 'Energy' : 5}),
      'Stats' :   (50, 50, 70, 70, 60, 60, 60, 60),
    }),
    'Norseman' : d2({
      'Resists' : d2({'Slash'  : 3, 'Crush'  : 2, 'Cold'   : 5}),
      'Stats' :   (70, 70, 50, 50, 60, 60, 60, 60),
    }),
    'Troll' : d2({
      'Resists' : d2({'Slash'  : 3, 'Thrust' : 2, 'Matter' : 5}),
      'Stats' :   (100, 70, 35, 35, 60, 60, 60, 60),
    }),
    'Valkyn' : d2({
      'Resists' : d2({'Slash'  : 3, 'Thrust' : 2, 'Cold'   : 5, 'Body'   : 5}),
      'Stats' :   (55, 45, 65, 75, 60, 60, 60, 60),
    }),
  }),
}

Races['All'] = {}
RaceList = {}
RaceList['All'] = []

for realm in Realms:
  for charclass in Races[realm]:
    Races['All'][charclass] = Races[realm][charclass]
  RaceList[realm] = Races[realm].keys()
  RaceList[realm].sort()
  RaceList[realm] = t2(RaceList[realm])
  RaceList['All'].extend(Races[realm])

RaceList['All'].sort()
RaceList['All'] = t2(RaceList['All'])
RaceList = d2(RaceList)

Races['All'] = d2(Races['All'])
Races = d2(Races)


ServerCodes = d2({
     '85' : 'Bedevere',
    '100' : 'Bors',
     '27' : 'Ector',
    '135' : 'Gaheris',
     '55' : 'Galahad',
    '220' : 'Gareth',
     '95' : 'Gawaine',
     '80' : 'Gwinevere',
    '130' : 'Igraine',
    '105' : 'Iseult',
    '120' : 'Kay',
     '60' : 'Lancelot',
    '192' : 'Lamorak',
     '75' : 'Merlin',
    '140' : 'Mordred',
     '90' : 'Morgan Le Fey',
    '115' : 'Nimue',
     '70' : 'Palomides',
    '110' : 'Pellinor',
     '50' : 'Pendragon',
     '51' : 'Hector',
     '65' : 'Percival',
    '125' : 'Tristan',

#Euro
     '33' : 'Excalibur',
    '177' : 'Prydwen',
     '45' : 'Avalon',
    '153' : 'Dartmoor',
     '11' : 'Lyonesse',
    '134' : 'Logres',
     '14' : 'Stonehenge',
     '34' : 'Broceliande',
     '12' : 'Ys',
    '139' : 'Orcanie',
    '171' : 'Carnac',
    '163' : 'Cumbria',
    '103' : 'Deira',
    '148' : 'Gorr',
    '147' : 'Camlann',
    '145' : 'Akatsuki', 
     '20' : 'Glastonbury',
})


if __name__ == "__main__":
    pass
    #import gnosis.xml.pickle
    #constants = {}
    #for v in __all__:
    #    constants[v] = locals()[v]
    #print gnosis.xml.pickle.dumps(constants)
