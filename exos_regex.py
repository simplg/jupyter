import regex as re
from timeit import timeit

regex_euros = re.compile(r'([\d.]+) ?(?:€|euros)')


def hascap_ascii(s):
    words = []
    for i in s.split():
        if (ord(i[0]) > 64 and ord(i[0]) < 91):
            words.append(i)
    return words


def hascap_regex(s):
    m = re.findall(r'[A-Z]\w+', s)
    return m


def inflate(phrase):
    matches = [s for s in re.findall(regex_euros, phrase)]
    matches.sort(reverse=True)
    for s in matches:
        phrase = phrase.replace(s, f'{float(s) * 2:.2f}')
    return phrase


def retour_ligne(txt):
    if len(txt) < 100:
        return txt
    lignes = []
    i = 0
    for s in txt.split():
        if (len(lignes) == 0):
            lignes.append(s)
        elif (len(lignes[i]) + len(s) > 24):
            if (len(lignes[i]) > 0):
                lignes.append(s)
                i += 1
            else:
                lignes[i] += ' ' + s
        else:
            lignes[i] += ' ' + s
    return lignes


def get_numbers(s):
    return re.findall(r'-*[\d.]+', s)


def arrondi_inf(s):
    return re.sub(r'(-*\d+)(\.\d+)?', r'\1', s)


s = 'Ma longue lettre à Brahiman et Julien, elle est magnifique !'
print(hascap_ascii(s))
print(hascap_regex(s))

print(inflate("J'ai gagné 10 euros mais dépensé 20 € !"))

s = "Onze ans déjà que cela passe vite Vous "
s += "vous étiez servis simplement de vos armes la "
s += "mort n‘éblouit pas les yeux des partisans Vous "
s += "aviez vos portraits sur les murs de nos villes "

print(retour_ligne(s))

print(get_numbers('Les 2 maquereaux valent 6.50 euros !'))
print(arrondi_inf('Les 2.9 maquereaux valent 6.50 euros'))
