"""Check if the user's guess is in the word."""
from typing import Tuple, List


def check_letter_in_word(secret_word: str, user_guess: str, current_word: str,
                         wrong_guesses: List[str],
                         hangman_state: int) -> Tuple[str, List[str], int]:
    """Check if the user's guess is in the word.

    Args:
        secret_word (str): The secret word chosen by the program.
        user_guess (str): The user's guessed character.
        current_word (str): The current state of the word.
        wrong_guesses (List[str]): The wrong guesses the user has made.
        hangman_state (int): The state of the hangman.

    Returns:
        Tuple[str, List[str], int]: Return, respectively, the current state of
        the word, a list of wrong guesses, and the state of the hangman.
    """
    index_of_letters: List[int] = []

    for i, _ in enumerate(secret_word):
        if secret_word[i] == user_guess:
            index_of_letters.append(i)

    for i in index_of_letters:
        current_word = current_word[0:i] + user_guess + current_word[i + 1:]

    if not index_of_letters:
        wrong_guesses.append(user_guess)
        hangman_state += 1
    return current_word, wrong_guesses, hangman_state


if __name__ == '__main__':
    import unittest
    from string import ascii_letters
    testing_list_of_words: List[str] = [
        "hangman", "kanban", "evidence", "problem", "decomposed", "components",
        "developed", "trialled", "assembled", "tested", "create", "final",
        "working", "outcome"
    ]

    class SimpleTest(unittest.TestCase):
        """Test check_letter_in_word()."""

        def test_letters_replaced(self):
            """Test that the letter are replaced properly."""
            positions_of_letters = []
            # Test every word in the word list
            for secret_testing_word in testing_list_of_words:
                # Test those words against every letter
                for testing_guess in ascii_letters:
                    # Get the results of that combination of the word and
                    # character.
                    (result, wrong_guesses,
                     hangman_state) = check_letter_in_word(
                         secret_testing_word, testing_guess,
                         '_' * len(secret_testing_word), [], 0)

                    # Fill positions_of_letters with the positions of
                    # testing_guess in the secret_testing_word
                    for index, _ in enumerate(secret_testing_word):
                        if secret_testing_word[index] == testing_guess:
                            positions_of_letters.append(index)

                    # Check if the list has been populated with anything, if
                    # it hasn't check that the result is just a string the
                    # length of the word, but populated with underscores.
                    # Also, check if the character has been appended to the
                    # list of wrong guesses
                    if not positions_of_letters:
                        self.assertEqual(result,
                                         '_' * len(secret_testing_word))
                        self.assertEqual(wrong_guesses, [testing_guess])
                        # assert that the hangman state has been increased
                        self.assertEqual(hangman_state, 1)
                    else:
                        # If the testing list has been populated, check that
                        # the postions specified in positions_of_letters have
                        # the guessed character, and check that the other
                        # letters are just and underscore.
                        for character_index, _ in enumerate(result):
                            if character_index in positions_of_letters:
                                self.assertEqual(result[character_index],
                                                 testing_guess)
                            else:
                                self.assertEqual(result[character_index], '_')

                    positions_of_letters = []

    unittest.main()
