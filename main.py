import json
import difflib

data = json.load(open('data.json'))


# function to get the meaning for user input
def meaning(user_input):
    user_input = user_input.lower().strip()
    if user_input in data:
        output = data.get(user_input)
        return output
    else:
        close_match = difflib.get_close_matches(user_input, data)
        if len(close_match) > 0:
            secound_input = input("Did you mean {}? if Yes press 'Y', If No press 'N' :".format(close_match[0]))

            if secound_input.strip().lower() == 'y':
                return data.get(close_match[0])
            elif secound_input.strip().lower() == 'n':
                return 'please recheck your input'
            else:
                return 'Sorry didnt understand your input'
        else:

            return "Sorry I didn't understand please recheck your input"


# get the user input
user_input = input("enter your word: ")

output = meaning(user_input)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
