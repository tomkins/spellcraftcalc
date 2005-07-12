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

ScVersion = "Kort 1.42b + Ehrayn/patch 1.0.4"

ClassList = { 
    'Albion' : [
        'Armsman', 'Cabalist', 'Cleric', 'Friar', 'Heretic', 'Infiltrator', 
        'Mercenary', 'Minstrel', 'Necromancer', 'Paladin', 'Reaver', 'Scout', 
        'Sorcerer', 'Theurgist', 'Wizard' ],
    'Hibernia' : [
        'Animist', 'Bainshee', 'Bard', 'Blademaster', 'Champion', 'Druid', 
        'Eldritch', 'Enchanter', 'Hero', 'Mentalist', 'Nightshade', 'Ranger', 
        'Valewalker', 'Vampiir', 'Warden' ],
    'Midgard' : [
        'Berserker', 'Bonedancer', 'Healer', 'Hunter',
        'Runemaster', 'Savage', 'Shadowblade', 'Shaman', 'Skald', 
        'Spiritmaster', 'Thane', 'Valkyrie', 'Warlock', 'Warrior' ] }

TabList = [
    'Chest', 'Arms', 'Head', 'Legs', 'Hands', 'Feet', 'Right Hand',
    'Left Hand', '2 Handed', 'Ranged', 'Spare', 'Neck', 'Cloak', 'Jewel',
    'Belt', 'Left Ring', 'Right Ring', 'Left Wrist', 'Right Wrist']

TypeList = ['Unused', 'Stat', 'Resist', 'Hits', 'Power', 'Focus', 'Skill']

DropTypeList = [
    'Unused', 'Stat', 'Resist', 'Hits', 'Power', 'Focus', 'Skill',
    'Cap Increase', 'PvE Bonus', 'Other Bonus']

StatList = [ 
    ['Strength', 'Fiery'], 
    ['Constitution', 'Earthen'], 
    ['Dexterity', 'Vapor'], 
    ['Quickness', 'Airy'], 
    ['Intelligence', 'Dusty'], 
    ['Piety', 'Watery'], 
    ['Charisma', 'Icy'] , 
    ['Empathy', 'Heated'] ]

DropStatList = [ 
    ['Strength', 'Fiery'], 
    ['Constitution', 'Earthen'], 
    ['Dexterity', 'Vapor'], 
    ['Quickness', 'Airy'], 
    ['Intelligence', 'Dusty'], 
    ['Piety', 'Watery'], 
    ['Charisma', 'Icy'] , 
    ['Empathy', 'Heated'],
    ['Acuity', '' ] ]

AllBonusList = { 
    'Armsman' : {
        'All Focus Bonus' : [], 
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Crush', 'Slash', 'Thrust', 'Polearm', 'Two Handed'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry'],
        'Acuity' : [] },
    'Cabalist' : {
        'All Focus Bonus' : ['Body Focus', 'Matter Focus', 'Spirit Focus'], 
        'All Magic Skill Bonus' : ['Body Magic', 'Matter Magic', 'Spirit Magic'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Intelligence'] },
    'Cleric' : {
        'All Focus Bonus' : [], 
        'All Magic Skill Bonus' : ['Rejuvenation', 'Enhancement', 'Smite'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Piety'] },
    'Friar' : {
        'All Focus Bonus' : [], 
        'All Magic Skill Bonus' : ['Rejuvenation', 'Enhancement'],
        'All Melee Skill Bonus' : ['Staff'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry'],
        'Acuity' : ['Piety'] },
    'Heretic' : {
        'All Focus Bonus' : [], 
        'All Magic Skill Bonus' : ['Rejuvenation', 'Enhancement'],
        'All Melee Skill Bonus' : ['Crush', 'Flexible'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Shield'],
        'Acuity' : ['Piety'] },
    'Infiltrator' : {
        'All Focus Bonus' : [], 
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Slash', 'Thrust'],
        'All Dual Wield Skill Bonus' : ['Dual Wield'],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Critical Strike', 'Envenom', 'Stealth'],
        'Acuity' : [] },
    'Mercenary' : {
        'All Focus Bonus' : [], 
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Crush', 'Slash', 'Thrust'],
        'All Dual Wield Skill Bonus' : ['Dual Wield'],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry', 'Shield'],
        'Acuity' : [] },
    'Minstrel' : {
        'All Focus Bonus' : [], 
        'All Magic Skill Bonus' : ['Instruments'],
        'All Melee Skill Bonus' : ['Slash', 'Thrust'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Stealth'],
        'Acuity' : ['Charisma'] },
    'Necromancer' : {
        'All Focus Bonus' : ['Deathsight Focus', 'Death Servant Focus', 
        'Painworking Focus'], 
        'All Magic Skill Bonus' : ['Deathsight', 'Death Servant', 'Painworking'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Intelligence'] },
    'Paladin' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Crush', 'Slash', 'Thrust', 'Two Handed'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry', 'Shield'],
        'Acuity' : [] },
    'Reaver' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Soulrending'],
        'All Melee Skill Bonus' : ['Crush', 'Slash', 'Thrust', 'Flexible'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry', 'Shield'],
        'Acuity' : [] },
    'Scout' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Slash', 'Thrust'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : ['Longbow'],
        'Other Skill Bonus' : ['Stealth', 'Shield'],
        'Acuity' : [] },
    'Sorcerer' : {
        'All Focus Bonus' : ['Body Focus', 'Mind Focus', 'Matter Focus'],
        'All Magic Skill Bonus' : ['Body Magic', 'Mind Magic', 'Matter Magic'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Intelligence'] },
    'Theurgist' : {
        'All Focus Bonus' : ['Earth Focus', 'Cold Focus', 'Wind Focus'],
        'All Magic Skill Bonus' : ['Earth Magic', 'Cold Magic', 'Wind Magic'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Intelligence'] },
    'Wizard' : {
        'All Focus Bonus' : ['Earth Focus', 'Cold Focus', 'Fire Focus'],
        'All Magic Skill Bonus' : ['Earth Magic', 'Cold Magic', 'Fire Magic'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Intelligence'] },
    'Animist' : {
        'All Focus Bonus' : ['Creeping Path Focus', 'Arboreal Focus', 'Verdant Path Focus'],
        'All Magic Skill Bonus' : ['Arboreal Path', 'Creeping Path', 'Verdant Path'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Intelligence'] },
    'Bainshee' : {
        'All Focus Bonus' : ['Ethereal Shriek Focus', 'Phantasmal Wail Focus', 'Spectral Guard Focus'],
        'All Magic Skill Bonus' : ['Ethereal Shriek', 'Phantasmal Wail', 'Spectral Guard'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Intelligence'] },
    'Bard' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Regrowth', 'Nurture', 'Music'],
        'All Melee Skill Bonus' : ['Blades', 'Blunt'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Charisma'] },
    'Blademaster' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Blades', 'Blunt', 'Piercing'],
        'All Dual Wield Skill Bonus' : ['Celtic Dual'],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry', 'Shield'],
        'Acuity' : [] },
    'Champion' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Valor'],
        'All Melee Skill Bonus' : ['Blades', 'Blunt', 'Piercing', 'Large Weaponry'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry', 'Shield'],
        'Acuity' : ['Intelligence'] },
    'Druid' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Regrowth', 'Nature', 'Nurture'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Empathy'] },
    'Eldritch' : {
        'All Focus Bonus' : ['Light Focus', 'Mana Focus', 'Void Focus'],
        'All Magic Skill Bonus' : ['Light', 'Mana', 'Void'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Intelligence'] },
    'Enchanter' : {
        'All Focus Bonus' : ['Light Focus', 'Mana Focus', 'Enchantments Focus'],
        'All Magic Skill Bonus' : ['Light', 'Mana', 'Enchantments'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Intelligence'] },
    'Mentalist' : {
        'All Focus Bonus' : ['Light Focus', 'Mana Focus', 'Mentalism Focus'],
        'All Magic Skill Bonus' : ['Light', 'Mana', 'Mentalism'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Intelligence'] },
    'Hero' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Blades', 'Blunt', 'Celtic Spear', 'Large Weaponry', 'Piercing'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry', 'Shield'],
        'Acuity' : [] },
    'Nightshade' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Blades', 'Piercing'],
        'All Dual Wield Skill Bonus' : ['Celtic Dual'],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Critical Strike', 'Envenom', 'Stealth'],
        'Acuity' : [] },
    'Ranger' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Pathfinding'],
        'All Melee Skill Bonus' : ['Blades', 'Piercing'],
        'All Dual Wield Skill Bonus' : ['Celtic Dual'],
        'Archery Skill Bonus' : ['Recurve Bow'],
        'Other Skill Bonus' : ['Stealth'],
        'Acuity' : [] },
    'Valewalker' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Arboreal Path'],
        'All Melee Skill Bonus' : ['Scythe'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry'],
        'Acuity' : ['Intelligence'] },
    'Vampiir' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Dementia', 'Shadow Mastery', 'Vampiiric Embrace'],
        'All Melee Skill Bonus' : ['Piercing'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : [] },
    'Warden' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Nurture', 'Regrowth', 'Nature'],
        'All Melee Skill Bonus' : ['Blades', 'Blunt'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry'],
        'Acuity' : ['Empathy'] },
    'Berserker' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Axe', 'Hammer', 'Sword'],
        'All Dual Wield Skill Bonus' : ['Left Axe'],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry'],
        'Acuity' : [] },
    'Bonedancer' : {
        'All Focus Bonus' : ['Darkness Focus', 'Suppression Focus', 'Bone Army Focus'],
        'All Magic Skill Bonus' : ['Darkness', 'Suppression', 'Bone Army'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Piety'] },
    'Healer' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Augmentation', 'Mending', 'Pacification'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Piety'] },
    'Hunter' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Beastcraft'],
        'All Melee Skill Bonus' : ['Spear', 'Sword'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : ['Composite Bow'],
        'Other Skill Bonus' : ['Stealth'],
        'Acuity' : [] },
    'Runemaster' : {
        'All Focus Bonus' : ['Darkness Focus', 'Suppression Focus', 'Runecarving Focus'],
        'All Magic Skill Bonus' : ['Darkness', 'Suppression', 'Runecarving'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Piety'] },
    'Savage' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Savagery'],
        'All Melee Skill Bonus' : ['Sword', 'Axe', 'Hammer', 'Hand To Hand'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry'],
        'Acuity' : [] },
    'Shadowblade' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Sword', 'Axe'],
        'All Dual Wield Skill Bonus' : ['Left Axe'],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Critical Strike', 'Envenom', 'Stealth'],
        'Acuity' : [] },
    'Shaman' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Augmentation', 'Mending', 'Subterranean'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Piety'] },
    'Skald' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Battlesongs'],
        'All Melee Skill Bonus' : ['Sword', 'Hammer', 'Axe'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry'],
        'Acuity' : ['Charisma'] },
    'Spiritmaster' : {
        'All Focus Bonus' : ['Darkness Focus', 'Suppression Focus', 'Summoning Focus'],
        'All Magic Skill Bonus' : ['Darkness', 'Suppression', 'Summoning'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Piety'] },
    'Thane' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Stormcalling'],
        'All Melee Skill Bonus' : ['Sword', 'Hammer', 'Axe'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry', 'Shield'],
        'Acuity' : ['Piety'] },
    'Valkyrie' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : ['Odin\'s Will'],
        'All Melee Skill Bonus' : ['Spear', 'Sword'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry'],
        'Acuity' : ['Piety'] },
    'Warlock' : {
        'All Focus Bonus' : ['Cursing'],
        'All Magic Skill Bonus' : ['Cursing', 'Hexing', 'Witchcraft'],
        'All Melee Skill Bonus' : [],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : [],
        'Acuity' : ['Piety'] },
    'Warrior' : {
        'All Focus Bonus' : [],
        'All Magic Skill Bonus' : [],
        'All Melee Skill Bonus' : ['Sword', 'Hammer', 'Axe'],
        'All Dual Wield Skill Bonus' : [],
        'Archery Skill Bonus' : [],
        'Other Skill Bonus' : ['Parry', 'Shield', 'Thrown Weapons'],
        'Acuity' : [] } }

for chcl in AllBonusList:
    list = {}
    for skill in AllBonusList[chcl]['All Magic Skill Bonus']: list[skill] = ''
    for skill in AllBonusList[chcl]['All Melee Skill Bonus']: list[skill] = ''
    for skill in AllBonusList[chcl]['All Dual Wield Skill Bonus']: list[skill] = ''
    for skill in AllBonusList[chcl]['Archery Skill Bonus']: list[skill] = ''
    for skill in AllBonusList[chcl]['Other Skill Bonus']: list[skill] = ''
    AllBonusList[chcl]['All Skills'] = list


OtherBonusList = [
    [ 'Power Percentage Bonus', ''],
    [ 'Debuff Bonus',           ''],
    [ 'Buff Bonus',             ''],
    [ 'Healing Bonus',          ''],
    [ 'Spell Duration Bonus',   ''],
    [ 'Casting Speed Bonus',    ''],
    [ 'Spell Range Bonus',      ''],
    [ 'Spell Damage Bonus',     ''],
    [ 'Archery Damage Bonus',   ''],
    [ 'Archery Range Bonus',    ''],
    [ 'Archery Speed Bonus',    ''],
    [ 'Style Damage Bonus',     ''],
    [ 'Melee Damage Bonus',     ''],
    [ 'Melee Speed Bonus',      ''],
    [ 'AF Bonus',               ''],
    [ 'Fatigue',                ''] ]

PvEBonusList = [
    [ 'Concentration', '' ], 
    [ 'Blocking', ''], 
    [ 'Evade', '' ], 
    [ 'Parry', '' ], 
    [ 'Negative Effect Duration Reduction', ''], 
    [ 'Bladeturn Reinforcement', ''], 
    [ 'Piece Ablative', ''], 
    [ 'Damage Reduction', ''], 
    [ 'Reactionary Style Damage Bonus', ''], 
    [ 'To-Hit Bonus', ''], 
    [ 'Spell Power Cost Reduction', ''], 
    [ 'Style Cost Reduction', ''], 
    [ 'Death Experience Loss Reduction', ''], 
    [ 'Arrow Recovery', ''] ]

CapIncreaseList = [ 
    ['Strength',     ''], 
    ['Constitution', ''], 
    ['Dexterity',    ''], 
    ['Quickness',    ''], 
    ['Intelligence', ''], 
    ['Piety',        ''], 
    ['Charisma',     ''] , 
    ['Empathy',      ''],
    ['Hits',         ''], 
    ['Power',        ''], 
    ['Acuity',       ''], 
    ['AF',           ''] ]

StatValues = ['1', '4', '7', '10', '13', '16', '19', '22', '25', '28']

QualityValues = ['94', '95', '96', '97', '98', '99', '100']

ResistList = [ 
    ['Body Resist',   'Dusty'], 
    ['Cold Resist',   'Icy'], 
    ['Heat Resist',   'Heated'], 
    ['Energy Resist', 'Light'],
    ['Matter Resist', 'Earthen'], 
    ['Spirit Resist', 'Vapor'],
    ['Crush Resist',  'Fiery'], 
    ['Thrust Resist', 'Airy'], 
    ['Slash Resist',  'Watery'] ]

ResistValues = ['1', '2', '3', '5', '7', '9', '11', '13', '15', '17']

HitsList = [ ['Hits', 'Blood'] ]

HitsValues = ['4', '12', '20', '28', '36', '44', '52', '60', '68', '76']

PowerList = [ ['Power', 'Mystical'] ]

PowerValues = ['1', '2', '3', '5', '7', '9', '11', '13', '15', '17']

FocusList = { 
    'Albion' : [
        ['Body Focus',            'Heat Sigil'], 
        ['Cold Focus',            'Ice Sigil'], 
        ['Death Servant Focus',   'Ashen Sigil'],
        ['Deathsight Focus',      'Vacuous Sigil'],
        ['Earth Focus',           'Earth Sigil'],
        ['Fire Focus',            'Fire Sigil'],
        ['Matter Focus',          'Dust Sigil'],
        ['Mind Focus',            'Water Sigil'],
        ['Painworking Focus',     'Salt Crusted Sigil'],
        ['Spirit Focus',          'Vapor Sigil'],
        ['Wind Focus',            'Air Sigil'],
        ['All Focus Bonus',       'Brilliant Sigil'] ],

    'Hibernia' : [
        ['Arboreal Focus',        'Steaming Spell Stone'] , 
        ['Creeping Path Focus',   'Oozing Spell Stone'],
        ['Enchantments Focus',    'Vapor Spell Stone'], 
        ['Ethereal Shriek Focus', 'Ethereal Spell Stone'], 
        ['Light Focus',           'Fire Spell Stone'], 
        ['Mana Focus',            'Water Spell Stone'], 
        ['Mentalism Focus',       'Earth Spell Stone'], 
        ['Phantasmal Wail Focus', 'Phantasmal Spell Stone'], 
        ['Spectral Guard Focus',  'Spectral Spell Stone'], 
        ['Verdant Path Focus',    'Mineral Encrusted Spell Stone'],
        ['Void Focus',            'Ice Spell Stone'],
        ['All Focus Bonus',       'Brilliant Spell Stone'] ],

    'Midgard' : [ 
        ['Bone Army Focus',       'Ashen Rune'], 
        ['Cursing Focus',         'Blighted Rune'],
        ['Darkness Focus',        'Ice Rune'],
        ['Runecarving Focus',     'Heat Rune'],
        ['Summoning Focus',       'Vapor Rune'], 
        ['Suppression Focus',     'Dust Rune'],
        ['All Focus Bonus',       'Brilliant Rune'] ] }

DropFocusList =  FocusList

FocusValues = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50']

SkillList = { 
    'Midgard' : 
    [ ['Augmentation', 'Airy Chaos Rune'],
    ['Axe', 'Earthen War Rune'], 
    ['Battlesongs', 'Airy Primal Rune'],
    ['BeastCraft', 'Earthen Primal Rune'],
    ['Bone Army', 'Ashen Primal Rune'],
    ['Composite Bow', 'Airy War Rune'],
    ['Critical Strike', 'Heated Battle Jewel'],
    ['Cursing', 'Blighted Primal Rune'], 
    ['Darkness', 'Icy Chaos Rune'],
    ['Envenom', 'Dusty Battle Jewel'],
    ['Hammer', 'Fiery War Rune'],
    ['Hand To Hand', 'Lightning Charged War Rune'],
    ['Hexing', 'Unholy Primal Rune'], 
    ['Left Axe', 'Icy War Rune'],
    ['Mending', 'Watery Chaos Rune'],
    ["Odin's Will", 'Valiant Primal Rune'], 
    ['Pacification', 'Earthen Chaos Rune'],
    ['Parry', 'Vapor Battle Jewel'],
    ['Runecarving', 'Heated Chaos Rune'],
    ['Shield', 'Fiery Battle Jewel'],
    ['Spear', 'Heated War Rune'],
    ['Staff', 'Earthen Battle Jewel'],
    ['Stealth', 'Airy Battle Jewel'],
    ['Stormcalling', 'Fiery Primal Rune'],
    ['Subterranean', 'Fiery Chaos Rune'],
    ['Summoning', 'Vapor Chaos Rune'],
    ['Suppression', 'Dusty Chaos Rune'],
    ['Sword', 'Watery War Rune'],
    ['Thrown Weapons', 'Vapor War Rune'],
    ['All Magic Skill Bonus', 'Finesse Primal Rune'],
    ['All Melee Skill Bonus', 'Finesse War Rune'] ],

    'Albion' : [
    ['Body Magic', 'Heated Evocation Sigil' ],
    ['Chants', 'Earthen Fervor Sigil' ],
    ['Cold Magic', 'Icy Evocation Sigil' ],
    ['Critical Strike','Heated Battle Jewel' ],
    ['Crossbow', 'Vapor War Sigil' ],
    ['Crush', 'Fiery War Sigil' ],
    ['Death Servant', 'Ashen Fervor Sigil' ],
    ['Deathsight', 'Vacuous Fervor Sigil' ],
    ['Dual Wield', 'Icy War Sigil' ],
    ['Earth Magic', 'Earthen Evocation Sigil' ],
    ['Enhancement', 'Airy Fervor Sigil' ],
    ['Envenom', 'Dusty Battle Jewel' ],
    ['Flexible', 'Molten Magma War Sigil' ],
    ['Fire Magic','Fiery Evocation Sigil' ],
    ['Instruments', 'Vapor Fervor Sigil' ],
    ['Longbow', 'Airy War Sigil' ],
    ['Matter Magic', 'Dusty Evocation Sigil' ],
    ['Mind Magic', 'Watery Evocation Sigil' ],
    ['Painworking','Salt Crusted Fervor Sigil' ],
    ['Parry', 'Vapor Battle Jewel' ],
    ['Polearm', 'Earthen War Sigil' ],
    ['Rejuvenation', 'Watery Fervor Sigil' ],
    ['Shield', 'Fiery Battle Jewel' ],
    ['Slash', 'Watery War Sigil' ],
    ['Smite','Fiery Fervor Sigil' ],
    ['Soulrending', 'Steaming Fervor Sigil' ],
    ['Spirit Magic', 'Vapor Evocation Sigil' ],
    ['Staff', 'Earthen Battle Jewel' ],
    ['Stealth', 'Airy Battle Jewel' ],
    ['Thrust','Dusty War Sigil' ],
    ['Two Handed', 'Heated War Sigil' ],
    ['Wind Magic', 'Air Evocation Sigil'],
    ['All Magic Skill Bonus', 'Finesse Fervor Sigil'],
    ['All Melee Skill Bonus', 'Finesse War Sigil'] ], 

    'Hibernia' : 
    [ ['Arboreal Path', 'Steaming Nature Spell Stone'], 
    ['Blades', 'Watery War Spell Stone'], 
    ['Blunt', 'Fiery War Spell Stone'],
    ['Celtic Dual', 'Icy War Spell Stone'],
    ['Celtic Spear', 'Earthen War Spell Stone'],
    ['Creeping Path', 'Oozing Nature Spell Stone'],
    ['Critical Strike', 'Heated Battle Jewel'],
    ['Dementia', 'Aberrant Arcane Spell Stone'], 
    ['Enchantments', 'Vapor Arcane Spell Stone'],
    ['Envenom', 'Dusty Battle Jewel'],
    ['Ethereal Shriek', 'Ethereal Arcane Spell Stone'], 
    ['Large Weaponry', 'Heated War Spell Stone'],
    ['Light', 'Fiery Arcane Spell Stone'], 
    ['Mana', 'Watery Arcane Spell Stone'],
    ['Mentalism', 'Earthen Arcane Spell Stone'],
    ['Music', 'Airy Nature Spell Stone'],
    ['Nature', 'Earthen Nature Spell Stone'],
    ['Nurture', 'Fiery Nature Spell Stone'],
    ['Parry', 'Vapor Battle Jewel'],
    ['Phantasmal Wail', 'Phantasmal Arcane Spell Stone'], 
    ['Piercing', 'Dusty War Spell Stone'],
    ['Recurve Bow', 'Airy War Spell Stone'],
    ['Regrowth', 'Watery Nature Spell Stone'],
    ['Scythe', 'Light War Spell Stone'],
    ['Shadow Mastery', 'Shadowy Arcane Spell Stone'], 
    ['Shield', 'Fiery Battle Jewel'],
    ['Spectral Guard', 'Spectral Arcane Spell Stone'], 
    ['Staff', 'Earthen Battle Jewel'],
    ['Stealth', 'Airy Battle Jewel'],
    ['Valor', 'Airy Arcane Spell Stone'],
    ['Vampiiric Embrace', 'Embracing Arcane Spell Stone'], 
    ['Verdant Path', 'Mineral Encrusted Nature Spell Stone'],
    ['Void', 'Icy Arcane Spell Stone'],
    ['All Magic Skill Bonus', 'Finesse Nature Spell Stone'],
    ['All Melee Skill Bonus', 'Finesse War Spell Stone'] ] }

DropSkillList = { 
    'Midgard' : 
    [ ['Augmentation', 'Airy Chaos Rune'],
    ['Axe', 'Earthen War Rune'], 
    ['Battlesongs', 'Airy Primal Rune'],
    ['BeastCraft', 'Earthen Primal Rune'],
    ['Bone Army', 'Ashen Chaos Rune'],
    ['Composite Bow', 'Airy War Rune'],
    ['Critical Strike', 'Heated Battle Jewel'],
    ['Cursing', 'Blighted Primal Rune'], 
    ['Darkness', 'Icy Chaos Rune'],
    ['Envenom', 'Dusty Battle Jewel'],
    ['Hammer', 'Fiery War Rune'],
    ['Hand To Hand', 'Lightning Charged War Rune'],
    ['Hexing', 'Unholy Primal Rune'], 
    ['Left Axe', 'Icy War Rune'],
    ['Mending', 'Watery Chaos Rune'],
    ['Odin\'s Will', 'Valiant Primal Rune'], 
    ['Pacification', 'Earthen Chaos Rune'],
    ['Parry', 'Vapor Battle Jewel'],
    ['Runecarving', 'Heated Chaos Rune'],
    ['Shield', 'Fiery Battle Jewel'],
    ['Spear', 'Heated War Rune'],
    ['Staff', 'Earthen Battle Jewel'],
    ['Stealth', 'Airy Battle Jewel'],
    ['Stormcalling', 'Fiery Primal Rune'],
    ['Subterranean', 'Fiery Chaos Rune'],
    ['Summoning', 'Vapor Chaos Rune'],
    ['Suppression', 'Dusty Chaos Rune'],
    ['Sword', 'Watery War Rune'],
    ['Thrown Weapons', 'Vapor War Rune'],
    ['All Magic Skill Bonus', 'Finesse Primal Rune'],
    ['All Melee Skill Bonus', 'Finesse War Rune'],
    ['All Dual Wield Skill Bonus', ''],
    ['Archery Skill Bonus', ''] ],

    'Albion' : [
    ['Body Magic', 'Heated Evocation Sigil' ],
    ['Chants', 'Earthen Fervor Sigil' ],
    ['Cold Magic', 'Icy Evocation Sigil' ],
    ['Critical Strike','Heated Battle Jewel' ],
    ['Crossbow', 'Vapor War Sigil' ],
    ['Crush', 'Fiery War Sigil' ],
    ['Cursing', 'Blighted Primal Rune'], 
    ['Death Servant', 'Ashen Fervor Sigil' ],
    ['Deathsight', 'Vacuous Fervor Sigil' ],
    ['Dual Wield', 'Icy War Sigil' ],
    ['Earth Magic', 'Earthen Evocation Sigil' ],
    ['Enhancement', 'Airy Fervor Sigil' ],
    ['Envenom', 'Dusty Battle Jewel' ],
    ['Flexible', 'Molten Magma War Sigil' ],
    ['Fire Magic','Fiery Evocation Sigil' ],
    ['Hexing', 'Unholy Primal Rune'], 
    ['Instruments', 'Vapor Fervor Sigil' ],
    ['Longbow', 'Airy War Sigil' ],
    ['Matter Magic', 'Dusty Evocation Sigil' ],
    ['Mind Magic', 'Watery Evocation Sigil' ],
    ['Odin\'s Will', 'Valiant Primal Rune'], 
    ['Painworking','Salt Crusted Fervor Sigil' ],
    ['Parry', 'Vapor Battle Jewel' ],
    ['Polearm', 'Earthen War Sigil' ],
    ['Rejuvenation', 'Watery Fervor Sigil' ],
    ['Shield', 'Fiery Battle Jewel' ],
    ['Slash', 'Watery War Sigil' ],
    ['Smite','Fiery Fervor Sigil' ],
    ['Soulrending', 'Steaming Fervor Sigil' ],
    ['Spirit Magic', 'Vapor Evocation Sigil' ],
    ['Staff', 'Earthen Battle Jewel' ],
    ['Stealth', 'Airy Battle Jewel' ],
    ['Thrust','Dusty War Sigil' ],
    ['Two Handed', 'Heated War Sigil' ],
    ['Wind Magic', 'Air Evocation Sigil'],
    ['All Magic Skill Bonus', 'Finesse Fervor Sigil'],
    ['All Melee Skill Bonus', 'Finesse War Sigil'],
    ['All Dual Wield Skill Bonus', ''],
    ['Archery Skill Bonus', ''] ],

    'Hibernia' : 
    [ ['Arboreal Path', 'Steaming Nature Spell Stone'], 
    ['Blades', 'Watery War Spell Stone'], 
    ['Blunt', 'Fiery War Spell Stone'],
    ['Celtic Dual', 'Icy War Spell Stone'],
    ['Celtic Spear', 'Earthen War Spell Stone'],
    ['Creeping Path', 'Oozing Nature Spell Stone'],
    ['Critical Strike', 'Heated Battle Jewel'],
    ['Dementia', 'Aberrant Arcane Spell Stone'], 
    ['Enchantments', 'Vapor Arcane Spell Stone'],
    ['Envenom', 'Dusty Battle Jewel'],
    ['Ethereal Shriek', 'Ethereal Arcane Spell Stone'], 
    ['Large Weaponry', 'Heated War Spell Stone'],
    ['Light', 'Fiery Arcane Spell Stone'], 
    ['Mana', 'Watery Arcane Spell Stone'],
    ['Mentalism', 'Earthen Arcane Spell Stone'],
    ['Music', 'Airy Nature Spell Stone'],
    ['Nature', 'Earthen Nature Spell Stone'],
    ['Nurture', 'Fiery Nature Spell Stone'],
    ['Parry', 'Vapor Battle Jewel'],
    ['Phantasmal Wail', 'Phantasmal Arcane Spell Stone'], 
    ['Piercing', 'Dusty War Spell Stone'],
    ['Recurve Bow', 'Airy War Spell Stone'],
    ['Regrowth', 'Watery Nature Spell Stone'],
    ['Scythe', 'Light War Spell Stone'],
    ['Shadow Mastery', 'Shadowy Arcane Spell Stone'], 
    ['Shield', 'Fiery Battle Jewel'],
    ['Spectral Guard', 'Spectral Arcane Spell Stone'], 
    ['Staff', 'Earthen Battle Jewel'],
    ['Stealth', 'Airy Battle Jewel'],
    ['Valor', 'Airy Arcane Spell Stone'],
    ['Vampiiric Embrace', 'Embracing Arcane Spell Stone'], 
    ['Verdant Path', 'Mineral Encrusted Nature Spell Stone'],
    ['Void', 'Icy Arcane Spell Stone'],
    ['All Magic Skill Bonus', 'Finesse Nature Spell Stone'],
    ['All Melee Skill Bonus', 'Finesse War Spell Stone'],
    ['All Dual Wield Skill Bonus', ''],
    ['Archery Skill Bonus', ''] ] }

SkillValues = ['1', '2', '3', '4', '5', '6', '7', '8']

# Placeholder
UnusedList = [ ]

UnusedValues = [ ]

Caps = { 
    'Str' : 'Stat', 
    'Con' : 'Stat', 
    'Dex' : 'Stat', 
    'Qui' : 'Stat', 
    'Int' : 'Stat', 
    'Pie' : 'Stat', 
    'Cha' : 'Stat', 
    'Emp' : 'Stat', 
    'Body' : 'Resist', 
    'Cold' : 'Resist', 
    'Heat' : 'Resist',
    'Energy' : 'Resist', 
    'Matter' : 'Resist', 
    'Spirit' : 'Resist', 
    'Crush' : 'Resist', 
    'Thrust' : 'Resist',
    'Slash' : 'Resist' }

# Bonuses are given as % of level + add
# e.g. [.25, 1] is level / 4 + 1,  [0, 10] is a fixed 10, [1, 0] is level
HighCapBonusList = {
    'Stat'                   : [ 1.50,  0 ],
    'Resist'                 : [  .50,  1 ],
    'Hits'                   : [ 4.00,  0 ],
    'Power'                  : [  .50,  1 ],
    'Skill'                  : [  .20,  1 ],
    'Cap'                    : [  .50,  1 ],
    'Hits Cap'               : [ 4.00,  0 ],
    'Power Cap'              : [ 1.00,  0 ],
    'AF Cap'                 : [ 1.00,  0 ],
    'PvE Bonus'              : [  .20,  0 ],
    'Other Bonus'            : [  .20,  0 ],
    'Power Percentage Bonus' : [  .50,  0 ],
    'Buff Bonus'             : [  .50,  0 ],
    'Debuff Bonus'           : [  .50,  0 ],
    'Healing Bonus'          : [  .50,  0 ],
    'Spell Duration Bonus'   : [  .50,  0 ],
    'Fatigue'                : [  .50,  0 ],
    'AF Bonus'               : [ 1.00,  0 ],
    'Arrow Recovery'         : [ 1.00,  0 ], 
    'Death Experience Loss Reduction' : [ 1.00, 0 ] }


ImbueMultipliers = { 'Stat' : 1.0, 'Resist' : 2.0, 'Skill' : 5.0, 
    'Hits' : 0.25, 'Power' : 2.0, 'Focus' : 1.0, 'Unused' : 0.0 } 

OCStartPercentages = [0, 10, 20, 30, 50, 70]

GemQualOCModifiers = { '' : 0, '94': 0, '95' : 0, '96' : 1, '97' : 3, '98' : 5, 
    '99' : 8, '100' : 11 }

ItemQualOCModifiers = { 
    '94' :  0, '95' :  0, '96'  :  6, '97' :  8, 
    '98' : 10, '99' : 18, '100' : 26 }

GemCosts = [ 160, 920, 3900, 13900, 40100, 88980, 133000, 198920, 258240, 296860 ]

RemakeCosts = [ 120, 560, 1740, 5260, 14180, 30660, 45520, 67680, 87640, 100700 ]

MaterialGems = ['Lo', 'Um', 'On', 'Ee', 'Pal', 'Mon', 'Ros', 'Zo', 'Kath', 'Ra' ]

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
    'Undead Ash and Holy Water' ]

DustsOrder = [
    'Ground Draconic Scales',
    'Essence of Life', 
    'Bloodied Battlefield Dirt',
    'Unseelie Dust', 
    'Fairy Dust', 
    'Other Worldly Dust',
    'Ground Caer Stone', 
    'Ground Blessed Undead Bone',
    'Ground Cave Crystal',
    'Ground Giant Bone', 
    'Ground Vendo Bone', 
    'Soot From Niflheim']

GemLiquids = { 
    'Fiery' :             'Draconic Fire', 
    'Earthen':            'Treant Blood',
    'Vapor' :             'Swamp Fog', 
    'Airy' :              'Air Elemental Essence',
    'Heated' :            'Heat From an Unearthly Pyre', 
    'Icy' :               'Frost From a Wasteland', 
    'Watery' :            'Leviathan Blood',
    'Dusty' :             'Undead Ash and Holy Water',
    'Fire' :              'Draconic Fire', 
    'Earth' :             'Treant Blood',
    'Vapor' :             'Swamp Fog', 
    'Air' :               'Air Elemental Essence',
    'Heat' :              'Heat From an Unearthly Pyre', 
    'Ice' :               'Frost From a Wasteland', 
    'Water' :             'Leviathan Blood',
    'Dust' :              'Undead Ash and Holy Water',
    'Ashen' :             'Undead Ash and Holy Water',
    'Vacuous' :           'Swamp Fog',
    'Salt' :              'Mystic Energy',
    'Steaming Spell' :    'Swamp Fog',
    'Steaming Nature' :   'Swamp Fog',
    'Steaming Fervor' :   'Heat From an Unearthly Pyre',
    'Oozing' :            'Treant Blood',
    'Mineral' :           'Heat From an Unearthly Pyre',
    'Lightning' :         'Leviathan Blood',
    'Molten' :            'Leviathan Blood',
    'Light' :             'Sun Light',
    'Blood' :             'Giant Blood',
    'Mystical' :          'Mystic Energy',
    'Mystic' :            'Mystic Energy', 
    'Brilliant' :       [ 'Draconic Fire', 'Mystic Energy', 'Treant Blood' ],
    'Finesse' :         [ 'Draconic Fire', 'Mystic Energy', 'Treant Blood' ],
    'Ethereal Spell' :    'Swamp Fog', 
    'Phantasmal Spell' :  'Leviathan Blood', 
    'Spectral Spell' :    'Draconic Fire', 
    'Ethereal Arcane' :   'Leviathan Blood', 
    'Phantasmal Arcane' : 'Draconic Fire', 
    'Spectral Arcane' :   'Air Elemental Essence', 
    'Aberrant' :          'Treant Blood', 
    'Embracing' :         'Frost From a Wasteland', 
    'Shadowy' :           'Swamp Fog', 
    'Blighted Primal' :   'Air Elemental Essence', 
    'Blighted Rune' :     'Undead Ash and Holy Water', 
    'Valiant' :           'Swamp Fog', 
    'Unholy' :            'Air Elemental Essence' }

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
    'Arcane Spell Stone' : 'Other Worldly Dust' }

GemNames = [ 
    'raw',      'uncut',   'rough',    'flawed',   'imperfect', 
    'polished', 'faceted', 'precious', 'flawless', 'perfect' ]

GemSubName = { 
    'Stat' : 'Essence', 
    'Resist' : 'Shielding', 
    'Hits' : 'Essence', 
    'Power' : 'Essence', 
    'Focus' : '', 
    'Skill' : '' }

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
    [10,15,18,21,24,28,32] ]

FileExt = { 
    'Neck' : 'neck', 
    'Cloak' : 'cloak', 
    'Belt' : 'belt', 
    'Jewel' : 'jewel',
    'Left Ring' : 'ring', 
    'Right Ring' : 'ring', 
    'Left Wrist' : ['bracer', 'wrist'],
    'Right Wrist' : ['bracer', 'wrist'], 
    'Chest' : 'chest', 'Arms' : 'arms', 
    'Head' : 'helm', 
    'Legs' : 'legs', 
    'Feet' : 'boots', 
    'Hands' : 'hands',
    'Right Hand' : 'wep', 
    'Left Hand' : ['lhwep', 'shield'],
    '2 Handed' : ['2hwep', 'lhwep', 'wep'],
    'Ranged' : 'ranged', 'Spare' : '*' }

ShieldTypes = [
    'Rowan',    'Elm',       'Oaken',    'Ironwood', 'Heartwood', 
    'Runewood', 'Stonewood', 'Ebonwood', 'Dyrwood',  'Duskwood' ]

Races = {
    'Albion' : [
        'Avalonian',
        'Briton',
        'Inconnu',
        'Saracen',
        'Half Ogre',
        'Highlander' ],
    'Hibernia' : [
        'Celt',
        'Elf',
        'Firbolg',
        'Lurikeen',
        'Shar',
        'Sylvan' ],
    'Midgard' : [
        'Dwarf',
        'Frostalf',
        'Kobold',
        'Troll',
        'Norseman',
        'Valkyn' ] }

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
   'Valkyn' :     {'Slash' : 3, 'Thrust' : 2, 'Cold'   : 5, 'Body'   : 5 } }


