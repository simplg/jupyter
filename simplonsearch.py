import os
from simplonutils import score2
from typing import Tuple
class File:
    content: str = ""
    filename: str = ""
    path: str = ""
    def __init__(self, path, filename) -> None:
        self.filename = filename
        self.path = path
        self.read()

    def read(self) -> str:
         with open(self.path + '/' + self.filename, encoding="utf-8") as f:
             for line in f.readlines():
                 self.content += line


def search(data: list[File]):
    scores: dict[str, int] = {}
    q = input('Taper votre recherche : (-1 pour quitter) ')
    if q == '-1':
        exit()
    for file in data:
        scores[file.filename] = score2(q, file.content)
    ls = sorted(scores.items(), key=lambda item: item[1])
    ls.reverse()
    scores = dict(ls)
    print(scores)
    search(data)
    

def main():
    print("Bienvenue dans le moteur de recherche SIMPLON !")
    files, path = getfiles()
    data: list[File] = []
    print("Chargement en cours...")
    for f in files:
        data.append(File(path, f))
    print("Chargement terminé !")
    search(data)


def getfiles() -> Tuple[list[str], str]:
    path = input("Dans quelle dossier voulez-vous chercher ? (defaut: dummytext) ")
    if path == '':
        path = 'dummytext'
    try:
        files = os.listdir(path)
        return files, path
    except FileNotFoundError as e:
        print("Le dossier n'existe pas, veuillez essayer à nouveau.")
    return getfiles()


if __name__ == "__main__":
    main()