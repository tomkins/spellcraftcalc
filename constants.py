# constants.py: Dark Age of Camelot Spellcrafting Calculator
# See http://www.ugcs.caltech.edu/~jlamanna/daoc/sccalc/index.html for updates

# Copyright t2(C) 2003,  James Lamanna t2(jlamanna@ugcs.caltech.edu)

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or t2(at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

__all__ = [
  'QualityValues', 'CapIncreaseTable', 'HitsList', 'StatTableOrdered', 
  'GemQualOCModifiers', 'ItemQualOCModifiers', 'ClassList', 'PowerTable', 
  'Races', 'GemLiquids', 'GemNames', 'ImbuePts', 'HitsValues', 'RaceList', 
  'DropStatTable', 'PvEBonusList', 'PowerList', 'ScVersion', 'FileExt', 'StatList', 
  'ResistValues', 'OtherBonusList', 'HighCapBonusList', 'TypeList', 'UnusedTable',
  'AllBonusList', 'DustsOrder', 'PowerValues', 'Caps', 'ResistList', 'GemDusts', 
  'StatValues', 'DropSkillList', 'Realms', 'ValuesLists', 'SkillValues', 
  'HitsTable', 'CapIncreaseList', 'FixEffectsTable', 'GemSubName', 'HotkeyGems', 
  'RemakeCosts', 'FocusTable', 'DropStatList', 'GemTables', 'ResistTableOrdered', 
  'StatTable', 'TabList', 'GemCosts', 'FocusValues', 'DropStatTableOrdered', 
  'OCStartPercentages', 'UnusedValues', 'ShieldTypes', 'ResistTable', 'SkillList', 
  'SkillTable', 'UnusedList', 'ImbueMultipliers', 'PvEBonusTable', 'DropTypeList', 
  'MaterialGems', 'FocusList', 'OtherBonusTable', 'LiquidsOrder', 'ServerCodes',
  'EffectTable', 'EffectRequiredLevel', 'EffectMetal', 'EffectItemNames',
  'EffectItemList', 'EffectTypeList', 'BodyHitOdds', 'PieceTabList', 'JewelTabList', 
]

ScVersion = "Kort 1.43.0010 (dev)"

from tuple2 import * 
from dict2 import * 

Realms = t2(('Albion', 'Hibernia', 'Midgard'))


# Placeholder
UnusedTable = d2({})

UnusedList = t2()

UnusedValues = t2()


AllBonusList = { 

  'Albion' : {

    'Armsman' : {
        'All Spell Lines' : (), 
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Crush', 'Slash', 'Thrust', 'Polearm', 'Two Handed',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre', 'Highlander', 'Inconnu', 'Saracen',)),
        'Acuity' : (),
    },

    'Cabalist' : {
        'All Spell Lines' : ('Body Magic', 'Matter Magic', 'Spirit Magic',), 
        'All Magic Skills' : ('Body Magic', 'Matter Magic', 'Spirit Magic',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre', 'Inconnu', 'Saracen',)),
        'Acuity' : ('Intelligence',),
    },

    'Cleric' : {
        'All Spell Lines' : (), 
        'All Magic Skills' : ('Rejuvenation', 'Enhancement', 'Smite',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Avalonian', 'Briton', 'Highlander',)),
        'Acuity' : ('Piety',),
    },

    'Friar' : {
        'All Spell Lines' : (), 
        'All Magic Skills' : ('Rejuvenation', 'Enhancement',),
        'All Melee Weapon Skills' : ('Staff',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry',),
        'Races' : t2(('Briton',)),
        'Acuity' : ('Piety',),
    },

    'Heretic' : {
        'All Spell Lines' : (), 
        'All Magic Skills' : ('Rejuvenation', 'Enhancement',),
        'All Melee Weapon Skills' : ('Crush', 'Flexible',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Shield',),
        'Races' : t2(('Avalonian', 'Briton', 'Inconnu',)),
        'Acuity' : ('Piety',),
    },

    'Infiltrator' : {
        'All Spell Lines' : (), 
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Slash', 'Thrust',),
        'All Dual Wield Skills' : ('Dual Wield',),
        'All Archery Skills' : (),
        'Other Skills' : ('Critical Strike', 'Envenom', 'Stealth',),
        'Races' : t2(('Briton', 'Inconnu', 'Saracen',)),
        'Acuity' : (),
    },

    'Mercenary' : {
        'All Spell Lines' : (), 
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Crush', 'Slash', 'Thrust',),
        'All Dual Wield Skills' : ('Dual Wield',),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre', 'Highlander', 'Inconnu', 'Saracen',)),
        'Acuity' : (),
    },

    'Minstrel' : {
        'All Spell Lines' : (), 
        'All Magic Skills' : ('Instruments',),
        'All Melee Weapon Skills' : ('Slash', 'Thrust',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Stealth',),
        'Races' : t2(('Briton', 'Highlander', 'Saracen',)),
        'Acuity' : ('Charisma',),
    },

    'Necromancer' : {
        'All Spell Lines' : ('Deathsight', 'Death Servant', 'Painworking',), 
        'All Magic Skills' : ('Deathsight', 'Death Servant', 'Painworking',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Briton', 'Inconnu', 'Saracen',)),
        'Acuity' : ('Intelligence',),
    },

    'Paladin' : {
        'All Spell Lines' : (),
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Crush', 'Slash', 'Thrust', 'Two Handed',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry', 'Shield',),
        'No Skill Effect' : ('Chants',),
        'Races' : t2(('Avalonian', 'Briton', 'Highlander', 'Saracen',)),
        'Acuity' : ('Piety',),
    },

    'Reaver' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Soulrending',),
        'All Melee Weapon Skills' : ('Crush', 'Flexible', 'Slash', 'Thrust',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Briton', 'Inconnu', 'Saracen',)),
        'Acuity' : ('Piety',),
    },

    'Scout' : {
        'All Spell Lines' : (),
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Slash', 'Thrust',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : ('Longbow',),
        'Other Skills' : ('Stealth', 'Shield',),
        'Races' : t2(('Briton', 'Highlander', 'Inconnu', 'Saracen',)),
        'Acuity' : (),
    },

    'Sorcerer' : {
        'All Spell Lines' : ('Body Magic', 'Mind Magic', 'Matter Magic',),
        'All Magic Skills' : ('Body Magic', 'Mind Magic', 'Matter Magic',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'No Skill Effect' : (),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre', 'Inconnu', 'Saracen',)),
        'Acuity' : ('Intelligence',),
    },

    'Theurgist' : {
        'All Spell Lines' : ('Earth Magic', 'Cold Magic', 'Wind Magic',),
        'All Magic Skills' : ('Earth Magic', 'Cold Magic', 'Wind Magic',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre',)),
        'Acuity' : ('Intelligence',),
    },

    'Wizard' : {
        'All Spell Lines' : ('Earth Magic', 'Cold Magic', 'Fire Magic',),
        'All Magic Skills' : ('Earth Magic', 'Cold Magic', 'Fire Magic',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Avalonian', 'Briton', 'Half Ogre',)),
        'Acuity' : ('Intelligence',),
    },
  },

  'Hibernia' : {

    'Animist' : {
        'All Spell Lines' : ('Arboreal Path', 'Creeping Path', 'Verdant Path',),
        'All Magic Skills' : ('Arboreal Path', 'Creeping Path', 'Verdant Path',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Celt', 'Firbolg', 'Sylvan',)),
        'Acuity' : ('Intelligence',),
    },

    'Bainshee' : {
        'All Spell Lines' : ('Ethereal Shriek', 'Phantasmal Wail', 'Spectral Guard',),
        'All Magic Skills' : ('Ethereal Shriek', 'Phantasmal Wail', 'Spectral Guard',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Celt', 'Elf', 'Lurikeen',)),
        'Acuity' : ('Intelligence',),
    },

    'Bard' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Regrowth', 'Nurture', 'Music',),
        'All Melee Weapon Skills' : ('Blades', 'Blunt',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Celt', 'Firbolg',)),
        'Acuity' : ('Charisma',),
    },

    'Blademaster' : {
        'All Spell Lines' : (),
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Blades', 'Blunt', 'Piercing',),
        'All Dual Wield Skills' : ('Celtic Dual',),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Celt', 'Firbolg', 'Shar',)),
        'Acuity' : (),
    },

    'Champion' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Valor',),
        'All Melee Weapon Skills' : ('Blades', 'Blunt', 'Piercing', 'Large Weaponry',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Celt', 'Elf', 'Lurikeen', 'Shar',)),
        'Acuity' : ('Intelligence',),
    },

    'Druid' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Regrowth', 'Nature', 'Nurture',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Celt', 'Firbolg', 'Sylvan',)),
        'Acuity' : ('Empathy',),
    },

    'Eldritch' : {
        'All Spell Lines' : ('Light', 'Mana', 'Void',),
        'All Magic Skills' : ('Light', 'Mana', 'Void',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Elf', 'Lurikeen',)),
        'Acuity' : ('Intelligence',),
    },

    'Enchanter' : {
        'All Spell Lines' : ('Light', 'Mana', 'Enchantments',),
        'All Magic Skills' : ('Light', 'Mana', 'Enchantments',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Elf', 'Lurikeen',)),
        'Acuity' : ('Intelligence',),
    },

    'Mentalist' : {
        'All Spell Lines' : ('Light', 'Mana', 'Mentalism',),
        'All Magic Skills' : ('Light', 'Mana', 'Mentalism',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Celt', 'Elf', 'Lurikeen', 'Shar',)),
        'Acuity' : ('Intelligence',),
    },

    'Hero' : {
        'All Spell Lines' : (),
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Blades', 'Blunt', 'Celtic Spear', 'Large Weaponry', 'Piercing',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Celt', 'Firbolg', 'Lurikeen', 'Shar', 'Sylvan',)),
        'Acuity' : (),
    },

    'Nightshade' : {
        'All Spell Lines' : (),
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Blades', 'Piercing',),
        'All Dual Wield Skills' : ('Celtic Dual',),
        'All Archery Skills' : (),
        'Other Skills' : ('Critical Strike', 'Envenom', 'Stealth',),
        'Races' : t2(('Elf', 'Lurikeen',)),
        'Acuity' : (),
    },

    'Ranger' : {
        'All Spell Lines' : (),
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Blades', 'Piercing',),
        'All Dual Wield Skills' : ('Celtic Dual',),
        'All Archery Skills' : ('Recurve Bow',),
        'Other Skills' : ('Stealth','Pathfinding',),
        'Races' : t2(('Celt', 'Elf', 'Lurikeen', 'Shar',)),
        'Acuity' : (),
    },

    'Valewalker' : {
        'All Spell Lines' : ('Arboreal Path',),
        'All Magic Skills' : ('Arboreal Path',),
        'All Melee Weapon Skills' : ('Scythe',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry',),
        'Races' : t2(('Celt', 'Firbolg', 'Sylvan',)),
        'Acuity' : ('Intelligence',),
    },

    'Vampiir' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Dementia', 'Shadow Mastery', 'Vampiiric Embrace',),
        'All Melee Weapon Skills' : ('Piercing',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Celt', 'Lurikeen', 'Shar',)),
        'Acuity' : (),
    },

    'Warden' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Nurture', 'Regrowth',),
        'All Melee Weapon Skills' : ('Blades', 'Blunt',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry',),
        'Races' : t2(('Celt', 'Firbolg', 'Sylvan',)),
        'Acuity' : ('Empathy',),
    },
  },

  'Midgard' : {

    'Berserker' : {
        'All Spell Lines' : (),
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Axe', 'Hammer', 'Sword',),
        'All Dual Wield Skills' : ('Left Axe',),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry',),
        'Races' : t2(('Dwarf', 'Norseman', 'Troll', 'Valkyn',)),
        'Acuity' : (),
    },

    'Bonedancer' : {
        'All Spell Lines' : ('Darkness', 'Suppression', 'Bone Army',),
        'All Magic Skills' : ('Darkness', 'Suppression', 'Bone Army',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Kobold', 'Troll', 'Valkyn',)),
        'Acuity' : ('Piety',),
    },

    'Healer' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Augmentation', 'Mending',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'No Skill Effect' : ('Pacification',),
        'Races' : t2(('Dwarf', 'Frostalf', 'Norseman',)),
        'Acuity' : ('Piety',),
    },

    'Hunter' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Beastcraft',),
        'All Melee Weapon Skills' : ('Spear', 'Sword',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : ('Composite Bow',),
        'Other Skills' : ('Stealth',),
        'Races' : t2(('Dwarf', 'Frostalf', 'Kobold', 'Norseman', 'Valkyn',)),
        'Acuity' : (),
    },

    'Runemaster' : {
        'All Spell Lines' : ('Darkness', 'Suppression', 'Runecarving',),
        'All Magic Skills' : ('Darkness', 'Suppression', 'Runecarving',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Dwarf', 'Frostalf', 'Kobold', 'Norseman',)),
        'Acuity' : ('Piety',),
    },

    'Savage' : {
        'All Spell Lines' : (),
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Sword', 'Axe', 'Hammer', 'Hand To Hand',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry',),
        'No Skill Effect' : ('Savagery',),
        'Races' : t2(('Dwarf', 'Kobold', 'Norseman', 'Troll', 'Valkyn',)),
        'Acuity' : (),
    },

    'Shadowblade' : {
        'All Spell Lines' : (),
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Sword', 'Axe',),
        'All Dual Wield Skills' : ('Left Axe',),
        'All Archery Skills' : (),
        'Other Skills' : ('Critical Strike', 'Envenom', 'Stealth',),
        'Races' : t2(('Kobold', 'Norseman', 'Valkyn',)),
        'Acuity' : (),
    },

    'Shaman' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Augmentation', 'Cave Magic', 'Mending',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Frostalf', 'Kobold', 'Troll',)),
        'Acuity' : ('Piety',),
    },

    'Skald' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Battlesongs',),
        'All Melee Weapon Skills' : ('Sword', 'Hammer', 'Axe',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry',),
        'Races' : t2(('Dwarf', 'Kobold', 'Norseman', 'Troll',)),
        'Acuity' : ('Charisma',),
    },

    'Spiritmaster' : {
        'All Spell Lines' : ('Darkness', 'Suppression', 'Summoning',),
        'All Magic Skills' : ('Darkness', 'Suppression', 'Summoning',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'Races' : t2(('Frostalf', 'Kobold', 'Norseman',)),
        'Acuity' : ('Piety',),
    },

    'Thane' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Stormcalling',),
        'All Melee Weapon Skills' : ('Sword', 'Hammer', 'Axe',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Dwarf', 'Frostalf', 'Norseman', 'Troll',)),
        'Acuity' : ('Piety',),
    },

    'Valkyrie' : {
        'All Spell Lines' : (),
        'All Magic Skills' : ('Odin\'s Will',),
        'All Melee Weapon Skills' : ('Spear', 'Sword',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry', 'Shield',),
        'Races' : t2(('Dwarf', 'Frostalf', 'Norseman',)),
        'Acuity' : ('Piety',),
    },

    'Warlock' : {
        'All Spell Lines' : ('Cursing',),
        'All Magic Skills' : ('Cursing', 'Hexing',),
        'All Melee Weapon Skills' : (),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : (),
        'No Skill Effect' : ('Witchcraft',),
        'Races' : t2(('Frostalf', 'Kobold', 'Norseman',)),
        'Acuity' : ('Piety',),
    },

    'Warrior' : {
        'All Spell Lines' : (),
        'All Magic Skills' : (),
        'All Melee Weapon Skills' : ('Sword', 'Hammer', 'Axe',),
        'All Dual Wield Skills' : (),
        'All Archery Skills' : (),
        'Other Skills' : ('Parry', 'Shield',),
        'No Skill Effect' : ('Thrown Weapons',),
        'Races' : t2(('Dwarf', 'Kobold', 'Norseman', 'Troll', 'Valkyn',)),
        'Acuity' : ()
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
    skills.extend(AllBonusList[realm][charclass]['All Magic Skills'])
    skills.extend(AllBonusList[realm][charclass]['All Melee Weapon Skills'])
    skills.extend(AllBonusList[realm][charclass]['All Dual Wield Skills'])
    skills.extend(AllBonusList[realm][charclass]['All Archery Skills'])
    skills.extend(AllBonusList[realm][charclass]['Other Skills'])

    AllBonusList[realm][charclass]['Skills Hash'] = d2(dict.fromkeys(skills))

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

TypeList = t2((
    'Unused', 
    'Stat', 
    'Resist', 
    'Hits', 
    'Power', 
    'Focus', 
    'Skill',
))

# This list is only for the 5th Alchemy imbue slot
#
EffectTypeList = t2((
    'Offensive Effect',
    'Reactive Effect',
    'Charged Effect',
))

# Duplicate the TypeList, plus non-craftable categories
#
DropTypeList = t2(
     TypeList + (
    'Cap Increase', 
    'PvE Bonus', 
    'Other Bonus',
 ) + EffectTypeList + (
    'Other Effect',
))

EffectTypeList = t2((
    'Unused',
 ) + EffectTypeList
)


StatTableOrdered = (
    ('Strength',     'Fiery'   ), 
    ('Constitution', 'Earthen' ), 
    ('Dexterity',    'Vapor'   ), 
    ('Quickness',    'Airy'    ), 
    ('Intelligence', 'Dusty'   ), 
    ('Piety',        'Watery'  ), 
    ('Charisma',     'Icy'     ), 
    ('Empathy',      'Heated'  ),
)

StatTable = d2(StatTableOrdered)

StatList = t2(map(lambda(x): x[0], StatTableOrdered))

StatValues = t2(('1', '4', '7', '10', '13', '16', '19', '22', '25', '28',))


# Duplicate the Stat lists as DropStat lists, add non-craftable 'Acuity' stat
#
DropStatTableOrdered = t2(StatTableOrdered + (
    ('Acuity',       ''        ),
))

DropStatTable = d2(DropStatTableOrdered)

DropStatList = t2(map(lambda(x): x[0], DropStatTableOrdered))


ResistTableOrdered = (
    ('Body',   'Dusty'   ), 
    ('Cold',   'Icy'     ), 
    ('Heat',   'Heated'  ), 
    ('Energy', 'Light'   ),
    ('Matter', 'Earthen' ), 
    ('Spirit', 'Vapor'   ),
    ('Crush',  'Fiery'   ), 
    ('Thrust', 'Airy'    ), 
    ('Slash',  'Watery'  ),
)

ResistTable = d2(ResistTableOrdered)

ResistList = map(lambda(x): x[0], ResistTableOrdered)

ResistValues = t2(('1', '2', '3', '5', '7', '9', '11', '13', '15', '17',))


HitsTable = d2((
    ('Hits',   'Blood'   ),
))

HitsList = t2(HitsTable.keys())

HitsValues = t2(('4', '12', '20', '28', '36', '44', '52', '60', '68', '76',))


PowerTable = d2((
    ('Power',  'Mystical'),
))

PowerList = t2(PowerTable.keys())

PowerValues = t2(('1', '2', '3', '5', '7', '9', '11', '13', '15', '17'))


FocusTable = {

    'Albion' : d2({

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
        'Wind Magic' :      'Air Sigil',
    }),

    'Hibernia' : d2({

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
        'Void' :            'Ice Spell Stone',
    }),

    'Midgard' : d2({

        'All Spell Lines' : 'Brilliant Rune', 
        'Bone Army' :       'Ashen Rune', 
        'Cursing' :         'Blighted Rune',
        'Darkness' :        'Ice Rune',
        'Runecarving' :     'Heat Rune',
        'Summoning' :       'Vapor Rune', 
        'Suppression' :     'Dust Rune',
    }),
}

FocusTable['All'] = {}
for realm in Realms:
  FocusTable['All'].update(FocusTable[realm])
FocusTable['All'] = d2(FocusTable['All'])
FocusTable = d2(FocusTable)

FocusList = {}
for realm in FocusTable.keys():
  FocusList[realm] = FocusTable[realm].keys()
  FocusList[realm].sort()
  FocusList[realm] = t2(FocusList[realm])
FocusList = d2(FocusList)

FocusValues = t2(('5', '10', '15', '20', '25', '30', '35', '40', '45', '50',))


SkillTable = { 

    'Albion' : d2({

        'All Magic Skills' :        'Finesse Fervor Sigil',
        'All Melee Weapon Skills' : 'Finesse War Sigil',
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
        'Wind Magic' :        'Air Evocation Sigil',
    }), 

    'Hibernia' : d2({

        'All Magic Skills' :        'Finesse Nature Spell Stone',
        'All Melee Weapon Skills' : 'Finesse War Spell Stone',
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
        'Void' :              'Icy Arcane Spell Stone',
    }),

    'Midgard' : d2({ 

        'All Magic Skills' :        'Finesse Primal Rune',
        'All Melee Weapon Skills' : 'Finesse War Rune',
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
    }),
}

SkillTable['All'] = {}
for realm in Realms:
  SkillTable['All'].update(SkillTable[realm])
SkillTable['All'] = d2(SkillTable['All'])
SkillTable = d2(SkillTable)

SkillList = {}
DropSkillList = {}

for realm in SkillTable.keys():
  skills = SkillTable[realm].keys()
  skills.sort()
  SkillList[realm] = t2(skills)
  skills.insert(2, 'All Dual Wield Skills')
  skills.insert(3, 'All Archery Skills')
  # bug - CM Explorer shows +Witchcraft, but no craftable gem
  if realm == 'Midgard': skills.append('Witchcraft')
  DropSkillList[realm] = t2(skills)

SkillList = d2(SkillList)
DropSkillList = d2(DropSkillList)

SkillValues = t2(('1', '2', '3', '4', '5', '6', '7', '8',))


CapIncreaseList = t2(DropStatList + (
    'Hits', 
    'Power', 
    'AF',
))

CapIncreaseTable = d2(dict.fromkeys(CapIncreaseList))


OtherBonusTable = d2({
    'AF' :                        '',
    'Archery Damage' :            '',
    'Archery Range' :             '',
    'Archery Speed' :             '',
    'Stat Buff Effectiveness' :   '',
    'Casting Speed' :             '',
    'Stat Debuff Effectiveness' : '',
    'Fatigue' :                   '', 
    'Healing Effectiveness' :     '',
    'Spell Damage' :              '',
    'Duration of Spells' :        '',
    'Spell Range' :               '',
    'Spell Piercing' :            '',
    'Style Damage' :              '',
    'Melee Damage' :              '',
    'Melee Combat Speed' :        '',   
    '% Power Pool' :              '', 
    'Unique Bonus...':            '',
})

OtherBonusList = OtherBonusTable.keys()
OtherBonusList.sort()
OtherBonusList = t2(OtherBonusList)


PvEBonusTable = d2({
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
    'Arrow Recovery' :                     '', 
    'Unique PvE Bonus...':                 '',
})

PvEBonusList = PvEBonusTable.keys()
PvEBonusList.sort()
PvEBonusList = t2(PvEBonusList)

DDEffectDamageSubtable = t2(("41", "50", "59", "68", "77", "86", "95"))
EffectRequiredLevel =    t2(("20", "25", "30", "35", "40", "43", "47"))

DDTinctureMetalCommon =  t2(("Alloy", "Fine Alloy", "Mithril", "Adamantium", 
                             "Asterite", "Netherium", "Arcanium",))
EffectMetal = d2({
    'Albion'   : DDTinctureMetalCommon,
    'Hibernia' : t2(("Dolomite", "Cobolt", "Carbide", "Sapphire", 
                     "Diamond", "Netherite", "Arcanite",)),
    'Midgard'  : DDTinctureMetalCommon,
})

DDEffectSubtable = d2({
    'Charged Effect':     DDEffectDamageSubtable,
    'Reactive Effect': t2(DDEffectDamageSubtable[-3:]),
    'Offensive Effect':   DDEffectDamageSubtable,
})

EffectTable = {
    'Direct Damage (Fire)' :     ('Fire',   DDEffectSubtable),
    'Direct Damage (Cold)' :     ('Cold',   DDEffectSubtable),
    'Direct Damage (Energy)' :   ('Energy', DDEffectSubtable),
    'Direct Damage (Spirit)' :   ('Spirit', DDEffectSubtable),
    'Damage Over Time' :         ('Eroding',   t2(("64",))),
    'Self AF Buff' :             ('Hardening', t2(("75",))),
    'Self Melee Health Buffer' : ('Ablative', d2({
                                      'Charged Effect':   t2(("50",)),
                                      'Reactive Effect':  t2(("100",)),
                                      'Offensive Effect': t2(("50",)), })),
    'Self Melee Haste Buff' :    ('Celeric', d2({
                                      'Charged Effect':   t2(("17",)),
                                      'Reactive Effect':  t2(("20",)),
                                      'Offensive Effect': t2(("20",)), })),
    'Self Damage Shield Buff' :  ('Shard', d2({
                                      'Charged Effect':   t2(("4",)),
                                      'Reactive Effect':  t2(("5",)),
                                      'Offensive Effect': t2(("5",)), })),
}

ProcEffectList = EffectTable.keys()
ProcEffectList.sort()
ProcEffectList = t2(ProcEffectList)


EffectTable.update({
    'Lifedrain' :                ('Leeching',     t2(("65",))),
    'Str/Con Debuff' :           ('Withering',    t2(("56",))),
    'Dex/Qui Debuff' :           ('Crippling',    t2(("56",))),
    'Self Damage Add Buff' :     ('Honing',       t2(("11",))),
    'Self Acuity Buff' :         ('Enlightening', t2(("75",))),
})

StableEffectList = EffectTable.keys()
StableEffectList.sort()
StableEffectList = t2(StableEffectList)

EffectTable['Unused'] = (UnusedList,)
EffectTable = d2(EffectTable)

EffectItemNames = d2({
    'Charged Effect' :   (StableEffectList, "Stable",   "Tincture",),
    'Reactive Effect' :  (ProcEffectList,   "Reactive", "Armor Tincture",),
    'Offensive Effect' : (ProcEffectList,   "Volatile", "Weapon Tincture",),
})


# Borrowed from Stable which is the most complete crafted list,
# add more non-craftable effect types here:
#
EffectItemList = t2(
     StableEffectList + (
    'Unique Effect...',
))


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
  GemTables[realm] = d2(GemTables[realm])
GemTables = d2(GemTables)


ValuesLists = d2({
    'Stat' :    StatValues,
    'Resist' :  ResistValues,
    'Hits' :    HitsValues,
    'Power' :   PowerValues,
    'Focus' :   FocusValues,
    'Skill' :   SkillValues,
    'Unused' :  UnusedValues,
})


Caps = dict.fromkeys(ResistList, 'Resist')
Caps.update(Caps.fromkeys(StatList, 'Stat'))
Caps = d2(Caps)


# Bonuses are given as % of level + add constant
# e.g. [ .25,  1] is the level / 4 + 1
#      [   0, 10] is a fixed 10
#      [   4,  0] is the level * 4
#
HighCapBonusList = d2({
    'Stat'                      : ( 1.50,  0 ),
    'Resist'                    : (  .50,  1 ),
    'Hits'                      : ( 4.00,  0 ),
    'Power'                     : (  .50,  1 ),
    'Skill'                     : (  .20,  1 ),
    'Cap'                       : (  .50,  1 ),
    'Hits Cap'                  : ( 4.00,  0 ),
    'Power Cap'                 : ( 1.00,  0 ),
    'AF Cap'                    : ( 1.00,  0 ),
    'PvE Bonus'                 : (  .20,  0 ),
    'Other Bonus'               : (  .20,  0 ),
    '% Power Pool'              : (  .50,  0 ),
    'Stat Buff Effectiveness'   : (  .50,  0 ),
    'Stat Debuff Effectiveness' : (  .50,  0 ),
    'Healing Effectiveness'     : (  .50,  0 ),
    'Duration of Spells'        : (  .50,  0 ),
    'Fatigue'                   : (  .50,  0 ),
    'AF'                        : ( 1.00,  0 ),
    'Arrow Recovery'            : ( 1.00,  0 ), 
    'Death Experience Loss Reduction' : ( 1.00,  0 ),
})


MaterialGems = t2(( 'Lo',   'Um',   'On',    'Ee',      'Pal',     'Mon',    'Ros',      'Zo',    'Kath',     'Ra',))

GemCosts =     t2(( 160,    920,   3900,   13900,      40100,     88980,   133000,    198920,    258240,   296860, ))

RemakeCosts =  t2(( 120,    560,   1740,    5260,      14180,     30660,    45520,     67680,     87640,   100700, ))

GemNames =     t2(('Raw','Uncut','Rough','Flawed','Imperfect','Polished','Faceted','Precious','Flawless','Perfect',))


LiquidsOrder = t2((
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
    'Undead Ash and Holy Water',
))

DustsOrder = t2((
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
    'Unseelie Dust',
))

GemLiquids = d2({ 
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
    'Brilliant' :         ('Draconic Fire', 'Mystic Energy', 'Treant Blood'),
    'Finesse' :           ('Draconic Fire', 'Mystic Energy', 'Treant Blood'),
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
    'Unholy' :             'Air Elemental Essence', 
})

GemDusts = d2({ 
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
    'Arcane Spell Stone' : 'Other Worldly Dust',
})

GemSubName = d2({ 
    'Stat' :   'Essence', 
    'Resist' : 'Shielding', 
    'Hits' :   'Essence', 
    'Power' :  'Essence', 
    'Focus' :  '', 
    'Skill' :  '', 
})


HotkeyGems = d2({
    'Albion' : d2({
        'Fiery Essence Jewel' :             0,
        'Earthen Essence Jewel' :           2,
        'Vapor Essence Jewel' :             4,
        'Airy Essence Jewel' :              6,
        'Watery Essence Jewel' :            8,
        'Heated Essence Jewel' :           10,
        'Dusty Essence Jewel' :            12,
        'Icy Essence Jewel' :              14,
        'Earthen Shielding Jewel' :        16,
        'Icy Shielding Jewel' :            18,
        'Heated Shielding Jewel' :         20,
        'Light Shielding Jewel' :          22,
        'Airy Shielding Jewel' :           24,
        'Vapor Shielding Jewel' :          26,
        'Dusty Shielding Jewel' :          28,
        'Fiery Shielding Jewel' :          30,
        'Watery Shielding Jewel' :         32,
        'Vapor Battle Jewel' :             34,
        'Fiery Battle Jewel' :             36,
        'Earthen Battle Jewel' :           38,
        'Airy Battle Jewel' :	           40,
        'Dusty Battle Jewel' :             42,
        'Heated Battle Jewel' :            44,
        'Watery War Sigil' :               46,
        'Fiery War Sigil' :                48,
        'Dusty War Sigil' :                50,
        'Heated War Sigil' :               52,
        'Earthen War Sigil' :              54,
        'Airy War Sigil' :                 56,
        'Vapor War Sigil' :                58,
        'Icy War Sigil' :                  60,
        'Fiery Fervor Sigil' :             62,
        'Airy Fervor Sigil' :              64,
        'Watery Fervor Sigil' :            66,
        'Earthen Fervor Sigil' :           68,
        'Vapor Fervor Sigil' :	           70,
        'Earthen Evocation Sigil' :        72,
        'Icy Evocation Sigil' :            74,
        'Fiery Evocation Sigil' :          76,
        'Airy Evocation Sigil' :           78,
        'Heated Evocation Sigil' :         80,
        'Dusty Evocation Sigil' :          82,
        'Vapor Evocation Sigil' :          84,
        'Watery Evocation Sigil' :         86,
        'Blood Essence Jewel' :            88,
        'Mystical Essence Jewel' :         90,
        'Earth Sigil' :                    92,
        'Ice Sigil' :                      94,
        'Fire Sigil' :                     96,
        'Air Sigil' :                      98,
        'Heat Sigil' :                    100,
        'Dust Sigil' :                    102,
        'Vapor Sigil' :                   104,
        'Water Sigil' :                   106,
        'Molten Magma War Sigil' :        108,
        'Vacuous Fervor Sigil' :          110,
        'Salt Crusted Fervor Sigil' :     112,
        'Ashen Fervor Sigil' :            114,
        'Steaming Fervor Sigil' :         116,
        'Vacuous Sigil' :                 118,
        'Salt Crusted Sigil' :            120,
        'Ashen Sigil' :                   122,
        'Brilliant Sigil' :               124,
        'Finesse War Sigil' :             126,
        'Finesse Fervor Sigil' :          128,
    }),

    'Hibernia' : d2({
        'Fiery Essence Jewel' :             0,
        'Earthen Essence Jewel' :           2,
        'Vapor Essence Jewel' :             4,
        'Airy Essence Jewel' :              6,
        'Watery Essence Jewel' :            8,
        'Heated Essence Jewel' :           10,
        'Dusty Essence Jewel' :            12,
        'Icy Essence Jewel' :              14,
        'Earthen Shielding Jewel' :        16,
        'Icy Shielding Jewel' :            18,
        'Heated Shielding Jewel' :         20,
        'Light Shielding Jewel' :          22,
        'Airy Shielding Jewel' :           24,
        'Vapor Shielding Jewel' :          26,
        'Dusty Shielding Jewel' :          28,
        'Fiery Shielding Jewel' :          30,
        'Watery Shielding Jewel' :         32,
        'Vapor Battle Jewel' :             34,
        'Fiery Battle Jewel' :             36,
        'Earthen Battle Jewel' :           38,
        'Airy Battle Jewel' :              40,
        'Dusty Battle Jewel' :             42,
        'Heated Battle Jewel' :            44,
        'Watery War Spell Stone' :         46,
        'Fiery War Spell Stone' :          48,
        'Dusty War Spell Stone' :          50,
        'Heated War Spell Stone' :         52,
        'Earthen War Spell Stone' :        54,
        'Icy War Spell Stone' :            56,
        'Airy War Spell Stone' :           58,
        'Fiery Nature Spell Stone' :       60,
        'Watery Nature Spell Stone' :      62,
        'Earthen Nature Spell Stone' :     64,
        'Airy Nature Spell Stone' :        66,
        'Airy Arcane Spell Stone' :        68,
        'Fiery Arcane Spell Stone' :       70,
        'Watery Arcane Spell Stone' :      72,
        'Vapor Arcane Spell Stone' :       74,
        'Icy Arcane Spell Stone' :         76,
        'Earthen Arcane Spell Stone' :     78,
        'Blood Essence Jewel' :            80,
        'Mystical Essence Jewel' :         82,
        'Fire Spell Stone' :               84,
        'Water Spell Stone' :              86,
        'Vapor Spell Stone' :              88,
        'Ice Spell Stone' :                90,
        'Earth Spell Stone' :              92,
        'Light War Spell Stone' :          94,
        'Steaming Nature Spell Stone' :    96,
        'Oozing Nature Spell Stone' :      98,
        'Mineral Encrusted Nature Spell Stone' : 100,
        'Steaming Spell Stone' :          102,
        'Oozing Spell Stone' :            104,
        'Mineral Encrusted Spell Stone' : 106,
        'Spectral Spell Stone' :          108,
        'Phantasmal Spell Stone' :        110,
        'Ethereal Spell Stone' :          112,
        'Spectral Arcane Spell Stone' :   114,
        'Phantasmal Arcane Spell Stone' : 116,
        'Ethereal Arcane Spell Stone' :   118,
        'Shadowy Arcane Spell Stone' :    120,
        'Embracing Arcane Spell Stone' :  122,
        'Aberrant Arcane Spell Stone' :   124,
        'Brilliant Spell Stone' :         126,
        'Finesse War Spell Stone' :       128,
        'Finesse Nature Spell Stone' :    130,
    }),

    'Midgard' : d2({
        'Fiery Essence Jewel' :             0,
        'Earthen Essence Jewel' :           2,
        'Vapor Essence Jewel' :             4,
        'Airy Essence Jewel' :              6,
        'Watery Essence Jewel' :            8,
        'Heated Essence Jewel' :           10,
        'Dusty Essence Jewel' :            12,
        'Icy Essence Jewel' :              14,
        'Earthen Shielding Jewel' :        16,
        'Icy Shielding Jewel' :            18,
        'Heated Shielding Jewel' :         20,
        'Light Shielding Jewel' :          22,
        'Airy Shielding Jewel' :           24,
        'Vapor Shielding Jewel' :          26,
        'Dusty Shielding Jewel' :          28,
        'Fiery Shielding Jewel' :          30,
        'Watery Shielding Jewel' :         32,
        'Vapor Battle Jewel' :             34,
        'Fiery Battle Jewel' :             36,
        'Earthen Battle Jewel' :           38,
        'Airy Battle Jewel' :              40,
        'Dusty Battle Jewel' :             42,
        'Heated Battle Jewel' :            44,
        'Watery War Rune' :                46,
        'Fiery War Rune' :                 48,
        'Earthen War Rune' :               50,
        'Heated War Rune' :                52,
        'Airy War Rune' :                  54,
        'Vapor War Rune' :                 56,
        'Icy War Rune' :                   58,
        'Earthen Primal Rune' :            60,
        'Airy Primal Rune' :               62,
        'Fiery Primal Rune' :              64,
        'Icy Chaos Rune' :                 66,
        'Dusty Chaos Rune' :               68,
        'Heated Chaos Rune' :              70,
        'Vapor Chaos Rune' :               72,
        'Watery Chaos Rune' :              74,
        'Airy Chaos Rune' :                76,
        'Fiery Chaos Rune' :               78,
        'Blood Essence Jewel' :            82,
        'Mystical Essence Jewel' :         84,
        'Ice Rune' :                       86,
        'Dust Rune' :                      88,
        'Heat Rune' :                      90,
        'Vapor Rune' :                     92,
        'Lightning Charged War Rune' :     94,
        'Ashen Primal Rune' :              96,
        'Ashen Rune' :                     98,
        'Blighted Rune' :                 100 ,
        'Valiant Primal Rune' :           104,
        'Blighted Primal Rune' :          106,
        'Unholy Primal Rune' :            108,
        'Brilliant Rune' :                110,
        'Finesse War Rune' :              112,
        'Finesse Primal Rune' :           114,
    }),
})

OCStartPercentages = (0, 10, 20, 30, 50, 70)

ImbueMultipliers = d2({ 
    'Stat' :   1.0, 
    'Resist' : 2.0, 
    'Skill' :  5.0, 
    'Hits' :   0.25, 
    'Power' :  2.0, 
    'Focus' :  1.0, 
    'Unused' : 0.0, 
})

QualityValues = t2(('94', '95', '96', '97', '98', '99', '100'))

GemQualOCModifiers = d2({ 
      '' :  0, 
    '94' :  0, 
    '95' :  0, 
    '96' :  1, 
    '97' :  3, 
    '98' :  5, 
    '99' :  8, 
   '100' : 11, 
})

ItemQualOCModifiers = d2({ 
    '94' :  0, 
    '95' :  0, 
    '96' :  6, 
    '97' :  8, 
    '98' : 10, 
    '99' : 18, 
   '100' : 26, 
})

ImbuePts = (
    ( 0, 1, 1, 1, 1, 1, 1),
    ( 1, 1, 1, 1, 1, 2, 2),
    ( 1, 1, 1, 2, 2, 2, 2),
    ( 1, 1, 2, 2, 2, 3, 3),
    ( 1, 2, 2, 2, 3, 3, 4),
    ( 1, 2, 2, 3, 3, 4, 4),
    ( 2, 2, 3, 3, 4, 4, 5),
    ( 2, 3, 3, 4, 4, 5, 5),
    ( 2, 3, 3, 4, 5, 5, 6),
    ( 2, 3, 4, 4, 5, 6, 7),
    ( 2, 3, 4, 5, 6, 6, 7),
    ( 3, 4, 4, 5, 6, 7, 8),
    ( 3, 4, 5, 6, 6, 7, 9),
    ( 3, 4, 5, 6, 7, 8, 9),
    ( 3, 4, 5, 6, 7, 8,10),
    ( 3, 5, 6, 7, 8, 9,10),
    ( 4, 5, 6, 7, 8,10,11),
    ( 4, 5, 6, 8, 9,10,12),
    ( 4, 6, 7, 8, 9,11,12),
    ( 4, 6, 7, 8,10,11,13),
    ( 4, 6, 7, 9,10,12,13),
    ( 5, 6, 8, 9,11,12,14),
    ( 5, 7, 8,10,11,13,15),
    ( 5, 7, 9,10,12,13,15),
    ( 5, 7, 9,10,12,14,16),
    ( 5, 8, 9,11,12,14,16),
    ( 6, 8,10,11,13,15,17),
    ( 6, 8,10,12,13,15,18),
    ( 6, 8,10,12,14,16,18),
    ( 6, 9,11,12,14,16,19),
    ( 6, 9,11,13,15,17,20),
    ( 7, 9,11,13,15,17,20),
    ( 7,10,12,14,16,18,21),
    ( 7,10,12,14,16,19,21),
    ( 7,10,12,14,17,19,22),
    ( 7,10,13,15,17,20,23),
    ( 8,11,13,15,17,20,23),
    ( 8,11,13,16,18,21,24),
    ( 8,11,14,16,18,21,24),
    ( 8,11,14,16,19,22,25),
    ( 8,12,14,17,19,22,26),
    ( 9,12,15,17,20,23,26),
    ( 9,12,15,18,20,23,27),
    ( 9,13,15,18,21,24,27),
    ( 9,13,16,18,21,24,28),
    ( 9,13,16,19,22,25,29),
    (10,13,16,19,22,25,29),
    (10,14,17,20,23,26,30),
    (10,14,17,20,23,27,31),
    (10,14,17,20,23,27,31),
    (10,15,18,21,24,28,32),
)


BodyHitOdds = d2({
    'Chest' : .40,
    'Legs'  : .25,
    'Arms'  : .15,
    'Head'  : .10,
    'Hands' : .05,
    'Feet'  : .05,
})

PieceTabList = t2((
    'Chest', 'Arms', 'Head', 'Legs', 'Hands', 'Feet', 
    'Right Hand', 'Left Hand', '2 Handed', 'Ranged', 'Spare',
))

JewelTabList = t2((
    'Neck', 'Cloak', 'Jewel', 'Belt', 
    'Left Ring', 'Right Ring', 'Left Wrist', 'Right Wrist',
))

TabList = t2(PieceTabList + JewelTabList)

FileExt = d2({ 
    'Neck' :         'neck', 
    'Cloak' :        'cloak', 
    'Belt' :         'belt', 
    'Jewel' :        'jewel',
    'Left Ring' :    'ring', 
    'Right Ring' :   'ring', 
    'Left Wrist' :  ('bracer', 'wrist',),
    'Right Wrist' : ('bracer', 'wrist',), 
    'Chest' :        'chest', 
    'Arms' :         'arms', 
    'Head' :         'helm', 
    'Legs' :         'legs', 
    'Feet' :         'boots', 
    'Hands' :        'hands',
    'Right Hand' :   'wep', 
    'Left Hand' :   ('lhwep', 'shield',),
    '2 Handed' :    ('2hwep', 'lhwep', 'wep',),
    'Ranged' :       'ranged', 
    'Spare' :        '*', 
})


ShieldTypes = t2((
    'Rowan',     'Elm',       'Oaken',     'Ironwood',  'Heartwood', 
    'Runewood',  'Stonewood', 'Ebonwood',  'Dyrwood',   'Duskwood',
))


#Races[realm] Now RaceList[realm]
#RacialResists[realm] Now Races[realm]['Resists']

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
#   '???' : 'Akatsuki', 
})


# Rename old skills to new skills, from previously saved template files
#
FixEffectsTable = {
    'Bonedancing' :    'Bone Army',
    'PainWorking' :    'Painworking', 
    'Subterranean' :   'Cave Magic',
    'BeastCraft' :     'Beastcraft',
    'Arboreal' :       'Arboreal Path',
    'Arboreal Focus' : 'Arboreal Path',
    'Body Focus' :     'Body Magic', 
    'Cold Focus' :     'Cold Magic', 
    'Earth Focus' :    'Earth Magic',
    'Fire Focus' :     'Fire Magic',
    'Matter Focus' :   'Matter Magic',
    'Mind Focus' :     'Mind Magic',
    'Spirit Focus' :   'Spirit Magic',
    'Wind Focus' :     'Wind Magic',

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
    'Healing Bonus' :          'Healing Effectiveness',
    'Spell Damage Bonus' :     'Spell Damage',
    'Magic Damage' :           'Spell Damage',
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

    'PvE' : 'PvE Bonus',

    'Body Resist' :     'Body', 
    'Cold Resist' :     'Cold', 
    'Heat Resist' :     'Heat', 
    'Energy Resist' :   'Energy',
    'Matter Resist' :   'Matter', 
    'Spirit Resist' :   'Spirit',
    'Crush Resist' :    'Crush', 
    'Thrust Resist' :   'Thrust', 
    'Slash Resist' :    'Slash', 
}
