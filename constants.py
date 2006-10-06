# constants.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

__all__ = [
  'ScVersion',
  'GemLists', 'DropLists', 'CraftedLists',
  'TypeList', 'EffectTypeList', 'DropTypeList', 'CraftedTypeList',
  'ValuesLists', 'CraftedValuesLists',
  'QualityValues', 'EstimatedMakes', 'ImbuePts',
  'OCStartPercentages', 'GemQualOCModifiers', 'ItemQualOCModifiers',
  'FileExt', 'Caps', 'HighCapBonusList', 'BodyHitOdds',
  'GemTables', 'GemDusts', 'GemLiquids', 'GemSubName',
  'GemNames', 'MaterialGems', 'GemCosts', 'RemakeCosts', 
  'EffectTypeNames', 'EffectItemNames', 'EffectMetal', 'EffectRequiredLevel',
  'FixEffectsTable', 'HotkeyGems', 'ImbueMultipliers',  
  'ShieldTypes',
  'TabList', 'PieceTabList', 'JewelTabList',
]

ScVersion = "Kort's Spellcrafting Calulator 1.46"

from Character import *
from tuple2 import * 
from dict2 import * 
import sys

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

# Placeholder
unusedTable = d2({})

unusedList = t2()

unusedValues = t2()

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
    'Salt Crusted' :       'Mystic Energy',
    'Steaming Spell' :     'Swamp Fog',
    'Steaming Nature' :    'Swamp Fog',
    'Steaming Fervor' :    'Heat From an Unearthly Pyre',
    'Oozing' :             'Treant Blood',
    'Mineral Encrusted' :  'Heat From an Unearthly Pyre',
    'Lightning Charged' :  'Leviathan Blood',
    'Molten Magma' :       'Leviathan Blood',
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
    'Essence Jewel' :      'Essence of Life',
    'Shielding Jewel' :    'Ground Draconic Scales',
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


type = 'Essence Jewel'

statTableOrdered = (
    ('Strength',     'Fiery',),
    ('Constitution', 'Earthen',),
    ('Dexterity',    'Vapor',),
    ('Quickness',    'Airy',),
    ('Intelligence', 'Dusty',),
    ('Piety',        'Watery',),
    ('Charisma',     'Icy',),
    ('Empathy',      'Heated',),
)

statTable = dict(statTableOrdered)
for (key, val) in statTable.iteritems():
    statTable[key] = (val, type, GemDusts[type], GemLiquids[val],)
statTable = d2(statTable)

statList = t2(map(lambda(x): x[0], statTableOrdered))

del statTableOrdered

statValues = t2(('1', '4', '7', '10', '13', '16', '19', '22', '25', '28',))

# Duplicate the Stat lists as DropStat lists, add non-craftable 'Acuity' stat
#
dropStatList = t2(statList + (
    'Acuity',
))

dropStatTable = dict().fromkeys(dropStatList)


hitsTable = d2({
    'Hits' : ('Blood', type, GemDusts[type], GemLiquids['Blood'],),
})

hitsList = t2(hitsTable.keys())

hitsValues = t2(('4', '12', '20', '28', '36', '44', '52', '60', '68', '76',))


powerTable = d2({
    'Power' : ('Mystical', type, GemDusts[type], GemLiquids['Mystical'],),
})

powerList = t2(powerTable.keys())

powerValues = t2(('1', '2', '3', '5', '7', '9', '11', '13', '15', '17'))


type = 'Shielding Jewel'

resistTableOrdered = (
    ('Body',   'Dusty',),
    ('Cold',   'Icy',),
    ('Heat',   'Heated',),
    ('Energy', 'Light',),
    ('Matter', 'Earthen',),
    ('Spirit', 'Vapor',),
    ('Crush',  'Fiery',),
    ('Thrust', 'Airy',),
    ('Slash',  'Watery',),
)

resistTable = dict(resistTableOrdered)
for (key, val) in resistTable.iteritems():
    resistTable[key] = (val, type, GemDusts[type], GemLiquids[val])
resistTable = d2(resistTable)

resistList = map(lambda(x): x[0], resistTableOrdered)

resistValues = t2(('1', '2', '3', '5', '7', '9', '11', '13', '15', '17',))

del resistTableOrdered


focusTable = {

    'Albion' : {

        'All Spell Lines' : ('Brilliant', 'Sigil',),
        'Body Magic' :      ('Heat', 'Sigil',),
        'Cold Magic' :      ('Ice', 'Sigil',),
        'Death Servant' :   ('Ashen', 'Sigil',),
        'Deathsight' :      ('Vacuous', 'Sigil',),
        'Earth Magic' :     ('Earth', 'Sigil',),
        'Fire Magic' :      ('Fire', 'Sigil',),
        'Matter Magic' :    ('Dust', 'Sigil',),
        'Mind Magic' :      ('Water', 'Sigil',),
        'Painworking' :     ('Salt Crusted', 'Sigil',),
        'Spirit Magic' :    ('Vapor', 'Sigil',),
        'Wind Magic' :      ('Air', 'Sigil',),
    },

    'Hibernia' : {

        'All Spell Lines' : ('Brilliant', 'Spell Stone',),
        'Arboreal Path' :   ('Steaming', 'Spell Stone',),
        'Creeping Path' :   ('Oozing', 'Spell Stone',),
        'Enchantments' :    ('Vapor', 'Spell Stone',),
        'Ethereal Shriek' : ('Ethereal', 'Spell Stone',),
        'Light' :           ('Fire', 'Spell Stone',),
        'Mana' :            ('Water', 'Spell Stone',),
        'Mentalism' :       ('Earth', 'Spell Stone',),
        'Phantasmal Wail':  ('Phantasmal', 'Spell Stone',),
        'Spectral Guard' :  ('Spectral', 'Spell Stone',),
        'Verdant Path' :    ('Mineral Encrusted', 'Spell Stone',),
        'Void' :            ('Ice', 'Spell Stone',),
    },

    'Midgard' : {

        'All Spell Lines' : ('Brilliant', 'Rune',),
        'Bone Army' :       ('Ashen', 'Rune',),
        'Cursing' :         ('Blighted', 'Rune',),
        'Darkness' :        ('Ice', 'Rune',),
        'Runecarving' :     ('Heat', 'Rune',),
        'Summoning' :       ('Vapor', 'Rune',),
        'Suppression' :     ('Dust', 'Rune',),
    },
}

focusTable['All'] = {}
for realm in Realms:
  for (key, val) in focusTable[realm].iteritems():
    if GemLiquids.has_key(val[0]):
      liquid = GemLiquids[val[0]]
    else:
      liquid = GemLiquids[val[0] + " " + val[1].split()[0]]
    focusTable[realm][key] = (val[0], val[1], GemDusts[val[1]], liquid,)
  focusTable[realm] = d2(focusTable[realm])
  focusTable['All'].update(focusTable[realm])
focusTable['All'] = d2(focusTable['All'])
focusTable = d2(focusTable)

focusList = {}
for realm in focusTable.keys():
  focusList[realm] = focusTable[realm].keys()
  focusList[realm].sort()
  focusList[realm] = t2(focusList[realm])
focusList = d2(focusList)

focusValues = t2(('5', '10', '15', '20', '25', '30', '35', '40', '45', '50',))


skillTable = { 

    'Albion' : {

        'All Melee Weapon Skills' : ('Finesse', 'War Sigil',),
        'All Magic Skills' :  ('Finesse', 'Fervor Sigil',),
        'Body Magic' :        ('Heated', 'Evocation Sigil',),
        'Chants' :            ('Earthen', 'Fervor Sigil',),
        'Cold Magic' :        ('Icy', 'Evocation Sigil',),
        'Critical Strike' :   ('Heated', 'Battle Jewel',),
        'Crossbow' :          ('Vapor', 'War Sigil',),
        'Crush' :             ('Fiery', 'War Sigil',),
        'Death Servant' :     ('Ashen', 'Fervor Sigil',),
        'Deathsight' :        ('Vacuous', 'Fervor Sigil',),
        'Dual Wield' :        ('Icy', 'War Sigil',),
        'Earth Magic' :       ('Earthen', 'Evocation Sigil',),
        'Enhancement' :       ('Airy', 'Fervor Sigil',),
        'Envenom' :           ('Dusty', 'Battle Jewel',),
        'Flexible' :          ('Molten Magma', 'War Sigil',),
        'Fire Magic' :        ('Fiery', 'Evocation Sigil',),
        'Instruments' :       ('Vapor', 'Fervor Sigil',),
        'Longbow' :           ('Airy', 'War Sigil',),
        'Matter Magic' :      ('Dusty', 'Evocation Sigil',),
        'Mind Magic' :        ('Watery', 'Evocation Sigil',),
        'Painworking' :       ('Salt Crusted', 'Fervor Sigil',),
        'Parry' :             ('Vapor', 'Battle Jewel',),
        'Polearm' :           ('Earthen', 'War Sigil',),
        'Rejuvenation' :      ('Watery', 'Fervor Sigil',),
        'Shield' :            ('Fiery', 'Battle Jewel',),
        'Slash' :             ('Watery', 'War Sigil',),
        'Smite' :             ('Fiery', 'Fervor Sigil',),
        'Soulrending' :       ('Steaming', 'Fervor Sigil',),
        'Spirit Magic' :      ('Vapor', 'Evocation Sigil',),
        'Staff' :             ('Earthen', 'Battle Jewel',),
        'Stealth' :           ('Airy', 'Battle Jewel',),
        'Thrust' :            ('Dusty', 'War Sigil',),
        'Two Handed' :        ('Heated', 'War Sigil',),
        'Wind Magic' :        ('Airy', 'Evocation Sigil',),
    }, 

    'Hibernia' : {

        'All Melee Weapon Skills' : ('Finesse', 'War Spell Stone',),
        'All Magic Skills' :  ('Finesse', 'Nature Spell Stone',),
        'Arboreal Path' :     ('Steaming', 'Nature Spell Stone',),
        'Blades' :            ('Watery', 'War Spell Stone',),
        'Blunt' :             ('Fiery', 'War Spell Stone',),
        'Celtic Dual' :       ('Icy', 'War Spell Stone',),
        'Celtic Spear' :      ('Earthen', 'War Spell Stone',),
        'Creeping Path' :     ('Oozing', 'Nature Spell Stone',),
        'Critical Strike' :   ('Heated', 'Battle Jewel',),
        'Dementia' :          ('Aberrant', 'Arcane Spell Stone',),
        'Enchantments' :      ('Vapor', 'Arcane Spell Stone',),
        'Envenom' :           ('Dusty', 'Battle Jewel',),
        'Ethereal Shriek' :   ('Ethereal', 'Arcane Spell Stone',),
        'Large Weaponry' :    ('Heated', 'War Spell Stone',),
        'Light' :             ('Fiery', 'Arcane Spell Stone',), 
        'Mana' :              ('Watery', 'Arcane Spell Stone',),
        'Mentalism' :         ('Earthen', 'Arcane Spell Stone',),
        'Music' :             ('Airy', 'Nature Spell Stone',),
        'Nature' :            ('Earthen', 'Nature Spell Stone',),
        'Nurture' :           ('Fiery', 'Nature Spell Stone',),
        'Parry' :             ('Vapor', 'Battle Jewel',),
        'Phantasmal Wail' :   ('Phantasmal', 'Arcane Spell Stone',),
        'Piercing' :          ('Dusty', 'War Spell Stone',),
        'Recurve Bow' :       ('Airy', 'War Spell Stone',),
        'Regrowth' :          ('Watery', 'Nature Spell Stone',),
        'Scythe' :            ('Light', 'War Spell Stone',),
        'Shadow Mastery' :    ('Shadowy', 'Arcane Spell Stone',),
        'Shield' :            ('Fiery', 'Battle Jewel',),
        'Spectral Guard' :    ('Spectral', 'Arcane Spell Stone',),
        'Staff' :             ('Earthen', 'Battle Jewel',),
        'Stealth' :           ('Airy', 'Battle Jewel',),
        'Valor' :             ('Airy', 'Arcane Spell Stone',),
        'Vampiiric Embrace' : ('Embracing', 'Arcane Spell Stone',),
        'Verdant Path' :      ('Mineral Encrusted', 'Nature Spell Stone',),
        'Void' :              ('Icy', 'Arcane Spell Stone',),
    },

    'Midgard' : { 

        'All Melee Weapon Skills' : ('Finesse', 'War Rune',),
        'All Magic Skills' :  ('Finesse', 'Primal Rune',),
        'Augmentation' :      ('Airy', 'Chaos Rune',),
        'Axe' :               ('Earthen', 'War Rune',),
        'Battlesongs' :       ('Airy', 'Primal Rune',),
        'Beastcraft' :        ('Earthen', 'Primal Rune',),
        'Bone Army' :         ('Ashen', 'Primal Rune',),
        'Cave Magic' :        ('Fiery', 'Chaos Rune',),
        'Composite Bow' :     ('Airy', 'War Rune',),
        'Critical Strike' :   ('Heated', 'Battle Jewel',),
        'Cursing' :           ('Blighted', 'Primal Rune',),
        'Darkness' :          ('Icy', 'Chaos Rune',),
        'Envenom' :           ('Dusty', 'Battle Jewel',),
        'Hammer' :            ('Fiery', 'War Rune',),
        'Hand To Hand' :      ('Lightning Charged', 'War Rune',),
        'Hexing' :            ('Unholy', 'Primal Rune',),
        'Left Axe' :          ('Icy', 'War Rune',),
        'Mending' :           ('Watery', 'Chaos Rune',),
        'Odin\'s Will' :      ('Valiant', 'Primal Rune',),
        'Parry' :             ('Vapor', 'Battle Jewel',),
        'Runecarving' :       ('Heated', 'Chaos Rune',),
        'Shield' :            ('Fiery', 'Battle Jewel',),
        'Spear' :             ('Heated', 'War Rune',),
        'Staff' :             ('Earthen', 'Battle Jewel',),
        'Stealth' :           ('Airy', 'Battle Jewel',),
        'Stormcalling' :      ('Fiery', 'Primal Rune',),
        'Summoning' :         ('Vapor', 'Chaos Rune',),
        'Suppression' :       ('Dusty', 'Chaos Rune',),
        'Sword' :             ('Watery', 'War Rune',),
        'Thrown Weapons' :    ('Vapor', 'War Rune',),
    },
}

skillTable['All'] = {}
for realm in Realms:
  for (key, val) in skillTable[realm].iteritems():
    if GemLiquids.has_key(val[0]):
      liquid = GemLiquids[val[0]]
    else:
      liquid = GemLiquids[val[0] + " " + val[1].split()[0]]
    skillTable[realm][key] = (val[0], val[1], GemDusts[val[1]], liquid,)
  skillTable[realm] = d2(skillTable[realm])
  skillTable['All'].update(skillTable[realm])
skillTable['All'] = d2(skillTable['All'])
skillTable = d2(skillTable)

skillList = {}
dropSkillList = {}

for realm in skillTable.keys():
  skills = skillTable[realm].keys()
  skills.sort()
  skillList[realm] = t2(skills)
  skills.insert(2, 'All Dual Wield Skills')
  skills.insert(3, 'All Archery Skills')
  # bug - CM Explorer shows +Witchcraft, but no craftable gem
  if realm == 'Midgard': skills.append('Witchcraft')
  dropSkillList[realm] = t2(skills)

skillList = d2(skillList)
dropSkillList = d2(dropSkillList)

skillValues = t2(('1', '2', '3', '4', '5', '6', '7', '8',))


capIncreaseList = t2(dropStatList + (
    'Hits', 
    'Power', 
    'AF',
))


otherBonusList = t2((
    '% Power Pool',
    'AF',
    'Archery Damage',
    'Archery Range',
    'Archery Speed',
    'Casting Speed',
    'Duration of Spells',
    'Fatigue',
    'Healing Effectiveness',
    'Melee Damage',
    'Melee Combat Speed',
    'Spell Damage',
    'Spell Piercing',
    'Spell Range',
    'Stat Buff Effectiveness',
    'Stat Debuff Effectiveness',
    'Style Damage',
    'Unique Bonus...',
))


pveBonusList = t2((
    'Arrow Recovery',
    'Bladeturn Reinforcement',
    'Block',
    'Concentration',
    'Damage Reduction',
    'Death Experience Loss Reduction',
    'Defensive',
    'Evade',
    'Negative Effect Duration Reduction',
    'Parry',
    'Piece Ablative',
    'Reactionary Style Damage',
    'Spell Power Cost Reduction',
    'Style Cost Reduction',
    'To Hit',
    'Unique PvE Bonus...',
))


EffectRequiredLevel =    t2(("47", "43", "40", "35", "30", "25", "20",))

ddMetalCommon =  t2(("Arcanium", "Netherium", "Asterite", 
                     "Adamantium", "Mithril", "Fine Alloy", "Alloy",))
EffectMetal = d2({
    'Albion'   : ddMetalCommon,
    'Hibernia' : t2(("Arcanite", "Netherite", "Diamond", 
                     "Sapphire", "Carbide", "Cobolt", "Dolomite",)),
    'Midgard'  : ddMetalCommon,
})

ddEffectDamageSubtable = t2(("95", "86", "77", "68", "59", "50", "41",))

offensiveEffectValues = d2({
    'Direct Damage (Fire)' :     ddEffectDamageSubtable,
    'Direct Damage (Cold)' :     ddEffectDamageSubtable,
    'Direct Damage (Energy)' :   ddEffectDamageSubtable,
    'Direct Damage (Spirit)' :   ddEffectDamageSubtable,
    'Damage Over Time' :         t2(("64",)),
    'Self AF Shield' :           t2(("75",)),
    'Self Melee Health Buffer' : t2(("50",)),
    'Self Melee Haste' :         t2(("20%",)),
    'Self Damage Shield' :       t2(("5.1",)),
})

reactiveEffectValues = offensiveEffectValues.copy()
reactiveEffectValues.update({
    'Direct Damage (Fire)' :     t2(ddEffectDamageSubtable[0:3]),
    'Direct Damage (Cold)' :     t2(ddEffectDamageSubtable[0:3]),
    'Direct Damage (Energy)' :   t2(ddEffectDamageSubtable[0:3]),
    'Direct Damage (Spirit)' :   t2(ddEffectDamageSubtable[0:3]),
    'Self Melee Health Buffer' : t2(("100",)),
})
reactiveEffectValues = d2(reactiveEffectValues)

chargedEffectValues = offensiveEffectValues.copy()
chargedEffectValues.update({
    'Self Melee Haste' :         t2(("17%",)),
    'Self Damage Shield' :       t2(("4.2",)),
    'Lifedrain' :                t2(("65",)),
    'Str/Con Debuff' :           t2(("56",)),
    'Dex/Qui Debuff' :           t2(("56",)),
    'Self Damage Add' :          t2(("11.3",)),
    'Self Acuity Buff' :         t2(("75",)),
})
chargedEffectValues = d2(chargedEffectValues)

procEffectList = offensiveEffectValues.keys()
procEffectList.sort()
procEffectList = t2(procEffectList)

stableEffectList = chargedEffectValues.keys()
stableEffectList.sort()
stableEffectList = t2(stableEffectList)

otherEffectList = t2(stableEffectList[:] + (
    "Unique Effect...",
))

EffectItemNames = d2({
    'Direct Damage (Fire)' :     t2(('Fiery', 'Fire',)),
    'Direct Damage (Cold)' :     t2(('', 'Cold',)),
    'Direct Damage (Energy)' :   t2(('', 'Energy',)),
    'Direct Damage (Spirit)' :   t2(('', 'Spirit',)),
    # Stables are Illbane's but don't confuse readers of Reactive/Volatile
    'Damage Over Time' :         t2(('', 'Eroding',)),
    'Self AF Shield' :           t2(('', 'Hardening',)),
    'Self Melee Health Buffer' : t2(('', 'Ablative',)),
    'Self Melee Haste' :         t2(('', 'Celeric',)),
    'Self Damage Shield' :       t2(('Barbed', 'Shard',)),
    'Lifedrain' :                t2(('Soul Drinker', 'Leeching',)),
    'Str/Con Debuff' :           t2(('', 'Withering',)),
    'Dex/Qui Debuff' :           t2(('Crippling', 'Crippling',)),
    'Self Damage Add' :          t2(('Keen', 'Honing',)),
    'Self Acuity Buff' :         t2(('Owl-runed', 'Enlightening',)),
})

EffectTypeNames = d2({
    'Charged Effect' :   t2(("Stable",   "Tincture",)),
    'Reactive Effect' :  t2(("Reactive", "Armor Tincture",)),
    'Offensive Effect' : t2(("Volatile", "Weapon Tincture",)),
})


GemTables = {
  'All': {
    'Stat' :    statTable,
    'Resist' :  resistTable,
    'Hits' :    hitsTable,
    'Power' :   powerTable,
    'Unused' :  unusedTable
  }
}

GemLists = {
  'All': {
    'Stat' :             statList,
    'Resist' :           resistList,
    'Hits' :             hitsList,
    'Power' :            powerList,
    'Unused' :           unusedList
  }
}

DropLists = {
  'All': {
    'Resist' :           resistList,
    'Hits' :             hitsList,
    'Power' :            powerList,
    'Unused' :           unusedList,
    'Stat' :             dropStatList,
    'Cap Increase' :     capIncreaseList,
    'PvE Bonus' :        pveBonusList,
    'Other Bonus' :      otherBonusList,
    'Charged Effect' :   otherEffectList,
    'Reactive Effect' :  otherEffectList,
    'Offensive Effect' : otherEffectList,
    'Other Effect' :     otherEffectList,
  }
}

# Only use GemTables['All'] when the specific realm of craft isn't known as
# there are many multi-realm gems which have different names and recipes
#
for realm in Realms:
  GemTables[realm] = {}
  GemTables[realm].update(GemTables['All'])
  GemLists[realm] = {}
  GemLists[realm].update(GemLists['All'])
  DropLists[realm] = {}
  DropLists[realm].update(DropLists['All'])
for realm in GemTables.keys():
  GemTables[realm]['Focus'] = focusTable[realm]
  GemTables[realm]['Skill'] = skillTable[realm]
  GemTables[realm] = d2(GemTables[realm])
  GemLists[realm]['Focus'] = focusList[realm]
  DropLists[realm]['Focus'] = focusList[realm]
  GemLists[realm]['Skill'] = skillList[realm]
  DropLists[realm]['Skill'] = dropSkillList[realm]
  GemLists[realm] = d2(GemLists[realm])
  DropLists[realm] = d2(DropLists[realm])
GemTables = d2(GemTables)
GemLists =  d2(GemLists)
DropLists = d2(DropLists)


ValuesLists = d2({
    'Stat' :             statValues,
    'Resist' :           resistValues,
    'Hits' :             hitsValues,
    'Power' :            powerValues,
    'Focus' :            focusValues,
    'Skill' :            skillValues,
    'Unused' :           unusedValues,
})


CraftedValuesLists = d2({
    'Unused' :             unusedValues,
    'Focus' :              t2(('50',)),
    'Skill' :              t2(('3',)),
    'Cap Increase' : d2({
        'Strength' :       t2(('5',)),
        'Constitution' :   t2(('5',)),
        'Dexterity' :      t2(('5',)),
        'Quickness' :      t2(('5',)),
        'Acuity' :         t2(('5',)),
        'Hits' :           t2(('40',)),
    }),
    'Other Bonus' : d2({
        '% Power Pool' :   t2(('5',)),
        'AF' :             t2(('10',)),
        'Healing Effectiveness' :   t2(('5',)),
        'Stat Buff Effectiveness' : t2(('5',)),
        'Archery Damage' : t2(('2',)),
        'Melee Damage' :   t2(('2',)),
        'Spell Damage' :   t2(('2',)),
    }),
    'PvE Bonus' :          t2(('5',)),
    'Offensive Effect' :   offensiveEffectValues,
    'Reactive Effect' :    reactiveEffectValues,
    'Charged Effect' :     chargedEffectValues,
})


CraftedTypeList = t2((
    'Unused', 
    'Focus', 
    'Skill',
    'Cap Increase', 
    'PvE Bonus', 
    'Other Bonus',
    'Offensive Effect',
    'Reactive Effect',
    'Charged Effect',
))


CraftedLists = {
  'All' : d2({
    'Unused' : 
        unusedList,
    'Focus' : t2((
        'All Magic Skills',
    )),
    'Skill' : t2((
        'All Archery Skills',
        'All Dual Wield Skills',
        'All Magic Skills',
        'All Melee Weapon Skills',
    )),
    'Cap Increase' : t2((
        'Strength',
        'Constitution',
        'Dexterity',
        'Quickness',
        'Acuity',
        'Hits',
    )),
    'Other Bonus' : t2((
        '% Power Pool',
        'AF',
        'Archery Damage',
        'Melee Damage',
        'Spell Damage',
        'Healing Effectiveness',
        'Stat Buff Effectiveness',
    )),
    'PvE Bonus' : t2((
        'Defensive',
    )),
    'Charged Effect' :   stableEffectList,
    'Reactive Effect' :  procEffectList,
    'Offensive Effect' : procEffectList,
  }),
}
for realm in Realms:
    CraftedLists[realm] = CraftedLists['All'] 
CraftedLists = d2(CraftedLists)


Caps = dict.fromkeys(resistList, 'Resist')
Caps.update(Caps.fromkeys(statList, 'Stat'))
Caps = d2(Caps)


# Bonuses are given as % of level + add constant
# e.g. [ .25,  1] is the level / 4 + 1
#      [   0, 10] is a fixed 10
#      [   4,  0] is the level * 4
#
HighCapBonusList = d2({
    'Death Experience Loss Reduction' : ( 1.00,  0 ),
    'Hits'                      : ( 4.00,  0 ),
    'Hits Cap'                  : ( 4.00,  0 ),
    'Stat'                      : ( 1.50,  0 ),
    'Focus'                     : ( 1.00,  0 ),
    'Power Cap'                 : ( 1.00,  0 ),
    'AF Cap'                    : ( 1.00,  0 ),
    'AF'                        : ( 1.00,  0 ),
    'Arrow Recovery'            : ( 1.00,  0 ), 
    'Resist'                    : (  .50,  1 ),
    'Power'                     : (  .50,  1 ),
    'Cap'                       : (  .50,  1 ),
    '% Power Pool'              : (  .50,  0 ),
    'Stat Buff Effectiveness'   : (  .50,  0 ),
    'Stat Debuff Effectiveness' : (  .50,  0 ),
    'Healing Effectiveness'     : (  .50,  0 ),
    'Duration of Spells'        : (  .50,  0 ),
    'Fatigue'                   : (  .50,  0 ),
    'Skill'                     : (  .20,  1 ),
    'PvE Bonus'                 : (  .20,  0 ),
    'Other Bonus'               : (  .20,  0 ),
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

GemSubName = d2({ 
    'Stat' :   'Essence Jewel', 
    'Resist' : 'Shielding Jewel', 
    'Hits' :   'Essence Jewel', 
    'Power' :  'Essence Jewel', 
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
        'Blighted Rune' :                 100,
        'Valiant Primal Rune' :           104,
        'Blighted Primal Rune' :          106,
        'Unholy Primal Rune' :            108,
        'Brilliant Rune' :                110,
        'Finesse War Rune' :              112,
        'Finesse Primal Rune' :           114,
    }),
})

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

OCStartPercentages = (0, 10, 20, 30, 50, 70)

EstimatedMakes = (1, 100/(5*49/3 + 2), 100/(4*49/3 + 2),
             100/51, 100/(2*49/3 + 2), 100/(1*49/3 + 2) - 1, 50)

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
    'Mythical',
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


# Rename old skills to new skills, from previously saved template files
#
FixEffectsTable = d2({
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
})

if __name__ == "__main__":
    pass
    #import gnosis.xml.pickle
    #constants = {}
    #for v in __all__:
    #    constants[v] = locals()[v]
    #print gnosis.xml.pickle.dumps(constants)
