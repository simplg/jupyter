
import regex as re
s = "Mon texte lol"
re.sub(r'Mon (\w+) lol', '', s)