"""Contains the main routine and functions of the game."""
from typing import List

from calculate_score1 import calculate_score
from check_game_state2 import check_game_state
from check_letter_in_word2 import check_letter_in_word
from check_user_wants_to_play_again1 import check_user_wants_to_play_again
from get_guess2 import get_guess
from get_name1 import get_name
from get_random_word2 import get_random_word
from get_sequential_plays2 import get_sequential_plays
from greeting3 import greeting
from print_game_screen2 import print_game_screen
from thank_user_for_playing2 import thank_user_for_playing


def main():
    """Tie together all of the components of the game."""
    greeting()
    # The list of used_words is global so as to stop repeating words in a
    # session.
    used_words: List[int] = []
    # User_name is constant throughout the game.
    user_name: str = get_name()
    # A flag to end the game incase the program runs out of words
    list_of_words_not_empty = True
    # Score is global through every game as this is a total.
    score: int = 0
    while list_of_words_not_empty:
        sequential_turns: int = get_sequential_plays()
        while sequential_turns > 0:
            # A new word is selected after every game, and the guesses
            # are reset.
            wrong_guesses: List[str] = []
            secret_word, used_words = get_random_word(used_words)
            # Check that we haven't run out of words.
            if secret_word is None:
                list_of_words_not_empty = False
                print("Sorry, but we seem to have run out of words.")
                break
            # Make the current word the length of the secret word in
            # underscores.
            current_word = '_' * len(secret_word)
            while check_game_state(current_word, wrong_guesses):
                print_game_screen(current_word, wrong_guesses)
                user_guess = get_guess(current_word, wrong_guesses)
                (current_word,
                 wrong_guesses) = check_letter_in_word(secret_word, user_guess,
                                                       current_word,
                                                       wrong_guesses)
            score += calculate_score(secret_word, wrong_guesses)
            sequential_turns -= 1
        if list_of_words_not_empty:
            if not check_user_wants_to_play_again():
                break
    thank_user_for_playing(score, user_name)


if __name__ == '__main__':
    main()
