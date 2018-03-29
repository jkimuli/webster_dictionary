"""
   This script provides a command line interface to a dictionary of words.
   Word meanings can then be searched by entering the word on the command line

   ***  Author - Julius Kimuli *****
   ***  Email  - jkimuli@gmail.com *****

"""

import json
from difflib import get_close_matches
from colorama import Back, Fore, Style,init

# open the dictionary.json file representing the text of the dictionary


def load_words():

    try:

        fp = open("data.json", "r")

        dictionary_data = json.load(fp)

        return dictionary_data

    except Exception as e:

        print(str(e))


def search_word(word_input):

    # return a list of valid words from the dictionary

    valid_words = load_words()

    # translate search word to lowercase

    search_key = word_input.lower()

    # set all dictionary keys to lowercase if not already lowercase

    valid_words = {k.lower(): v for k, v in valid_words.items()}

    if search_key in valid_words.keys():

        print("\nSearch Word :  %s" % search_key)

        print("Word Meanings: \n")

        for definition in valid_words[search_key]:

            print("\t - %s" % definition)  # returns for exact word match in our dictionary keys

    elif len(get_close_matches(search_key,valid_words.keys())) > 0:

        print(Fore.RED + "\n The exact word searched for doesn't exist in the dictionary!")
        print(Style.RESET_ALL)

        print("Please try searching again:")
        print("Here is a list of suggested similar words")

        for element in get_close_matches(search_key,valid_words.keys()):

            print(Fore.BLUE + "\t - %s" % element)

        print(Style.RESET_ALL)

    else:

        print(Fore.RED + "The searched for word is not available in the  dictionary,Please double check it! ")
        print(Style.RESET_ALL)

if __name__ == '__main__':

    init()  # initialize colorama to provide color to our terminal

    print(Fore.GREEN + "\n*********************************************************************\n")

    print("Welcome to my Interactive English dictionary Application \n")

    print("Copyright Julius Kimuli  \xA9 2018")

    print(Fore.GREEN + "\n*********************************************************************\n")

    print(Style.RESET_ALL) # reset to default terminal color settings

    continue_loop = True

    while continue_loop:

        word = input("\nPlease enter the name of the word to be search or press qx to quit: ")

        if word.lower() == 'qx':
            continue_loop = False
        else:
            search_word(word)