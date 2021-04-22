import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        best_match = get_close_matches(word, data.keys())[0]
        response = input(
            "Did you mean %s instead?\nEnter Y if yes, or N if no: " % best_match)
        if response == "Y":
            return data[best_match]
        elif response == "N":
            return "The word doesn't exist."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist."


word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
