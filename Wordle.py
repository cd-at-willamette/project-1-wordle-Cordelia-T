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
        # gw.show_message("You need to implement this method")
        word_to_row("Sofie", 0)
        print(word_from_row(0))


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


    # prints letters from the word into the wordle grid one at a time 
    # input : 5 letter word
    def word_to_row(word : str, row : int):
        for i in range(len(word)):
            gw.set_square_letter(row, i, word[i])
 
    def word_from_row(row : int) -> str:
        temp = ''

        for i in range(5):
            temp+= gw.get_square_letter(row, i)

        return temp




# Startup boilerplate
if __name__ == "__main__":
    wordle()




