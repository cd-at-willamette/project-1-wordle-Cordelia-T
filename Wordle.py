########################################
# Name: Cordelia Trueax
# Collaborators (if any): N/A (Aside from some discussion with Sophie)
# GenAI Transcript (if any): N/A
# Estimated time spent (hr):3-4
# Description of any added extensions: N/A
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.

    #    Keeps track of what the current row is
        curr_row = gw.get_current_row()

           # reads input on current line
        input = word_from_row(curr_row)


        # finds the letters which are the same in the input and to_guess
        for i in range(len(input)):
            if input[i].lower() == to_guess[i]:
                correct_letters.append(input[i])
        
        print(correct_letters)
        
                    # if the guess is an invalid word, displays according message
        if not valid_word(input):
            gw.show_message("Word is Invalid")

            # otherwise, the letters are colored and play goes on
        else:
            color_letters(input, curr_row)

                # if answer is correct, display win message
            if check_answer(input):
                gw.show_message("You got it! Be proud of yourself.")
               
                # if the game is not yet won, moves on to the next row
            else:
                    # if it's on the last row, the player has run out of turns
                if curr_row == N_ROWS:
                    gw.show_message("Out of Guesses 👎 The answer was: " + to_guess)
                    
                # otherwise it increments the row
                curr_row+=1
                gw.set_current_row(curr_row)

        

# =============================== Pre-Game Setup ====================================

    
    # picks a random word and assigns it to the to_guess variable
    # returns the five letter english word
    def set_to_guess():
        # a temporary variable to check if the word pulled out of ENGLISH_WORDS is 5 letters
        # initialized with a string that's not five letters but is replaced with the current word pulled out of the list
        temp = "not_five_letters"

        # while the length doesn't equal five
        while len(temp) != 5:
            temp = random.choice(ENGLISH_WORDS)
        
        return temp
    

    

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    # Sets the to_guess word before the game begins
    # to_guess = set_to_guess()
    # to_guess = "glass"
    to_guess = set_to_guess()
    print(to_guess)

    correct_letters = []


    # ===============================================================================




# ================================ Gameplay Functions ================================

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

            # determines which instance the current letter is out of the same letter in the word (e.g. 1st S, 2nd S, 3rd S...)
            # Is passed into check_letter to determine how many of each letter has been colored yellow
            for j in range(0, i+1):
                # convert to lower case so it may be properly compared
                curr_letter = guess[j].lower()
                
                copies = 0
                if curr_letter == to_guess[j]:
                    copies +=1
                

            # goes through the colors returned from check_letter, and colors the squares and keys
            match (check_letter(guess[i].lower(), i, copies, guess)):
            # match(check_letter(guess[i].lower(), i, guess)):
                case 'green':
                    gw.set_square_color(row, i, CORRECT_COLOR)
                    gw.set_key_color(guess[i], CORRECT_COLOR)
                
                case 'yellow':
                    gw.set_square_color(row, i, PRESENT_COLOR)
                    # doesn't recolor key if the letter has already been correctly guessed
                    if not guess[i] in correct_letters:
                        gw.set_key_color(guess[i], PRESENT_COLOR)

                case 'grey': 
                    gw.set_square_color(row, i, MISSING_COLOR)
                    gw.set_key_color(guess[i], MISSING_COLOR)

                case _:
                    gw.set_square_color(row, i, UNKNOWN_COLOR)






    # checks if the letter is in the word/ if its in the right spot - returns to color_letters function
    # guess_copies parameter is how many times the letter has shown up in the word before (and including) the current index
    def check_letter(letter: str, idx: int, guess_copy: int, guess: str) -> str:
    # def check_letter(letter: str, idx: int, guess: str) -> str:

        # converts everything to lower case
        letter = letter.lower()
        guess = guess.lower()

        # initializes variable to hold the number of times the letter shows up in to_guess
        to_guess_copies = 0


        # variable to hold the number of times a letter shows up in the word
        copies = 0
        # counts up how many times the letter appears
        for i in to_guess:
            if i == letter:
                to_guess_copies += 1
                
            # subtracts any instances where the correct placement has already been guessed
            for j in range(len(correct_letters)):
                if correct_letters[j].lower() == letter and j == idx:
                    to_guess_copies -= 1

        # if letter is at the current index, color green
        if to_guess[idx] == letter:
            return 'green'
        
        # else if letter in to_guess, but the letter hasn't repeated more times than it appears in the to_guess word, color yellow
        elif to_guess_copies > 0 and guess_copy <= to_guess_copies:
            return 'yellow'
        
        # else color grey
        else:
            return "grey"
        

#  ================================================================================



# Startup boilerplate
if __name__ == "__main__":
    wordle()







