########################################
# Name: Cordelia Trueax
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        
        # word_to_row("Laugh", 0)
        # print(word_from_row(0))

        # testing if the program can correctly check an answer
        input = word_from_row(0)
        gw.show_message("Correct Answer: " + str(check_answer(input)) + ", Real Word: " + str(valid_word(input)))

        # and testing its ability to identify a valid 5 letter word
        print(valid_word("asdfh"))
        print(valid_word("brilliant"))
        print(valid_word("stack"))
        print(valid_word("a;soijeh"))


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    # Globals
    # to_guess = set_to_guess()
    to_guess = "guess"


    # prints letters from the word into the wordle grid one at a time 
    # input : 5 letter word
    def word_to_row(word : str, row : int):
        for i in range(len(word)):
            gw.set_square_letter(row, i, word[i])
 
    # returns the word currently printed in a given row
    def word_from_row(row : int) -> str:
        temp = ''
        # assembles the word by iterating through all the current letters
        for i in range(5):
            temp+= gw.get_square_letter(row, i)

        return temp
    
    # # defines the word that the player will guess
    # def set_to_guess():

    
    # given an input word, checks if word aligns with to_guess word
    # returns true if it is the same word, false otherwise
    def check_answer(word: str) -> bool:
        # convert word to lowercase before comparing
        word = word.lower()

        if word == to_guess:
            return True
        return False
    

    
    # checks if the input word is a valid word from the english list and if it is 5 letters
    # returns true if word fits these qualities, else returns false
    def valid_word(word: str) -> bool:
        # convert word to lowercase
        word = word.lower()

        if len(word) == 5 and word in ENGLISH_WORDS:
            return True
        
        return False








# Startup boilerplate
if __name__ == "__main__":
    wordle()




