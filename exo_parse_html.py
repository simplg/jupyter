import re

tagRegex = re.compile(r'(<[-/\w\d]+>)')
titleRegex = re.compile(r'<[h]{1}[0-9]{1}>(.+?)</[h]{1}[0-9]{1}>', flags=re.IGNORECASE)

def balise2dico(s: str) -> dict[int,str]:
    mondic: dict[int, str] = {}
    for m in tagRegex.finditer(s):
        mondic[m.start()] = m.group(1)
    return mondic

print(balise2dico("<p>Lol <strong>xd</strong></p>"))

def interpreter(s: str) -> str:
    lastPos = 0
    retStr = ""
    for m in titleRegex.finditer(s):
        retStr += s[lastPos:m.start()] + m.group(1).upper()
        lastPos = m.end()
    retStr += s[lastPos:]
    retStr = tagRegex.sub('', retStr)
    return retStr

print(interpreter("<article><h1>Mon titre</h1><p>Moi je suis beau</p><H3>Commentaires :</H3></article>"))

def xml2csv(s: str, sep: str = ";") -> str:
    data: dict[str, list[str]] = {}
    i_data = 0
    tags: list[str] = []
    in_tag = False
    closing_tag = False
    current_tag = ""
    current_data = ""
    for l in s:
        if l == '<':
            in_tag = True
            if current_data != "":
                key = "_".join(tags)
                if key not in data:
                    data[key] = [] if i_data == 0 else ["None" * i_data]
                data[key].append(current_data)
                current_data = ""
        elif l == '>':
            in_tag = False
            closing_tag = False
            if current_tag != "":
                tags.append(current_tag)
                current_tag = ""
        elif in_tag and l == '/':
            tags.pop()
            if len(tags) == 0:
                i_data += 1
            closing_tag = True
        elif in_tag and not closing_tag:
            current_tag += l
        elif not in_tag:
            current_data += l
    return sep.join(data.keys())+"\n"+"\n".join([sep.join([data[k][i] if i < len(data[k]) else "None" for k in data]) for i in range(0, i_data)])

print(xml2csv("<individu><nom><prenom>Yanice</prenom><famille>Guigou</famille></nom><poids>23,5</poids></individu><individu><taille>134.6</taille><poids>34,5</poids><adresse><city>Mandelieu</city></adresse></individu>"))