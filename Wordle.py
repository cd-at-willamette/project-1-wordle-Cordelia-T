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

    #    Keeps track of what the current row is
        curr_row = gw.get_current_row()
        print(curr_row)

        N_ROW = 5

        # # game ends if curr_row is beyond the last row (#5)
        # if curr_row>5:
           
        
        # but if game is not over...
        print("hi")

           # reads input on current line
        input = word_from_row(curr_row)
        
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
                if curr_row == N_ROW:
                    gw.show_message("Out of Guesses 👎 The answer was: " + to_guess)
                    
                # otherwise it increments the row
                curr_row+=1
                gw.set_current_row(curr_row)

        



    
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
    
    # Globals
    # to_guess = set_to_guess()
    # to_guess = "glass"
    to_guess = set_to_guess()
    print(to_guess)
    # to_guess = "lapsl"


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
            # (if letters are repeated, the last time around will be when it correcly colors everything since it counts up letters before occurence)
            # copies = [0,0,0,0,0]

            for j in range(0, i+1):
                # convert to lower case so it may be properly compared
                curr_letter = guess[j].lower()

                # print(curr_letter, to_guess[j])
                # if curr_letter == to_guess[j]:
                #     copies[j] = copies[j] + 1
                    

                # curr_letter == guess[i] and not
                # print(copies)
                
                
                copies = 0
                if curr_letter == to_guess[j]:
                    copies -=1
                    # print(copies)

                


            # subtracts from the potential copies if one of them is correctly placed - fixes the case where letters turn yellow without accounting for green further down the word
            # for j in to_guess:
            #     if guess[i] == :
            #         copies-=1

            # loop through both words 
            # if two of them have the same current letter in the same place, 
            # subtract 1 from copies

            # goes through the colors returned from check_letter, and colors the square
            match (check_letter(guess[i].lower(), i, copies, guess)):
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
    def check_letter(letter: str, idx: int, guess_copy: int, guess: str) -> str:
        # converts everything to lower case
        letter = letter.lower()
        guess = guess.lower()

        # initializes the number of times the letter shows up in to_guess
        to_guess_copies = 0

        for i in range(len(to_guess)):
            # print(to_guess[i]== guess[i])
            # print(to_guess[i], guess[i])
            # print(letter)
            if to_guess[i] == letter and not to_guess[i]==guess[i]:
                to_guess_copies+=1
            # print(to_guess_copies)


        # print(to_guess_copies)


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







