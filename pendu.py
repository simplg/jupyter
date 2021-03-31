from random import randrange
LISTE_MOTS = [
    "POMMES",
    "ARBRE",
    "ECOLE",
    "INTELLIGENCE",
    "ARTIFICIELLE"
]

MAX_TRIES = 6

print("Salut et bienvenue dans le jeu du pendu !")
print("Vous avez jusqu'à 6 essais pour deviner les lettres avant de nous donner la réponse finale.")
input("Dès que vous êtes prêts, appuyez sur entrée...")

rand = randrange(0, len(LISTE_MOTS))
# mot à trouver
word_to_guess = LISTE_MOTS[rand]
# lettres dans le mot à trouver
# cette variable est nécessaire afin de contourner le problème des doublons mais aussi d'optimiser les performances de recherche
liste_lettre = list(set(word_to_guess))
# liste des lettres devinees
guessed_letters = []

# on initialise une variable i qui sera incrémenté à chaque nouvel essai
i = 0
# on affiche pour la première fois le mot à deviner
print("# " * len(word_to_guess))
# on boucle tant que le nombre d'essaie (i) est inférieur à 6 ET qu'il reste toujours des lettres à deviner
while i < MAX_TRIES and len(liste_lettre) > 0:
    # variable contenant la lettre que l'utilisateur veut deviner ce tour
    letter = ""
    # Tant que l'utilisateur n'envoie pas une seule lettre ou que cette lettre a déjà été envoyé,
    # on continue à lui demander de taper une lettre
    while len(letter) != 1 or letter in guessed_letters:
        letter = input("Taper une lettre : ").upper()
        # on affiche un message d'erreur pour les deux cas (plusieurs lettres ou lettre déjà deviné )
        if letter in guessed_letters:
            print("Attention : vous avez déjà deviné cette lettre !\n")
        elif len(letter) != 1:
            print("Erreur : vous ne devez taper qu'une seule lettre !\n")
    # une fois que les vérifications sont faîtes, on ajoute la lettre aux lettres devinés
    guessed_letters.append(letter)
    # si la lettre est présente dans le mot à trouver
    if letter in liste_lettre:
        # on enlève la lettre de la liste des lettres dans le mot à trouver
        liste_lettre.remove(letter)
    # on boucle sur les lettres du mot afin d'afficher le mot (ex: # # # # X # )
    for l in word_to_guess:
        # si la lettre du mot à deviner est présente dans la liste des lettres qui nous reste à deviner
        if l in liste_lettre:
            # on affiche "# "
            print("# ", end="")
        else:
            # sinon, ça veut dire que la lettre a été deviné donc on l'affiche
            print(f"{l} ", end="")
    # on affiche le nombre d'essai qu'il reste à l'utilisateur
    print(f"\nIl vous reste {MAX_TRIES - i - 1} essais...\n")
    # puis on incrémente le tour de 1
    i += 1
# A la fin, lorsque l'utilisateur n'a plus d'essaie ou lorsqu'il ne lui reste plus de lettres à deviner
# on lui demande de nous proposer le mot en entier
guessed = input("Devinez maintenant le mot : ").upper()

# si le mot correspond à celui qu'il fallait deviner
if guessed == word_to_guess:
    # on affiche gagné
    print("GAGNÉ !")
else:
    # sinon on affiche perdu
    print("PERDU !!!")
print(f"Le mot était '{word_to_guess}' !")
