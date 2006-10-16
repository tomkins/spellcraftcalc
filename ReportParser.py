# ReportParser.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

import re
from constants import *
import string
import MyStringIO

class ReportParser:
    def modTabNames(self, cat):
        if cat == '2 Handed': return '2handed'
        if cat == 'Right Hand': return 'rweapon'
        if cat == 'Left Hand' : return 'lweapon'
        if cat == 'Right Ring' : return 'rring'
        if cat == 'Left Ring' : return 'lring'
        if cat == 'Right Wrist' : return 'rwrist'
        if cat == 'Left Wrist' : return 'lwrist'
        return string.lower(cat)

    def parse(self, reporttext, iteminfo):
        totals = iteminfo['Stats']
        items = iteminfo['Items']

        regex = re.compile("<ifnotempty\s+(\w+)>(.*?)(<endifnotempty>|</ifnotempty>)", re.DOTALL|re.IGNORECASE)
        index = 0
        match = regex.search(reporttext[index:])
        while match is not None:
            piece = match.group(1)
            doc = match.group(2)
            piece = string.upper(piece[0])+string.lower(piece[1:])
            if piece == '2handed': piece = '2 Handed'
            if piece == 'Rweapon': piece = 'Right Hand'
            if piece == 'Lweapon': piece = 'Left Hand'
            if piece == 'Rring': piece = 'Right Ring'
            if piece == 'Lring': piece = 'Left Ring'
            if piece == 'Rwrist': piece = 'Right Wrist'
            if piece == 'Lwrist': piece = 'Left Wrist'
            if items.has_key(piece):
                empty = True
                endrng = items[piece].slotCount()
                for slot in range(0, endrng):
                    gemnum = 'gem%d' % (slot+1)
                    if items[piece][gemnum]['type'] != 'Unused':
                        empty = False
                        break
                if not empty:
                    reporttext = re.sub(re.escape(match.string[match.start():match.end()]),
                            doc, reporttext)
                else:
                    reporttext = re.sub(re.escape(match.string[match.start():match.end()]),
                            '', reporttext)
            else:
                reporttext = re.sub(re.escape(match.string[match.start():match.end()]),
                        '', reporttext)
            index = match.end()
            match = regex.search(reporttext[index:])

        regex = re.compile("<if\s+(\w+)\s+(\w+)>(.*?)(<endif>|</if>)", re.DOTALL|re.IGNORECASE)
        index = 0
        match = regex.search(reporttext[index:])
        while match is not None:
            piece = match.group(1)
            type = match.group(2)
            doc = match.group(3)
            piece = string.upper(piece[0])+string.lower(piece[1:])
            if piece == '2handed': piece = '2 Handed'
            if piece == 'Rweapon': piece = 'Right Hand'
            if piece == 'Lweapon': piece = 'Left Hand'
            if piece == 'Rring': piece = 'Right Ring'
            if piece == 'Lring': piece = 'Left Ring'
            if piece == 'Rwrist': piece = 'Right Wrist'
            if piece == 'Lwrist': piece = 'Left Wrist'
            if items.has_key(piece):
                if string.lower(type) == 'pcmade' and items[piece]['activestate'] == 'player':
                    reporttext = re.sub(re.escape(match.string[match.start():match.end()]),
                            doc, reporttext)
                elif string.lower(type) == 'drop' and items[piece]['activestate'] == 'drop':
                    reporttext = re.sub(re.escape(match.string[match.start():match.end()]),
                            doc, reporttext)
                else:
                    reporttext = re.sub(re.escape(match.string[match.start():match.end()]),
                            '', reporttext)
            else:
                reporttext = re.sub(re.escape(match.string[match.start():match.end()]),
                        '', reporttext)
            index = match.end()
            match = regex.search(reporttext[index:])

        intag = 0
        docstr = ''
        docstrings = []
        for i in range(0, len(reporttext)):
            if reporttext[i] == '>':
                intag = 0
                docstr += reporttext[i]
                docstrings.append(docstr)
                docstr = ''
            elif reporttext[i] == '<':
                if docstr != '':
                    docstrings.append(docstr)
                docstr = ''
                intag = 1
                docstr += reporttext[i]
            else:
                docstr += reporttext[i]
        if docstr != '':
            docstrings.append(docstr)
        modtablist = map(self.modTabNames, TabList)
        for i in range(0, len(docstrings)):
            tag = docstrings[i]
            if tag[0] != '<': continue
            tagpieces = string.split(tag, ' ', 1)
            if tagpieces[-1][-1] == '>': 
                if tagpieces[-1][-2:-1] == '/': 
                    tagpieces[-1] = tagpieces[-1][:-2]
                else:
                    tagpieces[-1] = tagpieces[-1][:-1]
            tagname = tagpieces[0][1:]
            if string.lower(tagname) == 'foci':
                focuslist = iteminfo['Focus']
                replstr = ''
                for focus, val in focuslist.items():
                    replstr += '%d %s<br />\n' % (val, focus)
                docstrings[i] = replstr
            elif string.lower(tagname[:5]) == 'focus':
                focusnum = tagname[5:]
                if focusnum != '':
                    focusnum = int(focusnum)
                    focuslist = iteminfo['Focus']
                    if len(focuslist.keys()) >= focusnum:
                        docstrings[i] = '%d %s' % (focuslist[focuslist.keys()[focusnum-1]], 
                            focuslist.keys()[focusnum-1]) 
                    else:
                        docstrings[i] = ''
                else:
                    docstrings[i] = ''
            elif string.lower(tagname) == 'otherbonuses':
                otherlist = iteminfo['Other']
                replstr = ''
                for other, val in otherlist.items():
                    replstr += '%d %s<br />\n' % (val, other)
                docstrings[i] = replstr
            elif string.lower(tagname) == 'capbonuses':
                caplist = iteminfo['Caps']
                replstr = ''
                for cap, val in caplist.items():
                    replstr += '%d %s<br />\n' % (val, cap)
                docstrings[i] = replstr
            elif string.lower(tagname) == 'skills':
                skilllist = iteminfo['Skills']
                replstr = ''
                for skill, val in skilllist.items():
                    replstr += '%d %s<br />\n' % (val, skill)
                docstrings[i] = replstr
            elif string.lower(tagname[:5]) == 'skill':
                skillnum = tagname[5:]
                if skillnum != '':
                    skillnum = int(skillnum)
                    skilllist = iteminfo['Skills']
                    if len(skilllist.keys()) >= skillnum:
                        docstrings[i] = '%d %s' % (skilllist[skilllist.keys()[skillnum-1]], 
                            skilllist.keys()[skillnum-1]) 
                    else:
                        docstrings[i] = ''
                else:
                    docstrings[i] = ''
            elif string.lower(tagname) in totals.keys():
                docstrings[i] = self.matchRegex("<%s\s*(\d+)?\s*/?>" % string.lower(tagname),
                    totals[string.lower(tagname)], docstrings[i])
                
            elif string.lower(tagname) in modtablist:
                cat = string.lower(tagname)
                lst = items[TabList[modtablist.index(cat)]]
                props = string.split(tagpieces[1], ' ', 1)
                prop = props[0] 
                if prop in lst.keys():
                    if prop[:3] != 'gem':
                        docstrings[i] = self.matchRegex("<%s %s\s*(\d+)?\s*/?>" % (cat, prop), 
                            lst[prop], docstrings[i])   
                    else:
                        gemprops = lst[prop]
                        spl = string.split(props[1], ' ', 1)
                        gemprop = spl[0]
                        if not gemprop in gemprops.keys():
                            gemval = ''
                        elif gemprop == 'effect' and gemprops[gemprop] == '':
                            gemval = 'Empty'
                        elif gemprops['effect'] == '':
                            gemval = ''
                        else:
                            gemval = gemprops[gemprop]
                        docstrings[i] = self.matchRegex("<%s %s %s\s*(\d+)?\s*/?>" % (cat, prop, gemprop),
                            gemval, docstrings[i])
                else:
                    docstrings[i] = ''
                
        docstrings = map(lambda x: MyStringIO.unicodeHtmlEscape(x), docstrings)
        return re.sub("\n(\n)+", "\n", reduce(lambda x, y: x+y, docstrings))

    def matchRegex(self, pattern, val, text):
        regex = re.compile(pattern, re.IGNORECASE);
        match = regex.search(text)
        if match is not None:
            valstr = unicode(val)
            if re.search('utility', text) is not None:
                valstr = '%.2f' % val
            width = len(valstr)
            if match.lastindex is not None:
                width = max(int(match.group(match.lastindex)), width)
            formatstr = '%%%ds' % width
            return formatstr % valstr
        return ''
