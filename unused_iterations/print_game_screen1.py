"""Print the all letters guessed and un-guessed, and the hangman."""
from typing import List
import ascii_art


def print_game_screen(hangman_state: int, word_progress: str,
                      wrong_guesses: List[str]) -> None:
    """Print the hangman."""
    print(f"""{ascii_art.hangman[hangman_state]}

{word_progress}

Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses
else "None"}""")


if __name__ == '__main__':
    import unittest
    from unittest.mock import patch, call
    from get_random_word2 import get_random_word
    from random import randint, choice
    from string import ascii_letters

    class SimpleTest(unittest.TestCase):
        """Test that all output is correct."""

        @patch('builtins.print')
        def test_print(self, mocked):
            """Test the printing of every iteration of hangman."""
            calls = []
            used_words = []
            for i, _ in enumerate(ascii_art.hangman):
                random_word, used_words = get_random_word(used_words)
                random_chars = []
                for _ in range(randint(1, 26)):
                    random_chars.append(choice(ascii_letters))
                print_game_screen(i, random_word, random_chars)
                calls.append(
                    call(f"""{ascii_art.hangman[i]}

{random_word}

Wrong guesses: {', '.join(sorted(random_chars))}"""))
            self.assertEqual(mocked.mock_calls, calls)

    unittest.main()
