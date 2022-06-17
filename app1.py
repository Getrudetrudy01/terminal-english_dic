#a terminal program for a english dictionary
import json
from difflib import get_close_matches

data = json.load(open("2.1 data.json.json"))
'''this is a comment on the fuction translate created below
we could also write the function as this
def translate(word)
    if word in data:
        return data[word]
    else:
        return "the word does not exit. please double
        check it..
    word = input("Enter word: ")
    print(translate(word))
    and the argument that would be passed would be 
    word too. there are just two different ways to 
    get the same result.'''
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif len(get_close_matches(w,data.keys())) > 0:
        '''basically, we using close matched because it 
        will output to the user the best matches of the word 
        the user will enter assuming there is a mistake. '''
        yn= input("Did you mean instead? Enter Y if yes, or N if no."% get_close_matches(w, data.keys()) [0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "We do not understand what you entered please"
    else:
        return "The word does not exist. Please doulbe check it..."

word = input("Enter word: ")

print(translate(word))


output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
    else:
        print(output)