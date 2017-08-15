"""
on this app we are going to develop a dictionary. The cmd will ask you for a word
and it will find it for you. Also it will try to detect close to meaning words
in case the user makes a typo.
steps for this app
1. open json file as python dictionary
2. ask for word. put input into lower case
3. display the definition.
4. ask for a word again
"""
#loading dictionary in .json
import json
from difflib import get_close_matches

def definition(w):
    w = w.lower()
    if w in d:
        return "\n".join(d[w])
    elif get_close_matches(word, d, 1) != []:
        new= get_close_matches(word, d, 1)[0]
        yn = input("do you mean %s? y/n " % new)
        if yn == "y":
            return "\n".join(d[new])
        elif yn == 'n':
            return "I couldn't match what you word with any words in this dictionary. sorry"
        else:
            return "we didn't understand you entry"
    else:
        return "'"+ w + "'"+ " not found on the dictionary. Check you spelling o try another word"

d = json.load(open("./data.json", "r"))
word = input("type a word that you want to get the definition of: ")
print(definition(word))
