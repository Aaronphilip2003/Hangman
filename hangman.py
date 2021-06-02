import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:

        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives)
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')


    if lives == 0:
        print(lives)
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
























# from words import words
# import random
# import string
#
# def get_valid_word(words):
#     word=random.choice(words)
#     while '-' or ' ' in word:
#         word=random.choice(words)
#
#     return word.upper()
#
# def hangman1():
#     word=get_valid_word(words)
#     word_letters=set(word)
#     alphabet=set(string.ascii_letters)
#     used_letter=set()
#
#
#
#     while len(word_letters) > 0:
#         print("You have used these letters: ", ' '.join((used_letter)))
#
#         word_list = [letter if letter in used_letter else '_' for letter in word]
#         print('Current Word:'.join(word_list))
#
#         user_letter=input("Guess a letter").upper()
#         if user_letter in alphabet - used_letter :
#             used_letter.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#
#         elif user_letter in used_letter:
#             print("You already Guessed that letter:")
#
#         else:
#             print("Invalid Character. Please try again .")
#
# if __name__ == '__main__':
#     hangman1()