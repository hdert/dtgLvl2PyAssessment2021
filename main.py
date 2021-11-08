"""Contains the main routine and functions of the game."""
from typing import List

from calculate_score1 import calculate_score
from check_game_state1 import check_game_state
from check_letter_in_word1 import check_letter_in_word
from check_user_wants_to_play_again1 import check_user_wants_to_play_again
from get_guess2 import get_guess
from get_name1 import get_name
from get_random_word2 import get_random_word
from get_sequential_plays2 import get_sequential_plays
from greeting3 import greeting
from print_game_screen1 import print_game_screen
from thank_user_for_playing2 import thank_user_for_playing


def main():
    """Tie together all of the components of the game."""
    greeting()
    used_words: List[int] = []
    user_name: str = get_name()
    list_of_words_not_empty = True
    while list_of_words_not_empty:
        sequential_turns: int = get_sequential_plays()
        while sequential_turns > 0:
            hangman_state: int = 0
            wrong_guesses: List[str] = []
            score: int = 0
            secret_word, used_words = get_random_word(used_words)
            if secret_word is None:
                list_of_words_not_empty = False
                break
            current_word = '_' * len(secret_word)
            while check_game_state(current_word, hangman_state):
                print_game_screen(hangman_state, current_word, wrong_guesses)
                user_guess = get_guess(current_word, wrong_guesses)
                (current_word, wrong_guesses,
                 hangman_state) = check_letter_in_word(secret_word, user_guess,
                                                       current_word,
                                                       wrong_guesses,
                                                       hangman_state)
            score += calculate_score(secret_word, wrong_guesses)
            sequential_turns -= 1
        if list_of_words_not_empty:
            if not check_user_wants_to_play_again():
                break
    thank_user_for_playing(score, user_name)


if __name__ == '__main__':
    main()
