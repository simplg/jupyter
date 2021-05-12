from simplonutils import score2

class ItemSearch():
    def __init__(self, test='', arg='', expected=0, mess=''):
        self.test = test
        self.arg = arg
        self.expected = expected
        self.mess = mess


def test_search():
    tests = [
        ItemSearch('Fichier', 'Fichier', 5, 'Appeler la fonction avec le même mot dans le texte et la recherche doit renvoyer 5'),
        ItemSearch(test='Fichier', arg='', expected= 0, mess= 'Appeler la fonction avec 0 caractères doit retourner 0'),
        ItemSearch(
            test='Fichier',
            arg= 'Lettre',
            expected= 0,
            mess= 'Appeler une fonction avec une chaine qui ne match pas doit retourner 0'
        ),
        ItemSearch(
            test= 'Mon Fichier',
            arg= 'Fichier',
            expected= 5,
            mess= 'Un seul match dans un fichier texte doit retourner 5'
        ),
        ItemSearch(
            test= 'Mon Fichier',
            arg= 'Mon Fichier',
            expected= 30,
            mess= '2 mots qui matchent à la suite renvoit 30'
        ),
        ItemSearch(
            test= 'Mon Fichier',
            arg= 'mon fichier',
            expected= 30,
            mess= 'La casse ne change pas le résultat du match'
        ),
        ItemSearch(
            test= 'Mon fichier, jamais !',
            arg= 'Mon fichier',
            expected= 30,
            mess= 'La ponctuation ne doit pas changer les résultats'
        ),
        ItemSearch(
            test= '''Mon fichier
            jamais !''',
            arg= 'Mon fichier',
            expected= 30,
            mess= 'Les retours à la ligne ne doivent pas empêcher un mot de matcher'
        ),
        ItemSearch(
            test= 'Mon fichiér',
            arg= 'Mon fichier',
            expected= 6,
            mess= 'Les accents doivent aussi être pris en compte'
        ),
        ItemSearch(
            test='fichiera,',
            arg='fichier',
            expected=1,
            mess='Un mot ayant une lettre en plus doit matcher'
        ),
        ItemSearch(
            test='Japon',
            arg='Savon',
            expected=0,
            mess='Un mot ayant 2 lettres ou plus différentes ne doit pas matcher'
        ),
        ItemSearch(
            test='nfichier',
            arg='fichier',
            expected=1,
            mess='Un mot ayant une lettre en plus doit matcher'
        ),
        ItemSearch(
            test='fchier,',
            arg='fichier',
            expected=1,
            mess='Un mot ayant une lettre en moins doit matcher'
        ),
        ItemSearch(
            test='accées et',
            arg='et',
            expected=5,
            mess='Attention aux boundaries, elles ne prennent pas en compte les accents'
        ),
        ItemSearch(
            test='ont',
            arg='et',
            expected=0,
            mess='Une lettre peut être remplacé ou ajouté, pas les deux'
        ),
        ItemSearch(
            test='ri',
            arg='et',
            expected=0,
            mess='Une lettre peut être remplacé ou ajouté, pas les deux'
        ),
        ItemSearch(
            test="C'est",
            arg='et',
            expected=1,
            mess='Une apostrophe sépare aussi les mots'
        )
    ]
    for t in tests:
        assert score2(t.arg, t.test) == t.expected
