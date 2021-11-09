"""A hangman game."""
from typing import List, Optional, Tuple
from string import ascii_letters
from random import randint


def hangman_art(index) -> str:
    """Return the hangman_state."""
    hangman = [
        """








              """,
        """








==============""",
        """
|
|
|
|
|
|
|
|
+=============""",
        """
|
|
|
|
|
|
|\\
| \\
+=============""",
        """
|
| /
|/
|
|
|
|\\
| \\
+=============""",
        """
+—————————————
| /
|/
|
|
|
|\\
| \\
+=============""",
        """
+—————————————
| /          |
|/
|
|
|
|\\
| \\
+=============""",
        """
+—————————————
| /          |
|/          (_)
|
|
|
|\\
| \\
+=============""",
        """
+—————————————
| /          |
|/          (_)
|            |
|            |
|
|\\
| \\
+=============""",
        """
+—————————————
| /          |
|/          (_)
|            |
|           /|\\
|            |
|\\
| \\
+=============""",
        """
+—————————————
| /          |
|/          (_)
|            |
|           /|\\
|            |
|\\          / \\
| \\
+=============""",
    ]
    return hangman[index]


def calculate_score(secret_word: str, wrong_guesses: List[str]) -> int:
    """Calculate the user's final score.

    Args:
        secret_word (str): The secret word.
        wrong_guesses (List[str]): The list of wrong guesses

    Returns:
        int: The score for the game.
    """
    # We need to round the final value, as we use division and want to return
    # an integer. We add to the length of wrong_guesses, as if the user has
    # no wrong guesses, we get a divide by zero error. This approach was chosen
    # instead of rounding zero up to one, as that would give a player who made
    # one mistake, the same final score as a player who made zero mistakes.
    # We then multiply the result by 1000 to give an arcady feel.
    return round((len(secret_word) / (len(wrong_guesses) + 1)) * 1000)


def check_game_state(current_word: str, wrong_guesses: List[str]) -> bool:
    """Check if there are any _ left in the word or if hangman_state >= 9.

    Args:
        current_word (str): The current state of the word that the user sees.
        wrong_guesses (List[str]): The list of wrong guesses.

    Returns:
        bool: True if the game may continue, False if the game is over.
    """
    # You'll notice the statement current_word if current_word else ''
    # Therefore, if not current_word, the if statement checks if '_' is
    # in '', which will fail.
    if (len(wrong_guesses) < 10) and ('_' in (current_word
                                              if current_word else '')):
        return True
    return False


def check_letter_in_word(secret_word: str, user_guess: str, current_word: str,
                         wrong_guesses: List[str]) -> Tuple[str, List[str]]:
    """Check if the user's guess is in the word.

    Args:
        secret_word (str): The secret word chosen by the program.
        user_guess (str): The user's guessed character.
        current_word (str): The current state of the word.
        wrong_guesses (List[str]): The wrong guesses the user has made.

    Returns:
        Tuple[str, List[str], int]: Return, respectively, the current state of
        the word, and a list of wrong guesses.
    """
    index_of_letters: List[int] = []

    # append index_of_letters with the positions of user_guess in secret_word
    # this is because we're not replacing secret_word with user_guess, we're
    # replacing the corresponding positions in current_word with user_guess.
    for i, _ in enumerate(secret_word):
        if secret_word[i] == user_guess:
            index_of_letters.append(i)

    # Apparently, this is the only way to splice strings in python.
    for i in index_of_letters:
        current_word = current_word[0:i] + user_guess + current_word[i + 1:]

    # if there isn't anything in index_of_letters, the user guess isn't in
    # secret_word.
    if not index_of_letters:
        wrong_guesses.append(user_guess)
    return current_word, wrong_guesses


def check_user_wants_to_play_again() -> bool:
    """Ask the user if they would like to continue playing.

    Returns:
        bool: True if the user would like to continue playing, False otherwise.
    """
    while True:
        user_input = str(input("""Would you like to play some more [Y/N]: """))
        if user_input.lower() == 'y':
            return True
        if user_input.lower() == 'n':
            return False
        print("""Please enter either 'y' or 'n'.""")


def get_guess(current_word: str, wrong_guesses: List[str]) -> str:
    """Get a letter from the user.

    Args:
        current_word (str): The current state of the word.
        wrong_guesses (List[str]): The wrong guesses that the user has made.

    Returns:
        str: Return the validated letter.
    """
    while True:
        user_input = input("Please enter a letter: ")
        # Check that user_input is a string, as the next checks will
        # throw and exception if user_input isn't a string.
        if not isinstance(user_input, str):
            print("Please enter a letter between a and z")
            continue
        # Comparing the length of user input helps condense the empty
        # and too many characters checks into one check.
        if len(user_input) != 1:
            print("Please enter one letter")
            continue
        # Test if user input is alphabetical, and is ascii, in one go.
        if user_input not in ascii_letters:
            print("Please enter a letter between a and z")
            continue
        # Test if the user has entered the guess before.
        if user_input in current_word or user_input in wrong_guesses:
            print("Please enter a letter you haven't used")
            continue
        # We return user_input as lower case as everything in the program
        # is lower case.
        return user_input.lower()


def get_name() -> str:
    """Get the user's name for further use in the game.

    Returns:
        str: The name the player has entered.
    """
    while True:
        name = str(input("""
What is your name: """))
        if name and not name.isspace():
            return name
        print("""
Name cannot be a space.""")


def get_random_word(used_words: List[int]) -> Tuple[Optional[str], List[int]]:
    """Select a random word from a list and pass on a list of used words.

    Args:
        used_words (list): A list of the indexes of every already used word.

    Returns:
        Tuple[Optional[str], list]: The random word that is selected and a list
        of the index of every random word that has been selected.
    """
    list_of_words: List[str] = [
        "hangman", "kanban", "evidence", "problem", "decomposed", "components",
        "developed", "trialled", "assembled", "tested", "create", "final",
        "working", "outcome"
    ]
    if len(used_words) == len(list_of_words):
        # if len(used_words) == len(list_of_words), when line 26 and 27
        # run, it will just delete every word from list_of_words, so we
        # save the computational energy, and another if statement to check
        # if list_of_words_without_used_words is empty, and just return
        # None as the word, thus signalling to the caller, that the word
        # list is empty.
        return None, used_words
    list_of_words_without_used_words: List[str] = list_of_words.copy()
    for i in sorted(used_words, reverse=True):
        # used_words is looped through in reverse for this as, when in
        # reverse, the 'popping' of an list item at index 'i' will
        # never effect a higher index list item, as that higher index
        # list item has already been popped.
        list_of_words_without_used_words.pop(i)
    # len(list_of_words_without_used_words) - 1 because, lists start
    # at index 0.
    random_number: int = randint(0, len(list_of_words_without_used_words) - 1)
    word = list_of_words_without_used_words[random_number]
    # because random_number picks a word from a popped version of
    # list_of_words, we can't directly translate the index of the word in
    # list_of_words_without_used_words to the index of the word in
    # list_of_words, therefore, we have to use the list.index()
    # function to find the index of the word in the full list.
    used_words.append(list_of_words.index(word))
    return word, used_words


def get_sequential_plays() -> int:
    """Get the sequential number of times the player wants to play.

    Returns:
        An integer between and including 1 to 10.
    """
    while True:
        try:
            # take plays as a float to account for users inputing floats
            # as casting to int() will just truncate an entered float.
            plays = float(
                input("""
How many times would you like to play [1-10]: """))
        except ValueError:
            print("""
You must enter a number, e.g. 1, 5, 8, 9.""")
            continue
        # Test whether plays is a whole number.
        if plays % 1 != 0:
            print("""
You must enter a whole number, e.g. 1, 5, 8, 9.""")
            continue
        # and if plays is a whole number, safely cast to int()
        plays = int(plays)
        if 1 <= plays <= 10:
            return plays
        print("""
The number must between from 0 and 11, e.g. 1, 5, 8, 9""")


def greeting() -> None:
    """Greet the user and explain the rules of the game.

    Args:
        None
    Returns:
        None
    """
    input("""
Hello, and welcome to hangman. You have ten turns to guess the randomly
selected word, letter by letter. If the letter you guess is in the word
you are guessing, the letter will appear on the word. If the letter you
guess is incorrect, you will lose a turn, and another part of the
gallows will be drawn. If the entire gallows and person is drawn, which
takes ten wrong guesses, you lose the game. You win the game by guessing
the word.
There will be three panels, one will have the amount of guesses you
have left, represented as a progressively drawn gallows and man.
There is another panel which will start out as a line of underscores,
and will fill up with your correctly guessed letters, The third panel
will fill up with your incorrectly guessed letters. You can guess
letters by pressing the corresponding key on your keyboard.

Press Enter to continue""")


def print_game_screen(word_progress: str, wrong_guesses: List[str]) -> None:
    """Print the hangman.

    Args:
        word_progress (str): The progress of the word.
        wrong_guesses (List[str]): The wrong guesses of the user.
    """
    print(f"""{hangman_art(len(wrong_guesses))}

{' '.join(word_progress.upper())}

Wrong guesses: {', '.join(sorted(wrong_guesses)).upper() if wrong_guesses
else "None"}""")


def thank_user_for_playing(score, user_name):
    """Thank the user for playing and display the final score."""
    print(f"""
Thank you for playing hangman {user_name}!
Your final score is: {score}""")


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
