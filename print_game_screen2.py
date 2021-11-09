"""Print the all letters guessed and un-guessed, and the hangman."""
from typing import List
import ascii_art


def print_game_screen(word_progress: str, wrong_guesses: List[str]) -> None:
    """Print the hangman.

    Args:
        word_progress (str): The progress of the word.
        wrong_guesses (List[str]): The wrong guesses of the user.
    """
    print(f"""{ascii_art.hangman[len(wrong_guesses)]}

{word_progress}

Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses
else "None"}""")


if __name__ == '__main__':
    import unittest
    from unittest.mock import patch, call
    from get_random_word2 import get_random_word
    from random import choice
    from string import ascii_letters

    class SimpleTest(unittest.TestCase):
        """Test that all output is correct."""

        @patch('builtins.print')
        def test_print(self, mocked):
            """Test the printing of every iteration of hangman."""
            calls = []
            used_words = []
            for _, _ in enumerate(ascii_art.hangman):
                random_word, used_words = get_random_word(used_words)
                random_chars = []
                for _ in range(1, len(ascii_art.hangman)):
                    random_chars.append(choice(ascii_letters))
                print_game_screen(random_word, random_chars)
                calls.append(
                    call(f"""{ascii_art.hangman[len(random_chars)]}

{random_word}

Wrong guesses: {', '.join(sorted(random_chars))}"""))
            self.assertEqual(mocked.mock_calls, calls)

    unittest.main()
