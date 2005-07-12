# constants.py: Dark Age of Camelot Spellcrafting Calculator
# See http://www.ugcs.caltech.edu/~jlamanna/daoc/sccalc/index.html for updates

# Copyright (C) 2003,  James Lamanna (jlamanna@ugcs.caltech.edu)

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

ScVersion = "Kort 1.42b + Ehrayn/patch 1.0.7"


Realms = ['Albion', 'Hibernia', 'Midgard']


AllBonusList = { 

  'Albion' : {

    'Armsman' : {
        'All Spell Lines' : [], 
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Crush', 'Slash', 'Thrust', 'Polearm', 'Two Handed'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry', 'Shield'],
        'Acuity' : [] },

    'Cabalist' : {
        'All Spell Lines' : ['Body Magic', 'Matter Magic', 'Spirit Magic'], 
        'All Magic Skills' : ['Body Magic', 'Matter Magic', 'Spirit Magic'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Intelligence'] },

    'Cleric' : {
        'All Spell Lines' : [], 
        'All Magic Skills' : ['Rejuvenation', 'Enhancement', 'Smite'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Piety'] },

    'Friar' : {
        'All Spell Lines' : [], 
        'All Magic Skills' : ['Rejuvenation', 'Enhancement'],
        'All Melee Weapon Skills' : ['Staff'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry'],
        'Acuity' : ['Piety'] },

    'Heretic' : {
        'All Spell Lines' : [], 
        'All Magic Skills' : ['Rejuvenation', 'Enhancement'],
        'All Melee Weapon Skills' : ['Crush', 'Flexible'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Shield'],
        'Acuity' : ['Piety'] },

    'Infiltrator' : {
        'All Spell Lines' : [], 
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Slash', 'Thrust'],
        'All Dual Wield Skills' : ['Dual Wield'],
        'All Archery Skills' : [],
        'Other Skills' : ['Critical Strike', 'Envenom', 'Stealth'],
        'Acuity' : [] },

    'Mercenary' : {
        'All Spell Lines' : [], 
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Crush', 'Slash', 'Thrust'],
        'All Dual Wield Skills' : ['Dual Wield'],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry', 'Shield'],
        'Acuity' : [] },

    'Minstrel' : {
        'All Spell Lines' : [], 
        'All Magic Skills' : ['Instruments'],
        'All Melee Weapon Skills' : ['Slash', 'Thrust'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Stealth'],
        'Acuity' : ['Charisma'] },

    'Necromancer' : {
        'All Spell Lines' : ['Deathsight', 'Death Servant', 
        'Painworking'], 
        'All Magic Skills' : ['Deathsight', 'Death Servant', 'Painworking'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Intelligence'] },

    'Paladin' : {
        'All Spell Lines' : [],
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Crush', 'Slash', 'Thrust', 'Two Handed'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry', 'Shield'],
        'No Skill Effect' : ['Chants'],
        'Acuity' : ['Piety'] },

    'Reaver' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Soulrending'],
        'All Melee Weapon Skills' : ['Crush', 'Flexible', 'Slash', 'Thrust'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry', 'Shield'],
        'Acuity' : ['Piety'] },

    'Scout' : {
        'All Spell Lines' : [],
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Slash', 'Thrust'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : ['Longbow'],
        'Other Skills' : ['Stealth', 'Shield'],
        'Acuity' : [] },

    'Sorcerer' : {
        'All Spell Lines' : ['Body Magic', 'Mind Magic', 'Matter Magic'],
        'All Magic Skills' : ['Body Magic', 'Matter Magic'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'No Skill Effect' : ['Mind Magic'],
        'Acuity' : ['Intelligence'] },

    'Theurgist' : {
        'All Spell Lines' : ['Earth Magic', 'Cold Magic', 'Wind Magic'],
        'All Magic Skills' : ['Earth Magic', 'Cold Magic', 'Wind Magic'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Intelligence'] },

    'Wizard' : {
        'All Spell Lines' : ['Earth Magic', 'Cold Magic', 'Fire Magic'],
        'All Magic Skills' : ['Earth Magic', 'Cold Magic', 'Fire Magic'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Intelligence'] } 
  },

  'Hibernia' : {

    'Animist' : {
        'All Spell Lines' : ['Arboreal Path', 'Creeping Path', 'Verdant Path'],
        'All Magic Skills' : ['Arboreal Path', 'Creeping Path', 'Verdant Path'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Intelligence'] },

    'Bainshee' : {
        'All Spell Lines' : ['Ethereal Shriek', 'Phantasmal Wail', 'Spectral Guard'],
        'All Magic Skills' : ['Ethereal Shriek', 'Phantasmal Wail', 'Spectral Guard'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Intelligence'] },

    'Bard' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Regrowth', 'Nurture', 'Music'],
        'All Melee Weapon Skills' : ['Blades', 'Blunt'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Charisma'] },

    'Blademaster' : {
        'All Spell Lines' : [],
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Blades', 'Blunt', 'Piercing'],
        'All Dual Wield Skills' : ['Celtic Dual'],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry', 'Shield'],
        'Acuity' : [] },

    'Champion' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Valor'],
        'All Melee Weapon Skills' : ['Blades', 'Blunt', 'Piercing', 'Large Weaponry'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry', 'Shield'],
        'Acuity' : ['Intelligence'] },

    'Druid' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Regrowth', 'Nature', 'Nurture'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Empathy'] },

    'Eldritch' : {
        'All Spell Lines' : ['Light', 'Mana', 'Void'],
        'All Magic Skills' : ['Light', 'Mana', 'Void'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Intelligence'] },

    'Enchanter' : {
        'All Spell Lines' : ['Light', 'Mana', 'Enchantments'],
        'All Magic Skills' : ['Light', 'Mana', 'Enchantments'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Intelligence'] },

    'Mentalist' : {
        'All Spell Lines' : ['Light', 'Mana', 'Mentalism'],
        'All Magic Skills' : ['Light', 'Mana', 'Mentalism'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Intelligence'] },

    'Hero' : {
        'All Spell Lines' : [],
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Blades', 'Blunt', 'Celtic Spear', 'Large Weaponry', 'Piercing'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry', 'Shield'],
        'Acuity' : [] },

    'Nightshade' : {
        'All Spell Lines' : [],
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Blades', 'Piercing'],
        'All Dual Wield Skills' : ['Celtic Dual'],
        'All Archery Skills' : [],
        'Other Skills' : ['Critical Strike', 'Envenom', 'Stealth'],
        'Acuity' : [] },

    'Ranger' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Pathfinding'],
        'All Melee Weapon Skills' : ['Blades', 'Piercing'],
        'All Dual Wield Skills' : ['Celtic Dual'],
        'All Archery Skills' : ['Recurve Bow'],
        'Other Skills' : ['Stealth'],
        'Acuity' : [] },

    'Valewalker' : {
        'All Spell Lines' : ['Arboreal Path'],
        'All Magic Skills' : ['Arboreal Path'],
        'All Melee Weapon Skills' : ['Scythe'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry'],
        'Acuity' : ['Intelligence'] },

    'Vampiir' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Dementia', 'Shadow Mastery', 'Vampiiric Embrace'],
        'All Melee Weapon Skills' : ['Piercing'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : [] },

    'Warden' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Nurture', 'Regrowth'],
        'All Melee Weapon Skills' : ['Blades', 'Blunt'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry'],
        'Acuity' : ['Empathy'] } 
  },

  'Midgard' : {

    'Berserker' : {
        'All Spell Lines' : [],
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Axe', 'Hammer', 'Sword'],
        'All Dual Wield Skills' : ['Left Axe'],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry'],
        'Acuity' : [] },

    'Bonedancer' : {
        'All Spell Lines' : ['Darkness', 'Suppression', 'Bone Army'],
        'All Magic Skills' : ['Darkness', 'Suppression', 'Bone Army'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Piety'] },

    'Healer' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Augmentation', 'Mending'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'No Skill Effect' : ['Pacification'],
        'Acuity' : ['Piety'] },

    'Hunter' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Beastcraft'],
        'All Melee Weapon Skills' : ['Spear', 'Sword'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : ['Composite Bow'],
        'Other Skills' : ['Stealth'],
        'Acuity' : [] },

    'Runemaster' : {
        'All Spell Lines' : ['Darkness', 'Suppression', 'Runecarving'],
        'All Magic Skills' : ['Darkness', 'Suppression', 'Runecarving'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Piety'] },

    'Savage' : {
        'All Spell Lines' : [],
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Sword', 'Axe', 'Hammer', 'Hand To Hand'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry'],
        'No Skill Effect' : ['Savagery'],
        'Acuity' : [] },

    'Shadowblade' : {
        'All Spell Lines' : [],
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Sword', 'Axe'],
        'All Dual Wield Skills' : ['Left Axe'],
        'All Archery Skills' : [],
        'Other Skills' : ['Critical Strike', 'Envenom', 'Stealth'],
        'Acuity' : [] },

    'Shaman' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Augmentation', 'Cave Magic', 'Mending'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Piety'] },

    'Skald' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Battlesongs'],
        'All Melee Weapon Skills' : ['Sword', 'Hammer', 'Axe'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry'],
        'Acuity' : ['Charisma'] },

    'Spiritmaster' : {
        'All Spell Lines' : ['Darkness', 'Suppression', 'Summoning'],
        'All Magic Skills' : ['Darkness', 'Suppression', 'Summoning'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Piety'] },

    'Thane' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Stormcalling'],
        'All Melee Weapon Skills' : ['Sword', 'Hammer', 'Axe'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry', 'Shield'],
        'Acuity' : ['Piety'] },

    'Valkyrie' : {
        'All Spell Lines' : [],
        'All Magic Skills' : ['Odin\'s Will'],
        'All Melee Weapon Skills' : ['Spear', 'Sword'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry', 'Shield'],
        'Acuity' : ['Piety'] },

    'Warlock' : {
        'All Spell Lines' : ['Cursing'],
        'All Magic Skills' : ['Cursing', 'Hexing', 'Witchcraft'],
        'All Melee Weapon Skills' : [],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : [],
        'Acuity' : ['Piety'] },

    'Warrior' : {
        'All Spell Lines' : [],
        'All Magic Skills' : [],
        'All Melee Weapon Skills' : ['Sword', 'Hammer', 'Axe'],
        'All Dual Wield Skills' : [],
        'All Archery Skills' : [],
        'Other Skills' : ['Parry', 'Shield'],
        'No Skill Effect' : ['Thrown Weapons'],
        'Acuity' : [] } 
  } 
}

# Make ClassList[realm] from AllBonusList[realm] class names
#
# Make AllBonusList['All']['class'] combined all-realms list
#
# Make AllBonusList['Hash']{'class'} dictionary for each class
#
ClassList = { }
ClassList['All'] = []
AllBonusList['All'] = {}
for realm in Realms:
  ClassList[realm] = AllBonusList[realm].keys()
  ClassList[realm].sort()
  for charclass in AllBonusList[realm]:
    list = []
    list.extend(AllBonusList[realm][charclass]['All Magic Skills'])
    list.extend(AllBonusList[realm][charclass]['All Melee Weapon Skills'])
    list.extend(AllBonusList[realm][charclass]['All Dual Wield Skills'])
    list.extend(AllBonusList[realm][charclass]['All Archery Skills'])
    list.extend(AllBonusList[realm][charclass]['Other Skills'])

    AllBonusList[realm][charclass]['Skills Hash'] = {}
    for skill in list:
      AllBonusList[realm][charclass]['Skills Hash'][skill] = ''

    AllBonusList[realm][charclass]['Focus Hash'] = {}
    for focus in AllBonusList[realm][charclass]['All Spell Lines']:
      AllBonusList[realm][charclass]['Focus Hash'][focus] = ''

    if len(AllBonusList[realm][charclass]['All Spell Lines']):
      AllBonusList[realm][charclass]['All Spell Lines'].insert(0, 'All Spell Lines')

    list.sort()
    if len(AllBonusList[realm][charclass]['All Melee Weapon Skills']) > 0:
      list.insert(0, 'All Melee Weapon Skills')
    if len(AllBonusList[realm][charclass]['All Magic Skills']) > 0:
      list.insert(0, 'All Magic Skills')
    AllBonusList[realm][charclass]['All Skills'] = list
 
  AllBonusList['All'].update(AllBonusList[realm])
  ClassList['All'].extend(ClassList[realm])
ClassList['All'].sort()


TypeList = [
    'Unused', 
    'Stat', 
    'Resist', 
    'Hits', 
    'Power', 
    'Focus', 
    'Skill'
]

# Duplicate the TypeList, add non-craftable categories
#
DropTypeList = TypeList[:]
DropTypeList.extend( [
    'Cap Increase', 
    'PvE Bonus', 
    'Other Bonus'
] )


StatTableOrdered = [ 
    ['Strength',     'Fiery'], 
    ['Constitution', 'Earthen'], 
    ['Dexterity',    'Vapor'], 
    ['Quickness',    'Airy'], 
    ['Intelligence', 'Dusty'], 
    ['Piety',        'Watery'], 
    ['Charisma',     'Icy'] , 
    ['Empathy',      'Heated'] 
]

StatTable = {}
for stat, stone in StatTableOrdered:
  StatTable[stat] = stone

StatList = map(lambda(x): x[0], StatTableOrdered)

StatValues = ['1', '4', '7', '10', '13', '16', '19', '22', '25', '28']


# Duplicate the Stat lists as DropStat lists, add non-craftable 'Acuity' stat
#
DropStatTableOrdered = StatTableOrdered[:]
DropStatTableOrdered.append( [
    'Acuity', ''
] ) 

DropStatTable = {}
DropStatTable.update(StatTable)
DropStatTable['Acuity'] = ''

DropStatList = StatList[:]
DropStatList.append('Acuity') 


ResistTableOrdered = [ 
    ['Body',   'Dusty'   ], 
    ['Cold',   'Icy'     ], 
    ['Heat',   'Heated'  ], 
    ['Energy', 'Light'   ],
    ['Matter', 'Earthen' ], 
    ['Spirit', 'Vapor'   ],
    ['Crush',  'Fiery'   ], 
    ['Thrust', 'Airy'    ], 
    ['Slash',  'Watery'  ] 
]

ResistTable = {}
for resist, gem in ResistTableOrdered:
  ResistTable[resist] = gem

ResistList = map(lambda(x): x[0], ResistTableOrdered)

ResistValues = ['1', '2', '3', '5', '7', '9', '11', '13', '15', '17']


HitsTable = { 'Hits' : 'Blood' }

HitsList = HitsTable.keys()

HitsValues = ['4', '12', '20', '28', '36', '44', '52', '60', '68', '76']


PowerTable = { 'Power' : 'Mystical' }

PowerList = PowerTable.keys()

PowerValues = ['1', '2', '3', '5', '7', '9', '11', '13', '15', '17']


FocusTable = {

    'Albion' : {

        'All Spell Lines' : 'Brilliant Sigil',
        'Body Magic' :      'Heat Sigil', 
        'Cold Magic' :      'Ice Sigil', 
        'Death Servant' :   'Ashen Sigil',
        'Deathsight' :      'Vacuous Sigil',
        'Earth Magic' :     'Earth Sigil',
        'Fire Magic' :      'Fire Sigil',
        'Matter Magic' :    'Dust Sigil',
        'Mind Magic' :      'Water Sigil',
        'Painworking' :     'Salt Crusted Sigil',
        'Spirit Magic' :    'Vapor Sigil',
        'Wind Magic' :      'Air Sigil'
    },

    'Hibernia' : {

        'All Spell Lines' : 'Brilliant Spell Stone',
        'Arboreal Path' :   'Steaming Spell Stone', 
        'Creeping Path' :   'Oozing Spell Stone',
        'Enchantments' :    'Vapor Spell Stone', 
        'Ethereal Shriek' : 'Ethereal Spell Stone', 
        'Light' :           'Fire Spell Stone', 
        'Mana' :            'Water Spell Stone', 
        'Mentalism' :       'Earth Spell Stone', 
        'Phantasmal Wail':  'Phantasmal Spell Stone', 
        'Spectral Guard' :  'Spectral Spell Stone', 
        'Verdant Path' :    'Mineral Encrusted Spell Stone',
        'Void' :            'Ice Spell Stone'
    },

    'Midgard' : {

        'All Spell Lines' : 'Brilliant Rune', 
        'Bone Army' :       'Ashen Rune', 
        'Cursing' :         'Blighted Rune',
        'Darkness' :        'Ice Rune',
        'Runecarving' :     'Heat Rune',
        'Summoning' :       'Vapor Rune', 
        'Suppression' :     'Dust Rune'
    }
}

FocusTable['All'] = {}
for realm in Realms:
  FocusTable['All'].update(FocusTable[realm])

FocusList = {}
for realm in FocusTable.keys():
  FocusList[realm] = FocusTable[realm].keys()
  FocusList[realm].sort()

FocusValues = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50']


SkillTable = { 

    'Albion' : {

        'All Magic Skills' :  'Finesse Fervor Sigil',
        'All Melee Weapon Skills' :  'Finesse War Sigil',
        'Body Magic' :        'Heated Evocation Sigil',
        'Chants' :            'Earthen Fervor Sigil',
        'Cold Magic' :        'Icy Evocation Sigil',
        'Critical Strike' :   'Heated Battle Jewel',
        'Crossbow' :          'Vapor War Sigil',
        'Crush' :             'Fiery War Sigil',
        'Death Servant' :     'Ashen Fervor Sigil',
        'Deathsight' :        'Vacuous Fervor Sigil',
        'Dual Wield' :        'Icy War Sigil',
        'Earth Magic' :       'Earthen Evocation Sigil',
        'Enhancement' :       'Airy Fervor Sigil',
        'Envenom' :           'Dusty Battle Jewel',
        'Flexible' :          'Molten Magma War Sigil',
        'Fire Magic' :        'Fiery Evocation Sigil',
        'Instruments' :       'Vapor Fervor Sigil',
        'Longbow' :           'Airy War Sigil',
        'Matter Magic' :      'Dusty Evocation Sigil',
        'Mind Magic' :        'Watery Evocation Sigil',
        'Painworking' :       'Salt Crusted Fervor Sigil',
        'Parry' :             'Vapor Battle Jewel',
        'Polearm' :           'Earthen War Sigil',
        'Rejuvenation' :      'Watery Fervor Sigil',
        'Shield' :            'Fiery Battle Jewel',
        'Slash' :             'Watery War Sigil',
        'Smite' :             'Fiery Fervor Sigil',
        'Soulrending' :       'Steaming Fervor Sigil',
        'Spirit Magic' :      'Vapor Evocation Sigil',
        'Staff' :             'Earthen Battle Jewel',
        'Stealth' :           'Airy Battle Jewel',
        'Thrust' :            'Dusty War Sigil',
        'Two Handed' :        'Heated War Sigil',
        'Wind Magic' :        'Air Evocation Sigil'
    }, 

    'Hibernia' : {

        'All Magic Skills' :  'Finesse Nature Spell Stone',
        'All Melee Weapon Skills' :  'Finesse War Spell Stone',
        'Arboreal Path' :     'Steaming Nature Spell Stone', 
        'Blades' :            'Watery War Spell Stone', 
        'Blunt' :             'Fiery War Spell Stone',
        'Celtic Dual' :       'Icy War Spell Stone',
        'Celtic Spear' :      'Earthen War Spell Stone',
        'Creeping Path' :     'Oozing Nature Spell Stone',
        'Critical Strike' :   'Heated Battle Jewel',
        'Dementia' :          'Aberrant Arcane Spell Stone', 
        'Enchantments' :      'Vapor Arcane Spell Stone',
        'Envenom' :           'Dusty Battle Jewel',
        'Ethereal Shriek' :   'Ethereal Arcane Spell Stone', 
        'Large Weaponry' :    'Heated War Spell Stone',
        'Light' :             'Fiery Arcane Spell Stone', 
        'Mana' :              'Watery Arcane Spell Stone',
        'Mentalism' :         'Earthen Arcane Spell Stone',
        'Music' :             'Airy Nature Spell Stone',
        'Nature' :            'Earthen Nature Spell Stone',
        'Nurture' :           'Fiery Nature Spell Stone',
        'Parry' :             'Vapor Battle Jewel',
        'Phantasmal Wail' :   'Phantasmal Arcane Spell Stone', 
        'Piercing' :          'Dusty War Spell Stone',
        'Recurve Bow' :       'Airy War Spell Stone',
        'Regrowth' :          'Watery Nature Spell Stone',
        'Scythe' :            'Light War Spell Stone',
        'Shadow Mastery' :    'Shadowy Arcane Spell Stone', 
        'Shield' :            'Fiery Battle Jewel',
        'Spectral Guard' :    'Spectral Arcane Spell Stone', 
        'Staff' :             'Earthen Battle Jewel',
        'Stealth' :           'Airy Battle Jewel',
        'Valor' :             'Airy Arcane Spell Stone',
        'Vampiiric Embrace' : 'Embracing Arcane Spell Stone', 
        'Verdant Path' :      'Mineral Encrusted Nature Spell Stone',
        'Void' :              'Icy Arcane Spell Stone'
    },

    'Midgard' : { 

        'All Magic Skills' :  'Finesse Primal Rune',
        'All Melee Weapon Skills' :  'Finesse War Rune',
        'Augmentation' :      'Airy Chaos Rune',
        'Axe' :               'Earthen War Rune', 
        'Battlesongs' :       'Airy Primal Rune',
        'Beastcraft' :        'Earthen Primal Rune',
        'Bone Army' :         'Ashen Primal Rune',
        'Cave Magic' :        'Fiery Chaos Rune',
        'Composite Bow' :     'Airy War Rune',
        'Critical Strike' :   'Heated Battle Jewel',
        'Cursing' :           'Blighted Primal Rune', 
        'Darkness' :          'Icy Chaos Rune',
        'Envenom' :           'Dusty Battle Jewel',
        'Hammer' :            'Fiery War Rune',
        'Hand To Hand' :      'Lightning Charged War Rune',
        'Hexing' :            'Unholy Primal Rune', 
        'Left Axe' :          'Icy War Rune',
        'Mending' :           'Watery Chaos Rune',
        'Odin\'s Will' :      'Valiant Primal Rune', 
        'Pacification' :      'Earthen Chaos Rune',
        'Parry' :             'Vapor Battle Jewel',
        'Runecarving' :       'Heated Chaos Rune',
        'Shield' :            'Fiery Battle Jewel',
        'Spear' :             'Heated War Rune',
        'Staff' :             'Earthen Battle Jewel',
        'Stealth' :           'Airy Battle Jewel',
        'Stormcalling' :      'Fiery Primal Rune',
        'Summoning' :         'Vapor Chaos Rune',
        'Suppression' :       'Dusty Chaos Rune',
        'Sword' :             'Watery War Rune',
        'Thrown Weapons' :    'Vapor War Rune',
    }
}

SkillTable['All'] = {}
for realm in Realms:
  SkillTable['All'].update(SkillTable[realm])

SkillList = {}
DropSkillList = {}

for realm in SkillTable.keys():
  SkillList[realm] = SkillTable[realm].keys()
  SkillList[realm].sort()
  DropSkillList[realm] = SkillList[realm][:]
  DropSkillList[realm].insert(2, 'All Dual Wield Skills')
  DropSkillList[realm].insert(3, 'All Archery Skills')

# bug - in game drops +Witchcraft(?), but no craftable gem
DropSkillList['Midgard'].append('Witchcraft')
DropSkillList['All'].append('Witchcraft')

SkillValues = ['1', '2', '3', '4', '5', '6', '7', '8']


CapIncreaseTable = {}
CapIncreaseTable.update(DropStatTable)
CapIncreaseTable.update( { 
    'Hits'  : '', 
    'Power' : '', 
    'AF'    : '' 
} )

CapIncreaseList = DropStatList[:]
CapIncreaseList.extend( [
    'Hits', 
    'Power', 
    'AF'
] )


OtherBonusTable = {
    'AF' :                        '',
    'Archery Damage' :            '',
    'Archery Range' :             '',
    'Archery Speed' :             '',
    'Stat Buff Effectiveness' :   '',
    'Casting Speed' :             '',
    'Stat Debuff Effectiveness' : '',
    'Fatigue' :                   '', 
    'Healing Effectiveness' :     '',
    'Magic Damage' :              '',
    'Duration of Spells' :        '',
    'Spell Range' :               '',
    'Style Damage' :              '',
    'Melee Damage' :              '',
    'Melee Combat Speed' :        '',   
    '% Power Pool' :              ''
}

OtherBonusList = OtherBonusTable.keys()
OtherBonusList.sort()


PvEBonusTable = {
    'Defensive' :                          '',
    'Concentration' :                      '', 
    'Block' :                              '', 
    'Evade' :                              '', 
    'Parry' :                              '', 
    'Negative Effect Duration Reduction' : '', 
    'Bladeturn Reinforcement' :            '', 
    'Piece Ablative' :                     '', 
    'Damage Reduction' :                   '', 
    'Reactionary Style Damage' :           '', 
    'To Hit' :                             '', 
    'Spell Power Cost Reduction' :         '', 
    'Style Cost Reduction' :               '', 
    'Death Experience Loss Reduction' :    '', 
    'Arrow Recovery' :                     '' 
}

PvEBonusList = PvEBonusTable.keys()
PvEBonusList.sort()


# Placeholder
UnusedTable = {}

UnusedList = [ ]

UnusedValues = [ ]


GemTables = {

  'All': {
    'Stat' :    StatTable,
    'Resist' :  ResistTable,
    'Hits' :    HitsTable,
    'Power' :   PowerTable,
    'Unused' :  UnusedTable
  }
}

# Only use GemTables['All'] when the specific realm of craft isn't known as
# there are many multi-realm gems which have different names and recipes
#
for realm in Realms:
  GemTables[realm] = {}
  GemTables[realm].update(GemTables['All'])
for realm in GemTables.keys():
  GemTables[realm]['Focus'] = FocusTable[realm]
  GemTables[realm]['Skill'] = SkillTable[realm]


ValuesLists = {
    'Stat' :    StatValues,
    'Resist' :  ResistValues,
    'Hits' :    HitsValues,
    'Power' :   PowerValues,
    'Focus' :   FocusValues,
    'Skill' :   SkillValues,
    'Unused' :  UnusedValues
}


Caps = {}
for resist in ResistList:
  Caps[resist] = 'Resist'
for stat in StatList:
  Caps[stat] = 'Stat'

# Bonuses are given as % of level + add constant
# e.g. [ .25,  1] is the level / 4 + 1
#      [   0, 10] is a fixed 10
#      [   4,  0] is the level * 4
#
HighCapBonusList = {
    'Stat'                      : [ 1.50,  0 ],
    'Resist'                    : [  .50,  1 ],
    'Hits'                      : [ 4.00,  0 ],
    'Power'                     : [  .50,  1 ],
    'Skill'                     : [  .20,  1 ],
    'Cap'                       : [  .50,  1 ],
    'Hits Cap'                  : [ 4.00,  0 ],
    'Power Cap'                 : [ 1.00,  0 ],
    'AF Cap'                    : [ 1.00,  0 ],
    'PvE Bonus'                 : [  .20,  0 ],
    'Other Bonus'               : [  .20,  0 ],
    '% Power Pool'              : [  .50,  0 ],
    'Stat Buff Effectiveness'   : [  .50,  0 ],
    'Stat Debuff Effectiveness' : [  .50,  0 ],
    'Healing  Effectiveness'    : [  .50,  0 ],
    'Spell Duration'            : [  .50,  0 ],
    'Fatigue'                   : [  .50,  0 ],
    'AF'                        : [ 1.00,  0 ],
    'Arrow Recovery'            : [ 1.00,  0 ], 
    'Death Experience Loss Reduction'   : [ 1.00,  0 ] 
}


MaterialGems = [ 'Lo',   'Um',   'On',    'Ee',      'Pal',     'Mon',    'Ros',      'Zo',    'Kath',     'Ra']

GemCosts =     [ 160,    920,   3900,   13900,      40100,     88980,   133000,    198920,    258240,   296860 ]

RemakeCosts =  [ 120,    560,   1740,    5260,      14180,     30660,    45520,     67680,     87640,   100700 ]

GemNames =     ['Raw','Uncut','Rough','Flawed','Imperfect','Polished','Faceted','Precious','Flawless','Perfect']


LiquidsOrder = [
    'Air Elemental Essence', 
    'Draconic Fire', 
    'Frost From a Wasteland',
    'Giant Blood', 
    'Heat From an Unearthly Pyre',
    'Leviathan Blood',
    'Mystic Energy',
    'Sun Light',
    'Swamp Fog',
    'Treant Blood', 
    'Undead Ash and Holy Water' 
]

DustsOrder = [
    'Bloodied Battlefield Dirt',
    'Essence of Life', 
    'Fairy Dust', 
    'Ground Blessed Undead Bone',
    'Ground Caer Stone', 
    'Ground Cave Crystal',
    'Ground Draconic Scales',
    'Ground Giant Bone', 
    'Ground Vendo Bone', 
    'Other Worldly Dust',
    'Soot From Niflheim',
    'Unseelie Dust'
]

GemLiquids = { 
    'Fiery' :              'Draconic Fire', 
    'Earthen':             'Treant Blood',
    'Vapor' :              'Swamp Fog', 
    'Airy' :               'Air Elemental Essence',
    'Heated' :             'Heat From an Unearthly Pyre', 
    'Icy' :                'Frost From a Wasteland', 
    'Watery' :             'Leviathan Blood',
    'Dusty' :              'Undead Ash and Holy Water',
    'Fire' :               'Draconic Fire', 
    'Earth' :              'Treant Blood',
    'Vapor' :              'Swamp Fog', 
    'Air' :                'Air Elemental Essence',
    'Heat' :               'Heat From an Unearthly Pyre', 
    'Ice' :                'Frost From a Wasteland', 
    'Water' :              'Leviathan Blood',
    'Dust' :               'Undead Ash and Holy Water',
    'Ashen' :              'Undead Ash and Holy Water',
    'Vacuous' :            'Swamp Fog',
    'Salt' :               'Mystic Energy',
    'Steaming Spell' :     'Swamp Fog',
    'Steaming Nature' :    'Swamp Fog',
    'Steaming Fervor' :    'Heat From an Unearthly Pyre',
    'Oozing' :             'Treant Blood',
    'Mineral' :            'Heat From an Unearthly Pyre',
    'Lightning' :          'Leviathan Blood',
    'Molten' :             'Leviathan Blood',
    'Light' :              'Sun Light',
    'Blood' :              'Giant Blood',
    'Mystical' :           'Mystic Energy',
    'Mystic' :             'Mystic Energy', 
    'Brilliant' :         ['Draconic Fire', 'Mystic Energy', 'Treant Blood'],
    'Finesse' :           ['Draconic Fire', 'Mystic Energy', 'Treant Blood'],
    'Ethereal Spell' :     'Swamp Fog', 
    'Phantasmal Spell' :   'Leviathan Blood', 
    'Spectral Spell' :     'Draconic Fire', 
    'Ethereal Arcane' :    'Leviathan Blood', 
    'Phantasmal Arcane' :  'Draconic Fire', 
    'Spectral Arcane' :    'Air Elemental Essence', 
    'Aberrant' :           'Treant Blood', 
    'Embracing' :          'Frost From a Wasteland', 
    'Shadowy' :            'Swamp Fog', 
    'Blighted Primal' :    'Air Elemental Essence', 
    'Blighted Rune' :      'Undead Ash and Holy Water', 
    'Valiant' :            'Swamp Fog', 
    'Unholy' :             'Air Elemental Essence' 
}

GemDusts = { 
    'Essence' :            'Essence of Life',
    'Shielding' :          'Ground Draconic Scales',
    'Spell Stone' :        'Ground Draconic Scales',
    'Sigil' :              'Ground Draconic Scales',
    'Rune' :               'Ground Draconic Scales',
    'Chaos Rune' :         'Soot From Niflheim',
    'Battle Jewel':        'Bloodied Battlefield Dirt',
    'War Rune' :           'Ground Giant Bone',
    'Primal Rune' :        'Ground Vendo Bone',
    'Evocation Sigil' :    'Ground Cave Crystal', 
    'Fervor Sigil' :       'Ground Blessed Undead Bone',
    'War Sigil' :          'Ground Caer Stone',
    'Nature Spell Stone' : 'Fairy Dust',
    'War Spell Stone' :    'Unseelie Dust',
    'Arcane Spell Stone' : 'Other Worldly Dust' 
}

GemSubName = { 
    'Stat' :   'Essence', 
    'Resist' : 'Shielding', 
    'Hits' :   'Essence', 
    'Power' :  'Essence', 
    'Focus' :  '', 
    'Skill' :  '' 
}


OCStartPercentages = [0, 10, 20, 30, 50, 70]

ImbueMultipliers = { 
    'Stat' :   1.0, 
    'Resist' : 2.0, 
    'Skill' :  5.0, 
    'Hits' :   0.25, 
    'Power' :  2.0, 
    'Focus' :  1.0, 
    'Unused' : 0.0 
} 

QualityValues = ['94', '95', '96', '97', '98', '99', '100']

GemQualOCModifiers = { 
      '' :  0, 
    '94' :  0, 
    '95' :  0, 
    '96' :  1, 
    '97' :  3, 
    '98' :  5, 
    '99' :  8, 
   '100' : 11 
}

ItemQualOCModifiers = { 
    '94' :  0, 
    '95' :  0, 
    '96' :  6, 
    '97' :  8, 
    '98' : 10, 
    '99' : 18, 
   '100' : 26 
}

ImbuePts = [ 
    [0,1,1,1,1,1,1],
    [1,1,1,1,1,2,2],
    [1,1,1,2,2,2,2],
    [1,1,2,2,2,3,3],
    [1,2,2,2,3,3,4],
    [1,2,2,3,3,4,4],
    [2,2,3,3,4,4,5],
    [2,3,3,4,4,5,5],
    [2,3,3,4,5,5,6],
    [2,3,4,4,5,6,7],
    [2,3,4,5,6,6,7],
    [3,4,4,5,6,7,8],
    [3,4,5,6,6,7,9],
    [3,4,5,6,7,8,9],
    [3,4,5,6,7,8,10],
    [3,5,6,7,8,9,10],
    [4,5,6,7,8,10,11],
    [4,5,6,8,9,10,12],
    [4,6,7,8,9,11,12],
    [4,6,7,8,10,11,13],
    [4,6,7,9,10,12,13],
    [5,6,8,9,11,12,14],
    [5,7,8,10,11,13,15],
    [5,7,9,10,12,13,15],
    [5,7,9,10,12,14,16],
    [5,8,9,11,12,14,16],
    [6,8,10,11,13,15,17],
    [6,8,10,12,13,15,18],
    [6,8,10,12,14,16,18],
    [6,9,11,12,14,16,19],
    [6,9,11,13,15,17,20],
    [7,9,11,13,15,17,20],
    [7,10,12,14,16,18,21],
    [7,10,12,14,16,19,21],
    [7,10,12,14,17,19,22],
    [7,10,13,15,17,20,23],
    [8,11,13,15,17,20,23],
    [8,11,13,16,18,21,24],
    [8,11,14,16,18,21,24],
    [8,11,14,16,19,22,25],
    [8,12,14,17,19,22,26],
    [9,12,15,17,20,23,26],
    [9,12,15,18,20,23,27],
    [9,13,15,18,21,24,27],
    [9,13,16,18,21,24,28],
    [9,13,16,19,22,25,29],
    [10,13,16,19,22,25,29],
    [10,14,17,20,23,26,30],
    [10,14,17,20,23,27,31],
    [10,14,17,20,23,27,31],
    [10,15,18,21,24,28,32] 
]


TabList = [
    'Chest', 'Arms', 'Head', 'Legs', 'Hands', 'Feet', 
    'Right Hand', 'Left Hand', '2 Handed', 'Ranged', 'Spare', 
    'Neck', 'Cloak', 'Jewel', 'Belt', 
    'Left Ring', 'Right Ring', 'Left Wrist', 'Right Wrist'
]

FileExt = { 
    'Neck' :         'neck', 
    'Cloak' :        'cloak', 
    'Belt' :         'belt', 
    'Jewel' :        'jewel',
    'Left Ring' :    'ring', 
    'Right Ring' :   'ring', 
    'Left Wrist' :  ['bracer', 'wrist'],
    'Right Wrist' : ['bracer', 'wrist'], 
    'Chest' :        'chest', 
    'Arms' :         'arms', 
    'Head' :         'helm', 
    'Legs' :         'legs', 
    'Feet' :         'boots', 
    'Hands' :        'hands',
    'Right Hand' :   'wep', 
    'Left Hand' :   ['lhwep', 'shield'],
    '2 Handed' :    ['2hwep', 'lhwep', 'wep'],
    'Ranged' :       'ranged', 
    'Spare' :        '*' 
}

ShieldTypes = [
    'Rowan',     'Elm',       'Oaken',     'Ironwood',  'Heartwood', 
    'Runewood',  'Stonewood', 'Ebonwood',  'Dyrwood',   'Duskwood' 
]


Races = {
    'Albion' : [
        'Avalonian',
        'Briton',
        'Inconnu',
        'Saracen',
        'Half Ogre',
        'Highlander' 
    ],

    'Hibernia' : [
        'Celt',
        'Elf',
        'Firbolg',
        'Lurikeen',
        'Shar',
        'Sylvan' 
    ],

    'Midgard' : [
        'Dwarf',
        'Frostalf',
        'Kobold',
        'Troll',
        'Norseman',
        'Valkyn' 
    ] 
}

Races['All'] = []
for realm in Realms:
  Races['All'].extend(Races[realm])
Races['All'].sort()


RacialResists = {
   'Avalonian' :  {'Crush' : 2, 'Slash'  : 3, 'Matter' : 5 },
   'Briton' :     {'Crush' : 2, 'Slash'  : 3, 'Cold'   : 5 },
   'Inconnu' :    {'Crush' : 2, 'Thrust' : 3, 'Heat'   : 5, 'Spirit' : 5 },
   'Saracen' :    {'Slash' : 2, 'Thrust' : 3, 'Heat'   : 5 },
   'Half Ogre' :  {'Slash' : 3, 'Thrust' : 2, 'Matter' : 5 },
   'Highlander' : {'Crush' : 3, 'Slash'  : 2, 'Cold'   : 5 },
   'Celt' :       {'Crush' : 2, 'Slash'  : 3, 'Spirit' : 5 },
   'Elf' :        {'Slash' : 2, 'Thrust' : 3, 'Spirit' : 5 },
   'Firbolg' :    {'Crush' : 3, 'Slash'  : 2, 'Heat'   : 5 },
   'Lurikeen' :   {'Crush' : 5,               'Energy' : 5 },
   'Shar' :       {'Crush' : 5,               'Energy' : 5 },
   'Sylvan' :     {'Crush' : 3, 'Thrust' : 2, 'Matter' : 5, 'Energy' : 5 },
   'Dwarf' :      {'Slash' : 2, 'Thrust' : 3, 'Body'   : 5 },
   'Frostalf' :   {'Slash' : 2, 'Thrust' : 3, 'Spirit' : 5 },
   'Kobold' :     {'Crush' : 5,               'Energy' : 5 },
   'Troll' :      {'Slash' : 3, 'Thrust' : 2, 'Matter' : 5 },
   'Norseman' :   {'Crush' : 2, 'Slash'  : 3, 'Cold'   : 5 },
   'Valkyn' :     {'Slash' : 3, 'Thrust' : 2, 'Cold'   : 5, 'Body'   : 5 } 
}


# Rename old skills to new skills, from previously saved template files
#
FixEffectsTable = {
    'Bonedancing' :    'Bone Army',
    'PainWorking' :    'Painworking', 
    'Subterranean' :   'Cave Magic',
    'Arboreal' :       'Arboreal Path',

    'All Focus Bonus' :             'All Spell Lines',
    'All Melee Skill Bonus' :       'All Melee Weapon Skills',
    'All Magic Skill Bonus' :       'All Magic Skills',
    'All Dual Wield Skill Bonus' :  'All Dual Wield Skills',
    'Archery Skill Bonus' :         'All Archery Skills',

    'AF Bonus' :               'AF',
    'Archery Damage Bonus' :   'Archery Damage',
    'Archery Range Bonus' :    'Archery Range',
    'Archery Speed Bonus' :    'Archery Speed',
    'Buff Bonus' :             'Stat Buff Effectiveness',
    'Casting Range' :          'Spell Range',
    'Casting Speed Bonus' :    'Casting Speed',
    'Debuff Bonus' :           'Stat Debuff Effectiveness',
    #??'Fatigue' :                'Fatigue', 
    'Healing Bonus' :          'Healing Effectiveness',
    'Spell Damage Bonus' :     'Magic Damage',
    'Spell Duration Bonus' :   'Duration of Spells',
    'Spell Range Bonus' :      'Spell Range',
    'Style Damage Bonus' :     'Style Damage',
    'Melee Damage Bonus' :     'Melee Damage',
    'Melee Speed Bonus' :      'Melee Combat Speed',   
    'Power Percentage Bonus' : '% Power Pool',

    'Strength Cap Increase' :     'Strength',
    'Constitution Cap Increase' : 'Constitution',
    'Dexterity Cap Increase' :    'Dexterity',
    'Quickness Cap Increase' :    'Quickness',
    'Intelligence Cap Increase':  'Intelligence',
    'Piety Cap Increase' :        'Piety',
    'Charisma Cap Increase' :     'Charisma', 
    'Empathy Cap Increase' :      'Empathy',
    'Acuity Cap Increase' :       'Acuity',
    'Power Cap Increase' :        'Power', 
    'Hits Cap Increase' :         'Hits', 
    'AF Cap Increase' :           'AF',

    'Reactionary Style Damage Bonus' :  'Reactionary Style Damage',
    'Death XP Loss Reduction' :         'Death Experience Loss Reduction',
    'Blocking' :                        'Block',

    'Body Resist' :     'Body', 
    'Cold Resist' :     'Cold', 
    'Heat Resist' :     'Heat', 
    'Energy Resist' :   'Energy',
    'Matter Resist' :   'Matter', 
    'Spirit Resist' :   'Spirit',
    'Crush Resist' :    'Crush', 
    'Thrust Resist' :   'Thrust', 
    'Slash Resist' :    'Slash'

    
}

