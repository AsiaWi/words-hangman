# I have used the following links to help me with the game:
# https://www.askpython.com/python/examples/hangman-game-in-python
# https://codefather.tech/blog/hangman-game-python/?utm_content=cmp-true

import random
import hangman
import os

from pyfiglet import Figlet
f = Figlet(font='slant')

from english_words import get_english_words_set
web2set = get_english_words_set(['web2'])


def clear():
    '''
    Clears terminal
    '''

    os.system("clear")


def users_level_choice():
    '''
    Provides user with choice of game levels
    allows user to select the level of choice
    Try method will convert input to int,
    will raise an error if input is not a number
    and if number entered is not 1 or 2
    '''

    while True:
        game_level = input('Enter 1 for beginners or 2 for advanced level: ')
        print()

        try:
            game_level = int(game_level)
        except ValueError:
            print('Numbers only')
            continue
        if 1 <= game_level <= 2:
            return game_level
            break
        else:
            print('Number outside the allowed range')

    clear()


def pick_random_word(web2set, game_level):
    '''
    Will select a random question from a list
    word length of 7 for begginers
    and word length of more than 7 for advanced level
    words < 7 not in the game
    '''

    word = random.choice(web2set).upper()

    if game_level == 1:
        while len(word) != 7:
            word = random.choice(web2set).upper()
    else:
        while len(word) < 7 or len(word) == 7:
            word = random.choice(web2set).upper()

    return word


def print_the_word(correct_guess, word):
    '''
    Will display the word to terminal
    underscore will be displayed for each letter
    unless letter already guessed by user
    '''

    for alpha in word:
        if alpha in correct_guess:
            print(f' {alpha} ', end='')
        else:
            print(' _ ', end='')


def letter_choice():
    '''
    Will take and verify users guess
    if input not a letter or longer than 1
    a user will see an error and input option again
    '''

    letter = input('  Enter the letter here:')
    while len(letter) != 1 or not letter.isalpha():
        print('  Please enter only single letters')
        letter = input('  Enter the letter here:')
    return (letter.upper())


def start_again():
    '''
    Will provide an option for user to start again
    and will verify users input
    Try method will convert the input to number,
    and provide error if not an int.
    will only accept 1 and then break the loop and
    take user back to main function to run program again
    '''

    while True:

        new_game = input('Press 1, if you want to start again!: ')

        try:
            new_game = int(new_game)
        except ValueError:
            print('Incorrect input, try again')
            continue
        if new_game == 1:
            main()
            break
        else:
            print('Invalid number')


def game_over(word, chances):
    '''
    Checks if user used all available chances,
    if so the function returns true and
    the game_loop breaks.
    If not, the function returns false and the
    game_loop continues
    '''

    if chances == 7:
        clear()
        print()
        print(f.renderText(' game over '))
        print(f'                 The word was: {word}  ')
        return True
    else:
        return False


def winner(word, correct_guess):
    '''
    Checks if the length of correctly guessed letters in
    correct_guess list equals the word set length.
    If so the function returns true and
    the game_loop breaks.
    If not, the function returns false and the
    game_loop continues
    '''

    if len(set(word)) == len(correct_guess):
        clear()
        print()
        print('                                 CONGRATULATIONS!')
        print(f.renderText('       you won ! '))
        print(f'                         {word} is the correct guess')
        return True
    else:
        return False


def game_loop(word):
    '''
    Inside game loop runs the whole game
    Starts after a word for appropriate level chosen by user has been selected.
    Updates chances needed for game over function.
    Stores correct and incorrect guessed letters in a relevant list.
    Displays and updates hangman feature with each incorrect guess.
    Checks if guessed letter is in the word, correct_guess
    or incorrect_guess list-
    then displays relevant message.
    Displays and updates remaining lives.
    '''

    chances = 0
    lives = 7
    correct_guess = []
    incorrect_guess = []
    hangman_values = ['O', '/', '|', '\\', '|', '/', '\\']
    update_display_hangman = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

    while True:
        print(word)  # to be removed before submitting
        hangman.print_hangman(update_display_hangman)
        print_the_word(correct_guess, word)
        print('\n')
        print('  Letters you guessed incorrectly: ', incorrect_guess)
        print()
        print(f'  You have {lives} lives left!')
        print()
        letter = letter_choice()

        if letter in word:
            if letter in correct_guess:
                clear()
                print()
                print("  You have already used this letter! Try again")
                continue
            else:
                clear()
                print()
                print('  Yeey! Great job!')
                correct_guess += letter
                if winner(word, correct_guess):
                    hangman.print_hangman_win()
                    start_again()
                    break
                continue
        else:
            if letter in incorrect_guess:
                clear()
                print()
                print('  You have already used this letter. Try again!')
                continue

            else:
                update_display_hangman[chances] = hangman_values[chances]
                chances += 1
                lives -= 1
                if game_over(word, chances):
                    hangman.print_hangman(update_display_hangman)
                    start_again()
                    break
                else:
                    clear()
                    print()
                    print("  Bad luck! Letter isn't part of the word")
                    incorrect_guess += letter
                    continue
        clear()


def main():
    '''
    Run the program
    outside game loop
    '''

    clear()
    print()
    print(f.renderText('. . Welcome to . .'))
    print(f.renderText(' H a n g m a n !'))
    word_list = list(web2set)
    game_level = users_level_choice()
    clear()
    word = pick_random_word(word_list, game_level)
    game_loop(word)


main()
