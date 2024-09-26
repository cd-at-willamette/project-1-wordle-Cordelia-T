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
        color_letters(input, 0)



    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    # Globals
    # to_guess = set_to_guess()
    to_guess = "stage"


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


    # colors letters - green if correct letter in correct spot, grey if incorrect letter, yellow if correct letter in wrong spot
    # input the guessed word in the game, and row it occurs in
    def color_letters(guess: str, row: int):
        # loops through letters in the guessed word
        for i in range(len(guess)):
            # counts up how many times the letter has appeared in the word, up to and including the current point 
            copies = 0
            for j in range(0,i+1):
                if guess[j] == guess[i]:
                    copies+=1

            # goes through the colors returned from check_letter, and colors the square
            match (check_letter(guess[i].lower(), i, copies)):
                case 'green':
                    gw.set_square_color(row, i, CORRECT_COLOR)
                
                case 'yellow':
                    gw.set_square_color(row, i, PRESENT_COLOR)

                case 'grey': 
                    gw.set_square_color(row, i, MISSING_COLOR)

                case _:
                    gw.set_square_color(row, i, UNKNOWN_COLOR)


    # checks if the letter is in the word/ if its in the right spot - returns to color_letters function
    # guess_copies parameter is how many times the letter has shown up in the word before (and including) the current index
    # LETTER SHOULD BE PASSED IN AS LOWER CASE
    def check_letter(letter: str, idx: int, guess_copy: int) -> str:

        # initializes the number of times the letter shows up in to_guess
        to_guess_copies = 0

        for i in to_guess:
            if i == letter:
                to_guess_copies+=1


        # if letter is at the current index, color green
        if to_guess[idx] == letter:
            return 'green'
        
        # else if letter in to_guess, but the letter hasn't repeated more times than it appears in the to_guess word, color yellow
        elif to_guess_copies > 0 and guess_copy <= to_guess_copies:
            return 'yellow'
        
        # else color grey
        else:
            return "grey"







# Startup boilerplate
if __name__ == "__main__":
    wordle()




