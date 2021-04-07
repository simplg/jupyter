import random
import regex
import time
from tqdm import tqdm

class Timer:
    def __init__(self):
        self.reset()
    def reset(self):
        self.__start_time = 0
        self.__stop_time = 0
    def seconds(self):
        return int(self.__stop_time - self.__start_time) if self.__stop_time > 0 else 0
    def start(self):
        if self.__start_time == 0:
            self.__start_time = time.perf_counter()
    def stop(self):
        self.__stop_time = time.perf_counter()

class Motus:
    def __init__(self, username = "Joueur", age = 18, max_attempt = 8):
        self.liste_mots = []
        self.index_len_word = {}
        self.__max_attempt = max_attempt
        self.username = username
        self.age = age
        self.prepare_words()
        self.timer = Timer()
        self.reset()
    
    def total_games(self):
        return self.wins + self.losses
    
    def reset(self):
        self.selected_word = ""
        self.wins = 0
        self.losses = 0
        self.best_time = None
        self.timer.reset()

    def prepare_words(self):
        file = open("liste_mots.txt")
        for line in tqdm(file, desc="Chargement des mots"):
            word = line.strip()
            i = len(self.liste_mots)
            self.liste_mots.append(word)
            if len(word) not in self.index_len_word:
                self.index_len_word[len(word)] = []
            self.index_len_word[len(word)].append(i)
        print("Chargement terminé !")
    def is_valid(self, word):
        return len(word) == len(self.selected_word) and regex.match(r'^[A-Z]+$', word) != None and word in self.liste_mots[self.index_len_word[len(self.selected_word)][0]:]

    def word_hints(self, word):
        rt = ""
        for i in range(len(word)):
            if word[i]==self.selected_word[i]: 
                rt += word[i]+'#'
            elif word[i] in self.selected_word:
                rt += word[i]+'?'  
            else:
                rt += word[i].lower()
            rt += ' '
        return rt

    def play(self):
        print("Chaque jeu est chronométré, lorsque vous appuierez sur 'Entrée', le timer commencera !")
        self.timer.reset()
        self.timer.start()
        nb_letters = random.randint(min(self.index_len_word), max(self.index_len_word))
        self.selected_word = self.liste_mots[random.choice(self.index_len_word[nb_letters])]
        input("Appuyer sur Entrée pour continuer...")
        attempt = 0
        won = False
        print(f"Mot de {len(self.selected_word)} lettres : " + "X " * len(self.selected_word))
        while attempt < self.__max_attempt:
            print("")
            print(f"Essaie n°{attempt + 1}")
            word = ""
            while not self.is_valid(word):
                if word != "":
                    print(f"Erreur, veuillez taper un mot français ne contenant que des lettres sans accents et de longueur {len(self.selected_word)} !")
                word = input("Taper votre mot : ").upper()
            if word == self.selected_word:
                print(f"Bravo ! Le mot deviné était bien '{self.selected_word}'.")
                won = True
                break
            else:
                print(self.word_hints(word))
            attempt += 1
        self.timer.stop()
        if won:
            self.wins += 1
            print(f"Vous avez mis {self.timer.seconds()} secondes...")
            if self.best_time == None or self.timer.seconds() < self.best_time:
                print("Magnifique ! C'est votre meilleur temps !")
                self.best_time = self.timer.seconds()
        else:
            self.losses += 1
            print("Vous avez perdu !")
            print(f"Le mot à deviner était '{self.selected_word}'...")
        if input("Continuer à jouer ? (y/n)") == "y":
            self.play()
        else:
            print(f"Au revoir {self.username}!")
            print(f"Au cours de cette sessions, vous avez eu {self.wins} jeux gagnés et {self.losses} jeux perdus !")
                



def main():
    print("Bonjour et bienvenue dans le jeu du Motus !")
    print("Avant de commencer, j'aimerai vous connaître un peu plus...")
    name = input("Quel est votre pseudo ? ")
    age = 0
    try:
        age = int(input("Quel est votre age ? "))
    except ValueError:
        age = 0
    game = Motus(name, age=age)
    print(f"Hey, {name} !\nLa partie va commencer, tu peux quitter le programme avec CTRL + C à tout moment !")
    game.play()

if __name__ == "__main__":
    main()