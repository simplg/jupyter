import regex as re
def almost(mot: str, s: str) -> list:
    words = ["".join([mot[j] if j != i else mot[j]+"?" for j in range(len(mot))]) for i in range(len(mot))]
    searchRegex = re.compile(r'\b('+ r"|".join(words) + r')\b', flags=re.IGNORECASE)
    return searchRegex.findall(" "+s, overlapped=True)

# print(almost("Jaune", "Ma voiture jaune est pas toute jeune mais je l'ai acheté en June et je l'appelle jarune iaune"))

def pluslarge(mot: str, s: str) -> list:

    words = ["".join([mot[j] if j != i else mot[j]+"?.{0,1}" for j in range(len(mot))]) for i in range(len(mot))]
    searchRegex = re.compile(r'\b('+ r"|".join(words) + r'|[a-z]' + mot + r')\b', flags=re.IGNORECASE)
    return searchRegex.findall(" "+s, overlapped=True)

# print(pluslarge("Jaune", "Ma voiture jaune est pas toute jeune mais je l'ai acheté en June et je l'appelle jarune iaune"))

def score(p: str, s: str) -> int:
    words = p.split(' ')
    score: int = 0
    for word in words:
        if word.isalnum():
            matches = pluslarge(word, s)
            print(matches)
            for m in matches:
                if m == word:
                    score += 5
                else:
                    score += 1
    return score

# print(score("Ma voiture préféré est en jaune !", "Ma voiture jaune est pas toute jeune mais je l'ai acheté en June et je l'appelle jarune iaune"))

def score2(p: str, s: str) -> int:
    words = p.split(' ')
    score: int = 0
    lastword = ''
    i = 0
    for word in words:
        if word.isalnum():
            matches = pluslarge(word, s)
            for m in matches:
                if m.lower() == word.lower():
                    score += 5
                    if lastword != '':
                        occurences = len(re.findall(lastword + ' ' + m, s, flags=re.IGNORECASE))
                        if occurences > 0:
                            score += 20 * occurences
                    lastword = word
                else:
                    score += 1
        i += 1
    return score

# print(score2("Ma voiture préféré est en jaune !", "Ma voiture jaune est pas toute jeune mais je l'ai acheté en June et je l'appelle jarune iaune"))
print(pluslarge('trois', 'Les etrois tris, lys trois gros, les troisx roi.'))